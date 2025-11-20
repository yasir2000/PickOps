# FinOps - Financial Operations

Cloud cost optimization, budget management, and financial governance.

## 🎯 Overview

- Cloud cost monitoring (Kubecost, Infracost)
- Budget alerts and forecasting
- Resource optimization recommendations
- Chargeback/showback
- Cost allocation and tagging
- Spend analytics

## 📦 Components

| Service | Port | Description |
|---------|------|-------------|
| Kubecost | 9090 | K8s cost monitoring |
| Infracost | 8080 | IaC cost estimation |
| OpenCost | 9003 | Cost monitoring |
| Grafana | 3000 | Cost dashboards |
| PostgreSQL | 5432 | Cost database |
| Prometheus | 9090 | Metrics collection |

## 🚀 Quick Start

```bash
cd FinOps
cp .env.example .env
./scripts/start.sh
```
