# SagaOps - Saga Pattern Operations

Distributed transaction management, orchestration, and saga pattern implementation.

## 🎯 Overview

- Saga orchestration (Temporal, Camunda)
- Event sourcing (EventStore, Axon)
- Command/event processing
- Compensation and rollback
- State machine management
- Distributed transaction monitoring

## 📦 Components

| Service | Port | Description |
|---------|------|-------------|
| Temporal | 7233 | Workflow orchestration |
| Camunda | 8080 | Process automation |
| EventStore | 2113 | Event sourcing DB |
| Kafka | 9092 | Event streaming |
| Axon Server | 8024 | CQRS/ES platform |
| Debezium | 8083 | Change data capture |

## 🚀 Quick Start

```bash
cd SagaOps
cp .env.example .env
./scripts/start.sh
```
