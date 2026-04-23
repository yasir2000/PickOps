# AgentOps — Agents Directory

Comprehensive agentic AI implementations across multiple frameworks.

## Frameworks

| Folder | Framework | Best For |
|--------|-----------|----------|
| `crewai/` | CrewAI | Role-based multi-agent teams |
| `langgraph/` | LangGraph | Stateful, cyclic agent workflows |
| `autogen/` | AutoGen (Microsoft) | Conversational multi-agent systems |
| `openagents/` | OpenAgents | Open-source tool-augmented agents |
| `agentscope/` | AgentScope (Alibaba) | Distributed, scalable agent pipelines |
| `tools/` | Shared tools | Reusable tool definitions across frameworks |
| `configs/` | Agent configs | YAML-based agent & team configurations |

## Quick Start

```bash
# Install all frameworks
pip install -r requirements.txt

# Run CrewAI ops team
python agents/crewai/ops_team.py

# Run LangGraph workflow
python agents/langgraph/ops_workflow.py

# Run AutoGen debate
python agents/autogen/ops_debate.py
```
