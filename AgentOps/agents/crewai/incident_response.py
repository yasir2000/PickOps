"""
CrewAI - Incident Response Team
Demonstrates: Reactive multi-agent incident management with tools
Agents: Detector, Analyst, Responder, Communicator
"""

from crewai import Agent, Task, Crew, Process
from crewai.tools import BaseTool
from langchain_community.llms import Ollama
from datetime import datetime
import os
import json

llm = Ollama(model=os.getenv("OLLAMA_MODEL", "llama3"), base_url="http://ollama:11434")


class MetricsFetchTool(BaseTool):
    name: str = "fetch_metrics"
    description: str = "Fetch current system metrics (CPU, memory, error rate) for a service"

    def _run(self, service: str) -> str:
        import random
        # In production: query Prometheus/Grafana API
        metrics = {
            "service": service,
            "cpu_pct": round(random.uniform(60, 99), 1),
            "memory_pct": round(random.uniform(50, 95), 1),
            "error_rate_pct": round(random.uniform(0, 30), 2),
            "latency_p99_ms": round(random.uniform(100, 5000), 0),
            "timestamp": datetime.utcnow().isoformat(),
        }
        return json.dumps(metrics, indent=2)


class LogSearchTool(BaseTool):
    name: str = "search_logs"
    description: str = "Search application logs for error patterns in the last N minutes"

    def _run(self, query: str) -> str:
        # In production: query Loki/Elasticsearch
        return (
            f"[SIMULATED] Log search for '{query}':\n"
            "  ERROR 2026-04-24 10:32:11 - Connection pool exhausted\n"
            "  ERROR 2026-04-24 10:32:15 - Timeout after 30s waiting for DB\n"
            "  WARN  2026-04-24 10:32:20 - Retry attempt 3/3 failed\n"
        )


class RunbookTool(BaseTool):
    name: str = "get_runbook"
    description: str = "Retrieve the operational runbook for a given incident type"

    def _run(self, incident_type: str) -> str:
        runbooks = {
            "high_cpu": "1. Check top processes\n2. Scale horizontally\n3. Profile hot paths",
            "db_connection": "1. Check pool size\n2. Restart connection pool\n3. Increase max_connections",
            "memory_leak": "1. Capture heap dump\n2. Restart pod\n3. File bug with heap diff",
            "high_error_rate": "1. Check recent deployments\n2. Review logs\n3. Consider rollback",
        }
        return runbooks.get(incident_type, f"No runbook found for: {incident_type}")


# ─────────────────────────────────────────────
# Incident Response Agents
# ─────────────────────────────────────────────
detector = Agent(
    role="Incident Detector",
    goal="Identify and classify active incidents from metrics and logs",
    backstory="You monitor system health 24/7 and quickly classify incidents by severity.",
    llm=llm,
    tools=[MetricsFetchTool(), LogSearchTool()],
    verbose=True,
)

analyst = Agent(
    role="Root Cause Analyst",
    goal="Determine the root cause of incidents through systematic investigation",
    backstory=(
        "You are an expert in distributed systems and use structured "
        "debugging methodologies to trace issues to their origin."
    ),
    llm=llm,
    tools=[LogSearchTool(), RunbookTool()],
    verbose=True,
)

responder = Agent(
    role="Incident Responder",
    goal="Execute remediation actions to resolve incidents quickly",
    backstory="You execute runbooks and automated fixes to resolve incidents within SLA.",
    llm=llm,
    tools=[RunbookTool(), MetricsFetchTool()],
    verbose=True,
)

communicator = Agent(
    role="Incident Communicator",
    goal="Draft clear incident reports and stakeholder communications",
    backstory="You write precise, calm incident reports for engineering teams and stakeholders.",
    llm=llm,
    verbose=True,
)

# ─────────────────────────────────────────────
# Tasks
# ─────────────────────────────────────────────
INCIDENT_SERVICE = os.getenv("INCIDENT_SERVICE", "agent-gateway")

detect_task = Task(
    description=f"Fetch current metrics for '{INCIDENT_SERVICE}' and classify any active incidents by severity (P0-P3).",
    expected_output="Incident severity classification with supporting metrics",
    agent=detector,
)

analyse_task = Task(
    description="Perform root cause analysis on the detected incident using logs and runbooks.",
    expected_output="Root cause hypothesis with evidence from logs",
    agent=analyst,
    context=[detect_task],
)

respond_task = Task(
    description="Execute the appropriate runbook steps to remediate the incident.",
    expected_output="List of remediation actions taken and their outcomes",
    agent=responder,
    context=[analyse_task],
)

communicate_task = Task(
    description=(
        "Write an incident report including: timeline, root cause, impact, "
        "remediation steps taken, and prevention recommendations."
    ),
    expected_output="Complete incident report in markdown format",
    agent=communicator,
    context=[detect_task, analyse_task, respond_task],
)

# ─────────────────────────────────────────────
# Crew
# ─────────────────────────────────────────────
incident_crew = Crew(
    agents=[detector, analyst, responder, communicator],
    tasks=[detect_task, analyse_task, respond_task, communicate_task],
    process=Process.sequential,
    verbose=True,
)

if __name__ == "__main__":
    print(f"🚨 Starting Incident Response for service: {INCIDENT_SERVICE}\n")
    result = incident_crew.kickoff()
    print("\n📋 Incident Report:\n")
    print(result)
