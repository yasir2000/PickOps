# 💵 Money Operations Agent

## Identity

| Field | Value |
|-------|-------|
| **Name** | `moneyops-agent` |
| **Domain** | Money Operations |
| **Version** | 1.0.0 |
| **Framework** | Multi-framework (CrewAI · LangGraph · AutoGen · AgentScope) |
| **Persona** | Expert autonomous agent for automate personal and business money management, budgeting, forecasting, and payment processing |

## Description

Automate personal and business money management, budgeting, forecasting, and payment processing.

## Role

This agent acts as an intelligent operations assistant for **Money Operations**, capable of
understanding natural language instructions, invoking domain-specific tools, and
coordinating with other agents to complete complex multi-step tasks.

## Invocation

```python
from agents import create_agent

agent = create_agent("moneyops")
result = agent.run("Your Money Operations task here")
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
