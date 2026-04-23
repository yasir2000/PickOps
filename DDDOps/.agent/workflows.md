# 🗺️ Domain-Driven Design Operations Agent — Workflows

## Workflow Patterns

This agent supports **4 primary workflow patterns**.

### Context Mapping Session

```
trigger → context-mapping-session → [tool calls] → result → notify
```

- **Pattern**: Sequential with conditional branching
- **Trigger**: User intent or scheduled cron
- **Steps**: Plan → Execute → Validate → Report
- **On failure**: Retry with backoff → Escalate → Human-in-the-loop

### Event Storming Facilitation

```
trigger → event-storming-facilitation → [tool calls] → result → notify
```

- **Pattern**: Sequential with conditional branching
- **Trigger**: User intent or scheduled cron
- **Steps**: Plan → Execute → Validate → Report
- **On failure**: Retry with backoff → Escalate → Human-in-the-loop

### Model Versioning Pipeline

```
trigger → model-versioning-pipeline → [tool calls] → result → notify
```

- **Pattern**: Sequential with conditional branching
- **Trigger**: User intent or scheduled cron
- **Steps**: Plan → Execute → Validate → Report
- **On failure**: Retry with backoff → Escalate → Human-in-the-loop

### Language Consistency Check

```
trigger → language-consistency-check → [tool calls] → result → notify
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
