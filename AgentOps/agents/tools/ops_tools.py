"""
Shared Tool Registry for AgentOps
All agentic frameworks share these reusable tool definitions.
"""

import os
import json
import subprocess
import urllib.request
import urllib.parse
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


# ─────────────────────────────────────────────
# Docker Tools
# ─────────────────────────────────────────────
def docker_ps(filter_label: Optional[str] = None) -> list[dict]:
    """List running Docker containers with health status."""
    cmd = ["docker", "ps", "--format", "{{json .}}"]
    if filter_label:
        cmd += ["--filter", f"label={filter_label}"]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
    containers = []
    for line in result.stdout.strip().splitlines():
        try:
            containers.append(json.loads(line))
        except json.JSONDecodeError:
            pass
    return containers


def docker_logs(container: str, tail: int = 50, since: Optional[str] = None) -> str:
    """Retrieve Docker container logs safely."""
    cmd = ["docker", "logs", "--tail", str(tail)]
    if since:
        cmd += ["--since", since]
    cmd.append(container)
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
    return (result.stdout + result.stderr)[-4000:]  # limit output size


def docker_inspect(container: str) -> dict:
    """Inspect a Docker container's full configuration."""
    result = subprocess.run(
        ["docker", "inspect", container],
        capture_output=True, text=True, timeout=10
    )
    data = json.loads(result.stdout)
    return data[0] if data else {}


# ─────────────────────────────────────────────
# Prometheus Tools
# ─────────────────────────────────────────────
PROMETHEUS_URL = os.getenv("PROMETHEUS_URL", "http://prometheus:9090")


def query_prometheus(promql: str) -> dict:
    """Execute an instant PromQL query."""
    url = f"{PROMETHEUS_URL}/api/v1/query?query={urllib.parse.quote(promql)}"
    with urllib.request.urlopen(url, timeout=10) as resp:
        return json.loads(resp.read()).get("data", {})


def query_prometheus_range(promql: str, start: str, end: str, step: str = "1m") -> dict:
    """Execute a range PromQL query."""
    params = urllib.parse.urlencode({
        "query": promql, "start": start, "end": end, "step": step
    })
    url = f"{PROMETHEUS_URL}/api/v1/query_range?{params}"
    with urllib.request.urlopen(url, timeout=15) as resp:
        return json.loads(resp.read()).get("data", {})


def get_alert_rules() -> list[dict]:
    """Get all active Prometheus alert rules."""
    url = f"{PROMETHEUS_URL}/api/v1/rules"
    with urllib.request.urlopen(url, timeout=10) as resp:
        data = json.loads(resp.read())
        return data.get("data", {}).get("groups", [])


# ─────────────────────────────────────────────
# Temporal Workflow Tools
# ─────────────────────────────────────────────
TEMPORAL_HOST = os.getenv("TEMPORAL_HOST", "temporal:7233")


def list_workflows(namespace: str = "default", status: str = "RUNNING") -> list[dict]:
    """List Temporal workflows by status."""
    result = subprocess.run(
        ["temporal", "workflow", "list",
         "--namespace", namespace,
         "--query", f'ExecutionStatus="{status}"',
         "--address", TEMPORAL_HOST],
        capture_output=True, text=True, timeout=15
    )
    return [{"raw": line} for line in result.stdout.splitlines() if line.strip()]


def describe_workflow(workflow_id: str, namespace: str = "default") -> str:
    """Describe a specific Temporal workflow."""
    result = subprocess.run(
        ["temporal", "workflow", "describe",
         "--workflow-id", workflow_id,
         "--namespace", namespace,
         "--address", TEMPORAL_HOST],
        capture_output=True, text=True, timeout=10
    )
    return result.stdout or result.stderr


# ─────────────────────────────────────────────
# Redis Tools
# ─────────────────────────────────────────────
REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379")


def redis_info() -> dict:
    """Get Redis server info and memory usage."""
    import redis
    r = redis.from_url(REDIS_URL)
    info = r.info()
    return {
        "used_memory_human": info.get("used_memory_human"),
        "connected_clients": info.get("connected_clients"),
        "total_commands_processed": info.get("total_commands_processed"),
        "keyspace_hits": info.get("keyspace_hits"),
        "keyspace_misses": info.get("keyspace_misses"),
        "uptime_in_seconds": info.get("uptime_in_seconds"),
    }


