# AppOps - Application Operations

Application lifecycle management, deployment automation, and runtime monitoring.

## 🎯 Overview

- Application deployment (Helm, Kustomize)
- Service mesh (Istio, Linkerd)
- Application monitoring (APM, tracing)
- Feature flags (Unleash, Flagsmith)
- A/B testing and canary deployments
- Application health checks

## 📦 Components

| Service | Port | Description |
|---------|------|-------------|
| Helm | - | Package manager |
| Telepresence | 8022 | Local development |
| Unleash | 4242 | Feature flags |
| Jaeger | 16686 | Distributed tracing |
| Envoy | 9901 | Service proxy |
| OpenTelemetry | 4317 | Observability |

## 🚀 Quick Start

```bash
cd AppOps
cp .env.example .env
./scripts/start.sh
```
