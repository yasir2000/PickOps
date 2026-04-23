"""
LangGraph - Multi-Agent Supervisor Pattern
Demonstrates: Supervisor agent routing tasks to specialist subagents
"""

from typing import TypedDict, Annotated, Sequence, Literal
from langgraph.graph import StateGraph, END, START
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import operator
import os

llm = ChatOllama(model=os.getenv("OLLAMA_MODEL", "llama3"), base_url="http://ollama:11434")

AGENTS = ["infra_agent", "security_agent", "database_agent", "monitoring_agent", "FINISH"]


class SupervisorState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]
    next: str


def make_specialist_agent(role: str, expertise: str):
    """Factory for specialist agents."""
    def agent_node(state: SupervisorState) -> SupervisorState:
        prompt = ChatPromptTemplate.from_messages([
            ("system", f"You are a {role} expert in {expertise}. Answer concisely and precisely."),
            MessagesPlaceholder(variable_name="messages"),
        ])
        chain = prompt | llm
        response = chain.invoke({"messages": state["messages"]})
        return {"messages": [HumanMessage(content=response.content, name=role)]}
    return agent_node


def supervisor_node(state: SupervisorState) -> SupervisorState:
    """Routes tasks to the most appropriate specialist."""
    options_str = ", ".join(AGENTS)
    supervisor_prompt = ChatPromptTemplate.from_messages([
        ("system", f"""You are an ops supervisor. Route user requests to the right specialist.
Specialists: {options_str}
- infra_agent: Docker, Kubernetes, networking, scaling
- security_agent: CVEs, secrets management, RBAC, compliance  
- database_agent: PostgreSQL, Redis, migrations, query optimization
- monitoring_agent: Prometheus, Grafana, alerting, SLOs
- FINISH: when the task is fully resolved

Respond with ONLY the agent name to route to next."""),
        MessagesPlaceholder(variable_name="messages"),
    ])
    chain = supervisor_prompt | llm
    response = chain.invoke({"messages": state["messages"]})
    next_agent = response.content.strip()
    if next_agent not in AGENTS:
        next_agent = "FINISH"
    return {"next": next_agent}


def build_supervisor_graph():
    graph = StateGraph(SupervisorState)

    graph.add_node("supervisor", supervisor_node)
    graph.add_node("infra_agent", make_specialist_agent("Infrastructure", "Docker, Kubernetes, cloud networking"))
    graph.add_node("security_agent", make_specialist_agent("Security", "DevSecOps, secrets, compliance, OWASP"))
    graph.add_node("database_agent", make_specialist_agent("Database", "PostgreSQL, Redis, query optimization"))
    graph.add_node("monitoring_agent", make_specialist_agent("Monitoring", "Prometheus, Grafana, alerting, SLOs"))

    graph.add_edge(START, "supervisor")

    for agent in AGENTS[:-1]:  # exclude FINISH
        graph.add_edge(agent, "supervisor")

    graph.add_conditional_edges(
        "supervisor",
        lambda s: s["next"],
        {a: a for a in AGENTS[:-1]} | {"FINISH": END},
    )

    return graph.compile()


if __name__ == "__main__":
    app = build_supervisor_graph()
    
    queries = [
        "How do I scale my agent-gateway service horizontally?",
        "What secrets management tool should I use for Kubernetes?",
        "My PostgreSQL queries are slow. How do I add indexes?",
        "Set up a Grafana alert for p99 latency > 2 seconds.",
    ]

    for query in queries:
        print(f"\n❓ Query: {query}")
        result = app.invoke({"messages": [HumanMessage(content=query)], "next": ""})
        last = result["messages"][-1]
        print(f"✅ {last.content[:300]}")
