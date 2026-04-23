"""
LangGraph - Stateful Ops Workflow Agent
Demonstrates: Cyclic agent graph with conditional routing, human-in-the-loop,
              persistent state, and tool nodes for ops automation
"""

from typing import TypedDict, Annotated, Sequence, Literal
from langgraph.graph import StateGraph, END, START
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import ToolNode
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage
from langchain_core.tools import tool
from langchain_community.llms import Ollama
from langchain_openai import ChatOpenAI
import operator
import os
import json
import subprocess
from datetime import datetime

# ─────────────────────────────────────────────
# LLM Setup
# ─────────────────────────────────────────────
USE_LOCAL = os.getenv("USE_LOCAL_LLM", "true").lower() == "true"
if USE_LOCAL:
    from langchain_community.chat_models import ChatOllama
    llm = ChatOllama(model=os.getenv("OLLAMA_MODEL", "llama3"), base_url="http://ollama:11434")
else:
    llm = ChatOpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))


# ─────────────────────────────────────────────
# Tool Definitions
# ─────────────────────────────────────────────
@tool
def check_service_health(service_name: str) -> dict:
    """Check the health of a deployed service by name."""
    import random
    status = random.choice(["healthy", "healthy", "healthy", "degraded", "unhealthy"])
    return {
        "service": service_name,
        "status": status,
        "uptime_seconds": random.randint(60, 86400),
        "last_restart": datetime.utcnow().isoformat(),
    }


@tool
def scale_service(service_name: str, replicas: int) -> str:
    """Scale a Docker Compose / Kubernetes service to the specified number of replicas."""
    # In production: kubectl scale or docker service scale
    return f"Scaled '{service_name}' to {replicas} replica(s) successfully."


@tool
def rollback_service(service_name: str, version: str) -> str:
    """Roll back a service to a previous version."""
    return f"Rolled back '{service_name}' to version '{version}' successfully."


@tool
def query_logs(service_name: str, tail: int = 50) -> str:
    """Retrieve the last N log lines from a service."""
    result = subprocess.run(
        ["docker", "logs", "--tail", str(tail), service_name],
        capture_output=True, text=True
    )
    return result.stdout or result.stderr or f"No logs found for {service_name}"


@tool
def run_health_checks(environment: str) -> dict:
    """Run full health checks across all services in an environment."""
    services = ["agent-gateway", "langserve", "redis", "postgres", "temporal"]
    import random
    return {
        svc: random.choice(["healthy", "healthy", "degraded"])
        for svc in services
    }


tools = [check_service_health, scale_service, rollback_service, query_logs, run_health_checks]
tool_node = ToolNode(tools)
llm_with_tools = llm.bind_tools(tools)


# ─────────────────────────────────────────────
# State Schema
# ─────────────────────────────────────────────
class OpsState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]
    current_task: str
    environment: str
    health_report: dict
    requires_human_approval: bool
    loop_count: int


# ─────────────────────────────────────────────
# Graph Nodes
# ─────────────────────────────────────────────
def ops_agent(state: OpsState) -> OpsState:
    """Main ops agent: reasons about current task and calls tools."""
    system_prompt = f"""You are an autonomous ops agent managing the '{state['environment']}' environment.
Current task: {state['current_task']}
Loop iteration: {state['loop_count']}

Use your tools to investigate and resolve the task. When you have a complete picture,
summarize findings. If a destructive action (scale down, rollback) is needed, set
requires_human_approval to true in your final message by including [NEEDS_APPROVAL].
"""
    messages = [HumanMessage(content=system_prompt)] + list(state["messages"])
    response = llm_with_tools.invoke(messages)
    
    requires_approval = "[NEEDS_APPROVAL]" in (response.content or "")
    
    return {
        "messages": [response],
        "requires_human_approval": requires_approval,
        "loop_count": state["loop_count"] + 1,
    }


def health_monitor(state: OpsState) -> OpsState:
    """Runs initial health checks and populates health_report."""
    result = run_health_checks.invoke({"environment": state["environment"]})
    degraded = [svc for svc, status in result.items() if status != "healthy"]
    
    summary = f"Health check complete. Degraded services: {degraded or 'none'}"
    return {
        "messages": [HumanMessage(content=summary)],
        "health_report": result,
        "current_task": f"Investigate and fix degraded services: {degraded}" if degraded else "All services healthy",
    }


def human_approval_gate(state: OpsState) -> OpsState:
    """Pause for human approval — in production integrates with Slack/PagerDuty."""
    last_msg = state["messages"][-1]
    print(f"\n⚠️  HUMAN APPROVAL REQUIRED\n{last_msg.content}\n")
    approval = input("Approve action? (yes/no): ").strip().lower()
    if approval == "yes":
        return {"messages": [HumanMessage(content="Human approved the action. Proceed.")], "requires_human_approval": False}
    return {"messages": [HumanMessage(content="Human rejected the action. Abort.")], "requires_human_approval": False}


def summarize_results(state: OpsState) -> OpsState:
    """Final node: summarizes all actions taken."""
    summary_prompt = "Summarize all actions taken, their outcomes, and any open follow-up items."
    response = llm_with_tools.invoke(list(state["messages"]) + [HumanMessage(content=summary_prompt)])
    return {"messages": [response]}


# ─────────────────────────────────────────────
# Routing Functions
# ─────────────────────────────────────────────
def should_use_tools(state: OpsState) -> Literal["tools", "human_gate", "summarize", "agent"]:
    last = state["messages"][-1]
    if state.get("requires_human_approval"):
        return "human_gate"
    if hasattr(last, "tool_calls") and last.tool_calls:
        return "tools"
    if state["loop_count"] >= 5:
        return "summarize"
    return "agent"


def after_tools(state: OpsState) -> Literal["agent", "summarize"]:
    if state["loop_count"] >= 5:
        return "summarize"
    return "agent"


# ─────────────────────────────────────────────
# Build Graph
# ─────────────────────────────────────────────
def build_ops_graph() -> StateGraph:
    graph = StateGraph(OpsState)

    graph.add_node("health_monitor", health_monitor)
    graph.add_node("agent", ops_agent)
    graph.add_node("tools", tool_node)
    graph.add_node("human_gate", human_approval_gate)
    graph.add_node("summarize", summarize_results)

    graph.add_edge(START, "health_monitor")
    graph.add_edge("health_monitor", "agent")
    
    graph.add_conditional_edges("agent", should_use_tools, {
        "tools": "tools",
        "human_gate": "human_gate",
        "summarize": "summarize",
        "agent": "agent",
    })
    
    graph.add_conditional_edges("tools", after_tools, {
        "agent": "agent",
        "summarize": "summarize",
    })
    
    graph.add_edge("human_gate", "agent")
    graph.add_edge("summarize", END)

    return graph


# ─────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────
if __name__ == "__main__":
    checkpointer = MemorySaver()
    graph = build_ops_graph().compile(checkpointer=checkpointer)

    initial_state: OpsState = {
        "messages": [],
        "current_task": "Monitor and maintain all services in the production environment",
        "environment": os.getenv("OPS_ENVIRONMENT", "production"),
        "health_report": {},
        "requires_human_approval": False,
        "loop_count": 0,
    }

    config = {"configurable": {"thread_id": "ops-session-001"}}

    print("🔁 Starting LangGraph Ops Workflow...\n")
    for event in graph.stream(initial_state, config=config, stream_mode="values"):
        last_msg = event["messages"][-1] if event.get("messages") else None
        if last_msg:
            print(f"[{type(last_msg).__name__}] {str(last_msg.content)[:200]}")

    print("\n✅ Workflow complete.")
