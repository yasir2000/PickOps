# GitOps - Git-based Operations

GitOps workflow automation, continuous deployment, and infrastructure as code.

## 🎯 Overview

- GitOps engines (ArgoCD, Flux, Jenkins X)
- Git repository management (Gitea, GitLab)
- Policy enforcement (OPA, Kyverno)
- Secret management (Sealed Secrets)
- Progressive delivery (Flagger)
- Configuration drift detection

## 📦 Components

| Service | Port | Description |
|---------|------|-------------|
| ArgoCD | 8080 | Declarative GitOps |
| Flux | 8081 | GitOps toolkit |
| Gitea | 3000 | Git server |
| Tekton | 9097 | CI/CD pipelines |
| Kustomize | - | K8s customization |
| Sealed Secrets | - | Secret encryption |

## 🚀 Quick Start

```bash
cd GitOps
cp .env.example .env
./scripts/start.sh
```