def redis_keys_count(pattern: str = "*") -> int:
    """Count Redis keys matching a pattern."""
    import redis
    r = redis.from_url(REDIS_URL)
    return len(r.keys(pattern))


# ─────────────────────────────────────────────
# PostgreSQL Tools
# ─────────────────────────────────────────────
DB_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@postgres:5432/agentops")


def db_query(sql: str, params: Optional[tuple] = None) -> list[dict]:
    """Execute a safe, read-only SQL query with parameterized inputs."""
    # Only SELECT statements allowed here — no DDL/DML
    if not sql.strip().upper().startswith("SELECT"):
        raise ValueError("Only SELECT queries are allowed via this tool")
    
    import psycopg2
    import psycopg2.extras
    conn = psycopg2.connect(DB_URL)
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute(sql, params or ())
        rows = cur.fetchmany(100)  # cap at 100 rows
        return [dict(row) for row in rows]


def db_table_sizes() -> list[dict]:
    """Get table sizes in the database."""
    return db_query("""
        SELECT schemaname, tablename,
               pg_size_pretty(pg_total_relation_size(quote_ident(schemaname)||'.'||quote_ident(tablename))) AS size
        FROM pg_tables
        WHERE schemaname NOT IN ('pg_catalog', 'information_schema')
        ORDER BY pg_total_relation_size(quote_ident(schemaname)||'.'||quote_ident(tablename)) DESC
        LIMIT 20
    """)


# ─────────────────────────────────────────────
# Notification Tools
# ─────────────────────────────────────────────
def send_slack_alert(channel: str, message: str, severity: str = "info") -> dict:
    """Send a Slack alert via webhook."""
    webhook_url = os.getenv("SLACK_WEBHOOK_URL", "")
    if not webhook_url:
        return {"status": "skipped", "reason": "SLACK_WEBHOOK_URL not configured"}
    
    color_map = {"info": "#36a64f", "warning": "#f0a500", "critical": "#d00000"}
    payload = json.dumps({
        "channel": channel,
        "attachments": [{
            "color": color_map.get(severity, "#36a64f"),
            "text": message,
            "footer": f"AgentOps | {datetime.utcnow().isoformat()}",
        }]
    }).encode()
    
    req = urllib.request.Request(webhook_url, data=payload,
                                  headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=5) as resp:
        return {"status": "sent", "response": resp.read().decode()}


# ─────────────────────────────────────────────
# LangChain / CrewAI Tool Wrappers
# ─────────────────────────────────────────────
def get_langchain_tools():
    """Return all tools as LangChain StructuredTool instances."""
    from langchain_core.tools import StructuredTool

    return [
        StructuredTool.from_function(docker_ps, name="docker_ps",
            description="List all running Docker containers"),
        StructuredTool.from_function(docker_logs, name="docker_logs",
            description="Get logs from a Docker container"),
        StructuredTool.from_function(query_prometheus, name="query_prometheus",
            description="Execute a PromQL query against Prometheus"),
        StructuredTool.from_function(redis_info, name="redis_info",
            description="Get Redis server health and memory info"),
        StructuredTool.from_function(db_table_sizes, name="db_table_sizes",
            description="Get PostgreSQL table sizes"),
        StructuredTool.from_function(send_slack_alert, name="send_slack_alert",
            description="Send a Slack alert notification"),
    ]


def get_crewai_tools():
    """Return all tools as CrewAI BaseTool instances."""
    from crewai.tools import BaseTool

    class DockerPsTool(BaseTool):
        name: str = "docker_ps"
        description: str = "List running Docker containers"
        def _run(self, filter_label: str = "") -> str:
            return json.dumps(docker_ps(filter_label or None), indent=2)

    class PrometheusQueryTool(BaseTool):
        name: str = "query_prometheus"
        description: str = "Execute a PromQL query"
        def _run(self, promql: str) -> str:
            return json.dumps(query_prometheus(promql), indent=2)

    class SlackAlertTool(BaseTool):
        name: str = "send_slack_alert"
        description: str = "Send a Slack notification"
        def _run(self, message: str) -> str:
            return json.dumps(send_slack_alert("#ops-alerts", message, "info"))

    return [DockerPsTool(), PrometheusQueryTool(), SlackAlertTool()]
