# 🌏 Trade Operations Agent — Workflows

## Workflow Patterns

This agent supports **4 primary workflow patterns**.

### Customs Automation Pipeline

```
trigger → customs-automation-pipeline → [tool calls] → result → notify
```

- **Pattern**: Sequential with conditional branching
- **Trigger**: User intent or scheduled cron
- **Steps**: Plan → Execute → Validate → Report
- **On failure**: Retry with backoff → Escalate → Human-in-the-loop

### Trade Finance Workflow

```
trigger → trade-finance-workflow → [tool calls] → result → notify
```

- **Pattern**: Sequential with conditional branching
- **Trigger**: User intent or scheduled cron
- **Steps**: Plan → Execute → Validate → Report
- **On failure**: Retry with backoff → Escalate → Human-in-the-loop

### Sanctions Screening Loop

```
trigger → sanctions-screening-loop → [tool calls] → result → notify
```

- **Pattern**: Sequential with conditional branching
- **Trigger**: User intent or scheduled cron
- **Steps**: Plan → Execute → Validate → Report
- **On failure**: Retry with backoff → Escalate → Human-in-the-loop

### Tariff Calculation

```
trigger → tariff-calculation → [tool calls] → result → notify
```

- **Pattern**: Sequential with conditional branching
- **Trigger**: User intent or scheduled cron
- **Steps**: Plan → Execute → Validate → Report
- **On failure**: Retry with backoff → Escalate → Human-in-the-loop



## Workflow Design Principles

1. **Idempotency** — safe to retry without side effects
2. **Observability** — all steps emit structured logs and metrics
3. **Compensation** — failed workflows trigger rollback/cleanup
4. **Human-in-the-loop** — destructive actions require approval
5. **Timeout handling** — all steps have explicit timeouts

## Workflow Orchestration

Workflows are orchestrated via:
- **LangGraph** — for stateful, cyclic agent workflows
- **Temporal** — for long-running, durable workflows
- **Celery** — for distributed task queues
