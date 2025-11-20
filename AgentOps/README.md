# AgentOps - AI Agent Operations

Production-grade AI agent orchestration and monitoring.

## 🎯 Overview

- Agent orchestration (LangGraph, AutoGen)
- Multi-agent systems
- Agent monitoring and observability
- Tool integration
- Memory management
- Agent evaluation

## 📦 Components

| Service | Port | Description |
|---------|------|-------------|
| LangServe | 8000 | Agent API server |
| Redis | 6379 | Agent memory/cache |
| PostgreSQL | 5432 | Agent state store |
| Temporal | 7233 | Workflow orchestration |
| LangSmith | 1984 | Agent monitoring |

## 🚀 Quick Start

```bash
cd AgentOps
cp .env.example .env
./scripts/start.sh
```
