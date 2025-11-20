# GitOps Examples

Real-world GitOps deployment patterns and workflows.

## Examples

1. [argocd-app-deployment](./argocd-app-deployment/) - Deploy app with ArgoCD
2. [flux-helm-release](./flux-helm-release/) - Helm chart deployment with Flux
3. [multi-env-promotion](./multi-env-promotion/) - Dev → Staging → Prod promotion
4. [sealed-secrets](./sealed-secrets/) - Encrypted secrets in Git
5. [progressive-delivery](./progressive-delivery/) - Canary deployments

## Quick Start

```bash
# Start GitOps stack
cd ../
docker-compose up -d

# Access ArgoCD
# http://localhost:8080
# admin / <get password from logs>
```
