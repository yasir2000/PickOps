# DevOps - Development Operations

Production-grade CI/CD and automation stack.

## 🎯 Overview

Complete DevOps platform with:
- CI/CD automation (Jenkins, GitLab CI)
- Container registry (Harbor)
- Artifact repository (Nexus)
- Code quality (SonarQube)
- Secret management (Vault)
- Monitoring (Prometheus, Grafana)

## 📦 Components

| Service | Port | Description |
|---------|------|-------------|
| Jenkins | 8080 | CI/CD automation |
| GitLab Runner | - | CI/CD executor |
| Harbor | 8082 | Container registry |
| Nexus | 8081 | Artifact repository |
| SonarQube | 9000 | Code quality |
| Vault | 8200 | Secret management |
| Grafana | 3000 | Monitoring |

## 🚀 Quick Start

```bash
cd DevOps
cp .env.example .env
./scripts/start.sh
```

## Access Points

- Jenkins: http://localhost:8080
- Harbor: http://localhost:8082 (admin/Harbor12345)
- Nexus: http://localhost:8081 (admin/admin123)
- SonarQube: http://localhost:9000 (admin/admin)
- Vault: http://localhost:8200
- Grafana: http://localhost:3000
