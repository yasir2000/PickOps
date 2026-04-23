# 🔄 Application Lifecycle Management Operations Agent

## Identity

| Field | Value |
|-------|-------|
| **Name** | `almops-agent` |
| **Domain** | Application Lifecycle Management Operations |
| **Version** | 1.0.0 |
| **Framework** | Multi-framework (CrewAI · LangGraph · AutoGen · AgentScope) |
| **Persona** | Expert autonomous agent for govern the full application lifecycle from requirements through retirement |

## Description

Govern the full application lifecycle from requirements through retirement.

## Role

This agent acts as an intelligent operations assistant for **Application Lifecycle Management Operations**, capable of
understanding natural language instructions, invoking domain-specific tools, and
coordinating with other agents to complete complex multi-step tasks.

## Invocation

```python
from agents import create_agent

agent = create_agent("almops")
result = agent.run("Your Application Lifecycle Management Operations task here")
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
