"""
OpenAgents-style Tool-Augmented Agent
Demonstrates: ReAct-style agent with rich tool ecosystem for ops tasks
Uses: LangChain AgentExecutor + custom tool registry pattern

OpenAgents (XAgent/OpenAgents) pattern: plugin-style tools with
structured tool descriptions, approval gates, and streaming output.
"""

import os
import json
import subprocess
from datetime import datetime
from typing import Optional

from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.tools import StructuredTool, tool
from langchain_community.chat_models import ChatOllama
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from pydantic import BaseModel, Field

# ─────────────────────────────────────────────
# LLM
# ─────────────────────────────────────────────
USE_LOCAL = os.getenv("USE_LOCAL_LLM", "true").lower() == "true"
if USE_LOCAL:
    llm = ChatOllama(
        model=os.getenv("OLLAMA_MODEL", "llama3"),
        base_url="http://ollama:11434",
        callbacks=[StreamingStdOutCallbackHandler()],
    )
else:
    llm = ChatOpenAI(
        model="gpt-4o",
        api_key=os.getenv("OPENAI_API_KEY"),
        streaming=True,
        callbacks=[StreamingStdOutCallbackHandler()],
    )


# ─────────────────────────────────────────────
# Tool Input Schemas
# ─────────────────────────────────────────────
class ServiceHealthInput(BaseModel):
    service_name: str = Field(description="Name of the Docker service to check")
    include_logs: bool = Field(default=False, description="Include last 10 log lines")


class ScaleServiceInput(BaseModel):
    service_name: str = Field(description="Name of the service to scale")
    replicas: int = Field(description="Target number of replicas (1-10)", ge=1, le=10)


class QueryMetricsInput(BaseModel):
    promql: str = Field(description="PromQL query to execute")
    prometheus_url: str = Field(default="http://prometheus:9090", description="Prometheus URL")


class ShellCommandInput(BaseModel):
    command: str = Field(description="Safe, non-destructive shell command to run")
    timeout: int = Field(default=10, description="Timeout in seconds", ge=1, le=60)


class SearchLogsInput(BaseModel):
    service_name: str = Field(description="Service name to search logs for")
    pattern: str = Field(description="grep pattern to search for")
    tail: int = Field(default=100, description="Number of lines to search from end", ge=10, le=1000)


# ─────────────────────────────────────────────
# Tool Implementations
# ─────────────────────────────────────────────
def check_service_health_fn(service_name: str, include_logs: bool = False) -> str:
    """Check health of a Docker service."""
    stats_result = subprocess.run(
        ["docker", "stats", "--no-stream", "--format",
         "{{.Name}}|{{.CPUPerc}}|{{.MemUsage}}|{{.NetIO}}", service_name],
        capture_output=True, text=True, timeout=10
    )
    
    inspect_result = subprocess.run(
        ["docker", "inspect", "--format", "{{.State.Status}}|{{.State.Health.Status}}", service_name],
        capture_output=True, text=True, timeout=10
    )
    
    output = {
        "service": service_name,
        "timestamp": datetime.utcnow().isoformat(),
        "stats": stats_result.stdout.strip() or "Not running",
        "state": inspect_result.stdout.strip() or "Unknown",
    }
    
    if include_logs:
        logs = subprocess.run(
            ["docker", "logs", "--tail", "10", service_name],
            capture_output=True, text=True, timeout=10
        )
        output["recent_logs"] = logs.stdout[-500:] or logs.stderr[-500:]
    
    return json.dumps(output, indent=2)


def scale_service_fn(service_name: str, replicas: int) -> str:
    """Scale a service (requires approval for scale-down)."""
    # In production: docker service scale or kubectl scale
    return json.dumps({
        "action": "scale",
        "service": service_name,
        "replicas": replicas,
        "status": "simulated — connect to Docker Swarm or K8s in production",
        "timestamp": datetime.utcnow().isoformat(),
    })


def query_metrics_fn(promql: str, prometheus_url: str = "http://prometheus:9090") -> str:
    """Execute a PromQL query against Prometheus."""
    import urllib.request
    import urllib.parse
    
    url = f"{prometheus_url}/api/v1/query?query={urllib.parse.quote(promql)}"
    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            data = json.loads(resp.read())
            return json.dumps(data.get("data", {}), indent=2)
    except Exception as e:
        return f"Prometheus query failed: {e}"


