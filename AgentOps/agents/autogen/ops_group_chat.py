"""
AutoGen (Microsoft) - Ops Multi-Agent Conversation System
Demonstrates: Conversational agents, tool use, group chat, and code execution
for DevOps / AgentOps automation tasks
"""

import os
import autogen
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager
from autogen.coding import LocalCommandLineCodeExecutor
from pathlib import Path

# ─────────────────────────────────────────────
# LLM Configuration
# ─────────────────────────────────────────────
USE_LOCAL = os.getenv("USE_LOCAL_LLM", "true").lower() == "true"

if USE_LOCAL:
    llm_config = {
        "config_list": [
            {
                "model": os.getenv("OLLAMA_MODEL", "llama3"),
                "base_url": "http://ollama:11434/v1",
                "api_key": "ollama",  # required but unused for Ollama
            }
        ],
        "temperature": 0.1,
        "timeout": 120,
    }
else:
    llm_config = {
        "config_list": [
            {
                "model": "gpt-4o",
                "api_key": os.getenv("OPENAI_API_KEY"),
            }
        ],
        "temperature": 0.1,
    }

# ─────────────────────────────────────────────
# Code Executor (sandboxed local execution)
# ─────────────────────────────────────────────
executor = LocalCommandLineCodeExecutor(
    timeout=30,
    work_dir=Path("/tmp/autogen_ops_workspace"),
)

# ─────────────────────────────────────────────
# Agents
# ─────────────────────────────────────────────

# User Proxy — acts as the human operator, can execute code
ops_engineer = UserProxyAgent(
    name="OpsEngineer",
    human_input_mode="NEVER",          # Fully automated — set to "ALWAYS" for interactive
    max_consecutive_auto_reply=5,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"executor": executor},
    system_message=(
        "You are a senior ops engineer. You review proposed solutions, "
        "execute code safely, and report results. When a task is complete, "
        "reply with TERMINATE."
    ),
)

# Planner — breaks down tasks
planner = AssistantAgent(
    name="OpsPlannerAgent",
    llm_config=llm_config,
    system_message=(
        "You are an ops planning expert. When given a task, break it down into "
        "clear numbered steps. Assign each step to the appropriate specialist: "
        "InfraAgent, SecurityAgent, or MonitoringAgent. Be concise and precise."
    ),
)

# Infrastructure specialist
infra_agent = AssistantAgent(
    name="InfraAgent",
    llm_config=llm_config,
    system_message=(
        "You are an infrastructure expert specializing in Docker, Kubernetes, "
        "Terraform, and cloud platforms. Write production-grade infrastructure "
        "code and shell scripts. Always include error handling and comments."
    ),
)

# Security specialist
security_agent = AssistantAgent(
    name="SecurityAgent",
    llm_config=llm_config,
    system_message=(
        "You are a security expert specializing in DevSecOps, OWASP, secrets "
        "management, and cloud security. Review all code for security issues. "
        "Flag vulnerabilities with severity (HIGH/MEDIUM/LOW) and remediation steps."
    ),
)

# Monitoring specialist
monitoring_agent = AssistantAgent(
    name="MonitoringAgent",
    llm_config=llm_config,
    system_message=(
        "You are a monitoring expert specializing in Prometheus, Grafana, "
        "Loki, and distributed tracing. Design observability solutions and "
        "write PromQL queries, alert rules, and dashboard configs."
    ),
)

# Critic — reviews final output
critic = AssistantAgent(
    name="CriticAgent",
    llm_config=llm_config,
    system_message=(
        "You are a senior tech lead and critic. Review all proposed solutions "
        "for correctness, security, reliability, and maintainability. "
        "Provide specific, actionable feedback. If satisfied, say 'APPROVED'."
    ),
)

# ─────────────────────────────────────────────
# Group Chat
# ─────────────────────────────────────────────
group_chat = GroupChat(
    agents=[ops_engineer, planner, infra_agent, security_agent, monitoring_agent, critic],
    messages=[],
    max_round=20,
    speaker_selection_method="auto",   # LLM-driven speaker selection
    allow_repeat_speaker=False,
)

manager = GroupChatManager(
    groupchat=group_chat,
    llm_config=llm_config,
)


# ─────────────────────────────────────────────
# Ops Tasks
# ─────────────────────────────────────────────
OPS_TASKS = [
    """
    Task: Set up a production-ready monitoring stack for our agent-gateway microservice.
    Requirements:
    - Prometheus scraping every 15s
    - Grafana dashboard with: request rate, error rate, p99 latency, memory usage
    - Alert rules: error rate > 5%, p99 > 2s, memory > 80%
    - All config as code (no manual clicks)
    Please provide: Prometheus config, Grafana dashboard JSON, and alert rules YAML.
    """,
    
    """
    Task: Harden the agent-gateway Docker container for production.
    Requirements:
    - Run as non-root user
    - Read-only filesystem where possible
    - Drop all Linux capabilities, add only required ones
    - Set resource limits (CPU: 2 cores, Memory: 512Mi)
    - Health check with proper timeout
    - No secrets in environment variables (use Docker secrets or Vault)
    Please provide: Hardened Dockerfile and docker-compose service block.
    """,
]


# ─────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────
def run_ops_task(task: str):
    print(f"\n{'='*60}")
    print(f"TASK: {task[:100].strip()}...")
    print(f"{'='*60}\n")

    chat_result = ops_engineer.initiate_chat(
        manager,
        message=task.strip(),
        summary_method="reflection_with_llm",
    )

    print(f"\n{'='*60}")
    print("SUMMARY:")
    print(chat_result.summary)
    print(f"{'='*60}\n")
    return chat_result


if __name__ == "__main__":
    import sys
    task_idx = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    run_ops_task(OPS_TASKS[task_idx % len(OPS_TASKS)])
