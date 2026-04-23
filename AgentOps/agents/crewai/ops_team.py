"""
CrewAI - DevOps / AgentOps Operations Team
Demonstrates: Role-based multi-agent collaboration for ops tasks
Agents: Planner, Coder, Reviewer, Security Auditor, Deployer
"""

from crewai import Agent, Task, Crew, Process
from crewai.tools import BaseTool
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama
from pydantic import Field
import os

# ─────────────────────────────────────────────
# LLM Configuration (swap between Ollama / OpenAI)
# ─────────────────────────────────────────────
USE_LOCAL = os.getenv("USE_LOCAL_LLM", "true").lower() == "true"

if USE_LOCAL:
    llm = Ollama(model=os.getenv("OLLAMA_MODEL", "llama3"), base_url="http://ollama:11434")
else:
    llm = ChatOpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))

# ─────────────────────────────────────────────
# Custom Tools
# ─────────────────────────────────────────────
class DockerInspectTool(BaseTool):
    name: str = "docker_inspect"
    description: str = "Inspect a running Docker container's status and resource usage"

    def _run(self, container_name: str) -> str:
        import subprocess
        result = subprocess.run(
            ["docker", "stats", "--no-stream", "--format",
             "{{.Name}}: CPU={{.CPUPerc}} MEM={{.MemUsage}}", container_name],
            capture_output=True, text=True
        )
        return result.stdout or f"Container {container_name} not found"


class GitLogTool(BaseTool):
    name: str = "git_log"
    description: str = "Fetch recent git commits from a repository path"

    def _run(self, repo_path: str = ".") -> str:
        import subprocess
        result = subprocess.run(
            ["git", "-C", repo_path, "log", "--oneline", "-10"],
            capture_output=True, text=True
        )
        return result.stdout or "No git history found"


class SecurityScanTool(BaseTool):
    name: str = "security_scan"
    description: str = "Run a basic security scan on a Python file or directory"

    def _run(self, target: str) -> str:
        import subprocess
        result = subprocess.run(
            ["bandit", "-r", target, "-f", "text", "-q"],
            capture_output=True, text=True
        )
        return result.stdout or result.stderr or "Scan complete — no issues found"


# ─────────────────────────────────────────────
# Agents
# ─────────────────────────────────────────────
planner = Agent(
    role="Ops Planner",
    goal="Break down operations tasks into clear, actionable subtasks for the team",
    backstory=(
        "You are a senior DevOps architect with 15 years of experience. "
        "You plan infrastructure changes, CI/CD pipelines, and agent workflows "
        "with precision and foresight."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=True,
)

coder = Agent(
    role="Ops Engineer",
    goal="Write production-quality infrastructure code, scripts, and agent implementations",
    backstory=(
        "You are an expert SRE and Python developer who writes clean, efficient "
        "Dockerfiles, Terraform, and automation scripts."
    ),
    llm=llm,
    tools=[DockerInspectTool(), GitLogTool()],
    verbose=True,
)

security_auditor = Agent(
    role="Security Auditor",
    goal="Identify and fix security vulnerabilities in code and infrastructure",
    backstory=(
        "You are a cybersecurity expert specializing in cloud-native security, "
        "OWASP compliance, and DevSecOps practices."
    ),
    llm=llm,
    tools=[SecurityScanTool()],
    verbose=True,
)

reviewer = Agent(
    role="Code Reviewer",
    goal="Review code for quality, correctness, and best practices before deployment",
    backstory=(
        "You are a meticulous senior engineer who ensures all code meets "
        "high standards for reliability, observability, and maintainability."
    ),
    llm=llm,
    verbose=True,
)

deployer = Agent(
    role="Deployment Specialist",
    goal="Deploy services safely using blue-green or canary strategies",
    backstory=(
        "You are a deployment expert who uses Kubernetes, Docker Compose, "
        "and GitOps pipelines to deploy services with zero downtime."
    ),
    llm=llm,
    tools=[DockerInspectTool()],
    verbose=True,
)

# ─────────────────────────────────────────────
# Tasks
# ─────────────────────────────────────────────
plan_task = Task(
    description=(
        "Plan a deployment of a new microservice called 'agent-gateway' that "
        "routes requests to multiple AI agents. Include: service dependencies, "
        "required environment variables, health checks, and rollout strategy."
    ),
    expected_output="A detailed deployment plan with all steps and dependencies listed",
    agent=planner,
)

code_task = Task(
    description=(
        "Write a Docker Compose service definition and a Python FastAPI entrypoint "
        "for the 'agent-gateway' service based on the deployment plan."
    ),
    expected_output="A docker-compose service block and a main.py FastAPI app for agent-gateway",
    agent=coder,
    context=[plan_task],
)

security_task = Task(
    description=(
        "Review the generated code and Docker configuration for security issues. "
        "Check for: hardcoded secrets, insecure defaults, OWASP Top 10 violations, "
        "and overly permissive container settings."
    ),
    expected_output="Security report with findings and recommended fixes",
    agent=security_auditor,
    context=[code_task],
)

review_task = Task(
    description=(
        "Review the agent-gateway code and deployment config for quality. "
        "Ensure proper error handling, logging, health endpoints, and documentation."
    ),
    expected_output="Code review report with specific line-level recommendations",
    agent=reviewer,
    context=[code_task, security_task],
)

deploy_task = Task(
    description=(
        "Generate a deployment checklist and deployment command sequence for "
        "rolling out agent-gateway to production using docker compose."
    ),
    expected_output="Step-by-step deployment checklist and commands",
    agent=deployer,
    context=[review_task],
)

# ─────────────────────────────────────────────
# Crew
# ─────────────────────────────────────────────
ops_crew = Crew(
    agents=[planner, coder, security_auditor, reviewer, deployer],
    tasks=[plan_task, code_task, security_task, review_task, deploy_task],
    process=Process.sequential,
    verbose=True,
    memory=True,          # Enable crew-level memory
    embedder={
        "provider": "ollama",
        "config": {"model": "nomic-embed-text", "base_url": "http://ollama:11434"}
    },
)

if __name__ == "__main__":
    print("🤖 Starting AgentOps CrewAI Ops Team...\n")
    result = ops_crew.kickoff()
    print("\n✅ Crew completed task:\n")
    print(result)