def run_safe_command_fn(command: str, timeout: int = 10) -> str:
    """Run a safe, read-only shell command."""
    # Allowlist of safe commands
    SAFE_PREFIXES = ("docker ps", "docker stats", "docker logs", "kubectl get",
                     "kubectl describe", "helm list", "git log", "git status",
                     "df -h", "free -m", "uptime", "cat /proc")
    
    cmd_lower = command.strip().lower()
    if not any(cmd_lower.startswith(prefix) for prefix in SAFE_PREFIXES):
        return f"BLOCKED: Command '{command}' is not in the safe command allowlist."
    
    result = subprocess.run(
        command, shell=False, capture_output=True, text=True,
        timeout=timeout, args=command.split()
    )
    return (result.stdout or result.stderr)[:2000]


def search_logs_fn(service_name: str, pattern: str, tail: int = 100) -> str:
    """Search service logs for a pattern."""
    logs = subprocess.run(
        ["docker", "logs", "--tail", str(tail), service_name],
        capture_output=True, text=True, timeout=15
    )
    all_logs = (logs.stdout + logs.stderr).splitlines()
    matches = [line for line in all_logs if pattern.lower() in line.lower()]
    return f"Found {len(matches)} matches for '{pattern}':\n" + "\n".join(matches[:20])


# ─────────────────────────────────────────────
# Tool Registry
# ─────────────────────────────────────────────
tools = [
    StructuredTool.from_function(
        func=check_service_health_fn,
        name="check_service_health",
        description="Check the health, stats, and optionally logs of a Docker service. Use this to investigate service issues.",
        args_schema=ServiceHealthInput,
    ),
    StructuredTool.from_function(
        func=scale_service_fn,
        name="scale_service",
        description="Scale a service to a target number of replicas. Only use after diagnosing the issue. Requires justification.",
        args_schema=ScaleServiceInput,
    ),
    StructuredTool.from_function(
        func=query_metrics_fn,
        name="query_prometheus",
        description="Execute a PromQL query to retrieve metrics. Use for CPU, memory, request rates, error rates, latency.",
        args_schema=QueryMetricsInput,
    ),
    StructuredTool.from_function(
        func=run_safe_command_fn,
        name="run_safe_command",
        description="Run a safe, read-only shell command from the allowlist (docker ps, kubectl get, git log, etc.)",
        args_schema=ShellCommandInput,
    ),
    StructuredTool.from_function(
        func=search_logs_fn,
        name="search_logs",
        description="Search the last N lines of a service's Docker logs for a pattern (error, timeout, exception, etc.)",
        args_schema=SearchLogsInput,
    ),
]

# ─────────────────────────────────────────────
# ReAct Prompt
# ─────────────────────────────────────────────
REACT_PROMPT = PromptTemplate.from_template("""You are an expert ops agent with access to production tools.
You think step-by-step (ReAct pattern): Thought → Action → Observation → repeat until done.

IMPORTANT RULES:
- Never run destructive commands
- Always investigate BEFORE taking action
- Explain your reasoning at each step
- If unsure, gather more information

Available tools:
{tools}

Tool names: {tool_names}

Format:
Question: the input task
Thought: what I need to do
Action: tool_name
Action Input: {{"param": "value"}}
Observation: tool result
... (repeat as needed)
Thought: I have enough information
Final Answer: structured summary of findings and actions taken

Question: {input}
Thought: {agent_scratchpad}""")

# ─────────────────────────────────────────────
# Agent
# ─────────────────────────────────────────────
agent = create_react_agent(llm=llm, tools=tools, prompt=REACT_PROMPT)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    max_iterations=10,
    handle_parsing_errors=True,
    return_intermediate_steps=True,
)


# ─────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────
if __name__ == "__main__":
    tasks = [
        "Check the health of the agentops-langserve service and identify any issues",
        "Query Prometheus for the error rate of the last 5 minutes and alert if > 1%",
        "Search logs of agentops-redis for any connection errors in the last 200 lines",
    ]

    for task in tasks:
        print(f"\n{'='*60}\nTask: {task}\n{'='*60}")
        try:
            result = agent_executor.invoke({"input": task})
            print(f"\nFinal Answer:\n{result['output']}")
        except Exception as e:
            print(f"Error: {e}")
