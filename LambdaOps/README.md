# LambdaOps - Serverless Operations

Serverless function management, development, and monitoring.

## 🎯 Overview

- Local Lambda development (LocalStack)
- Function deployment and versioning
- API Gateway management
- Event-driven architectures
- Cold start optimization
- Serverless monitoring

## 📦 Components

| Service | Port | Description |
|---------|------|-------------|
| LocalStack | 4566 | Local AWS services |
| OpenFaaS | 8080 | Function platform |
| Fission | 8888 | K8s serverless |
| Nuclio | 8070 | High-perf functions |
| Prometheus | 9090 | Metrics |
| Grafana | 3000 | Dashboards |

## 🚀 Quick Start

```bash
cd LambdaOps
cp .env.example .env
./scripts/start.sh
```
