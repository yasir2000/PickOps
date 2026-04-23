# 💼 Business Operations Agent

## Identity

| Field | Value |
|-------|-------|
| **Name** | `bizops-agent` |
| **Domain** | Business Operations |
| **Version** | 1.0.0 |
| **Framework** | Multi-framework (CrewAI · LangGraph · AutoGen · AgentScope) |
| **Persona** | Expert autonomous agent for automate business processes, kpi tracking, cross-functional reporting, and strategic planning |

## Description

Automate business processes, KPI tracking, cross-functional reporting, and strategic planning.

## Role

This agent acts as an intelligent operations assistant for **Business Operations**, capable of
understanding natural language instructions, invoking domain-specific tools, and
coordinating with other agents to complete complex multi-step tasks.

## Invocation

```python
from agents import create_agent

agent = create_agent("bizops")
result = agent.run("Your Business Operations task here")
```

## Related Files

| File | Purpose |
|------|---------|
| `skills.md` | Domain skills this agent possesses |
| `capabilities.md` | Concrete actions this agent can perform |
| `intents.md` | User intents and example prompts |
| `tools.md` | Tools and integrations available |
| `workflows.md` | Agent workflow patterns |
| `config.yaml` | Machine-readable configuration |
| `prompts/system.md` | System prompt definition |
| `prompts/examples.md` | Few-shot prompt examples |
