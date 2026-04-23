# AgentOps - AI Agent Operations

Production-grade multi-agent AI operations platform with **5 agentic frameworks**,
**100 domain-specific `.agent/` definitions**, and a fully enriched observability stack.

## Architecture

```
AgentOps/
├── agents/
│   ├── crewai/              # Role-based multi-agent teams
│   │   ├── ops_team.py      # DevOps operations crew (5 agents)
│   │   └── incident_response.py
│   ├── langgraph/           # Stateful cyclic agent workflows
│   │   ├── ops_workflow.py  # Health monitor + human-in-the-loop
│   │   └── supervisor_pattern.py
│   ├── autogen/             # Microsoft AutoGen conversational agents
│   │   ├── ops_group_chat.py
│   │   └── code_review_pipeline.py
│   ├── openagents/          # ReAct tool-augmented agent
│   │   └── ops_tool_agent.py
│   ├── agentscope/          # Alibaba AgentScope pipeline agents
│   │   └── ops_pipeline.py
│   ├── tools/               # Shared tool registry (all frameworks)
│   │   └── ops_tools.py
│   └── requirements.txt
├── .agent/                  # Agent definition for this domain
│   ├── agent.md · skills.md · capabilities.md · intents.md
│   ├── tools.md · workflows.md · config.yaml
│   └── prompts/ (system.md · examples.md)
├── docker-compose.yml
└── README.md
```

## Services

| Service | Port | Description |
|---------|------|-------------|
| LangServe | 8000 | Agent API server |
| LangGraph Server | 8001 | Stateful workflow API |
| AgentScope Server | 12001 | Distributed agent RPC |
| Ollama | 11434 | Local LLM (llama3, mistral, etc.) |
| Qdrant | 6333 | Vector store for RAG |
| Vault | 8200 | Secrets management |
| Langfuse | 3001 | Agent tracing & evaluation |
| Redis | 6379 | Agent memory/cache |
| PostgreSQL | 5432 | Agent state store |
| Temporal | 7233 | Workflow orchestration |
| Temporal UI | 8088 | Workflow dashboard |
| Prometheus | 9090 | Metrics |
| Grafana | 3000 | Dashboards |

## Quick Start

```bash
cd AgentOps
cp .env.example .env
docker compose up -d

# Pull a local LLM (no API key needed)
docker exec agentops-ollama ollama pull llama3

# Run CrewAI ops team
docker exec agentops-crewai python agents/crewai/ops_team.py

# Run LangGraph stateful workflow
docker exec agentops-langgraph python agents/langgraph/ops_workflow.py

# Run AutoGen group chat
docker exec agentops-autogen python agents/autogen/ops_group_chat.py
```

## Frameworks

| Framework | Pattern | Best For |
|-----------|---------|----------|
| **CrewAI** | Role-based teams | Structured ops tasks with delegation |
| **LangGraph** | State machine graphs | Cyclic, conditional, stateful workflows |
| **AutoGen** | Conversational multi-agent | Code generation, review, and debate |
| **OpenAgents** | ReAct tool-use | Rich tool ecosystems, streaming |
| **AgentScope** | Pipeline DAGs | Distributed, scalable agent pipelines |

## .agent/ Structure

Every `*Ops/` folder in this workspace contains a `.agent/` directory with:
`agent.md` · `skills.md` · `capabilities.md` · `intents.md` · `tools.md` · `workflows.md` · `config.yaml` · `prompts/system.md` · `prompts/examples.md`

Regenerate all with: `python scripts/generate_agent_structures.py`
