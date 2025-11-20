# ArgoCD Application Deployment Example

Deploy and manage applications using GitOps principles with ArgoCD.

## What You'll Learn

- Deploy applications declaratively
- Automated sync from Git
- Self-healing deployments
- Multi-environment management
- Rollback strategies

## Prerequisites

```bash
# Start GitOps stack
cd ../../
docker-compose up -d argocd-server gitea

# Wait for ArgoCD to be ready
docker-compose logs -f argocd-server
```

## Get ArgoCD Password

```bash
# Get initial admin password
docker-compose exec argocd-server argocd admin initial-password
```

## Access ArgoCD UI

1. Open http://localhost:8080
2. Login: `admin` / `<password-from-above>`

## Deploy Application (UI Method)

### Step 1: Create Application

1. Click **+ New App**
2. Fill in details:
   - **Application Name**: guestbook
   - **Project**: default
   - **Sync Policy**: Automatic
   - **Repository URL**: https://github.com/argoproj/argocd-example-apps.git
   - **Path**: guestbook
   - **Cluster**: https://kubernetes.default.svc
   - **Namespace**: guestbook

3. Click **Create**

### Step 2: Sync Application

ArgoCD will automatically:
1. Detect resources in Git
2. Compare with cluster state
3. Sync resources to cluster
4. Monitor health status

## Deploy Application (CLI Method)

```bash
# Install ArgoCD CLI
curl -sSL -o argocd https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
chmod +x argocd
sudo mv argocd /usr/local/bin/

# Login
argocd login localhost:8080 --username admin --password <password> --insecure

# Create application
argocd app create guestbook \
  --repo https://github.com/argoproj/argocd-example-apps.git \
  --path guestbook \
  --dest-server https://kubernetes.default.svc \
  --dest-namespace guestbook \
  --sync-policy automated \
  --auto-prune \
  --self-heal

# View status
argocd app get guestbook

# Sync manually (if needed)
argocd app sync guestbook
```

## Deploy Application (Declarative Method)

```bash
# Apply the application manifest
kubectl apply -f application.yaml

# Watch status
kubectl get applications -n argocd -w
```

## Verify Deployment

```bash
# Check application status
argocd app get guestbook

# View resources
argocd app resources guestbook

# Check sync status
argocd app sync-status guestbook

# View application logs
argocd app logs guestbook
```

## GitOps Workflow Demo

### 1. Make a Change in Git

Fork the example repo and modify `guestbook/guestbook-ui-deployment.yaml`:

```yaml
spec:
  replicas: 3  # Change from 1 to 3
```

Commit and push.

### 2. Watch Auto-Sync

ArgoCD will:
1. Detect Git change (polling every 3 minutes)
2. Compare with cluster
3. Automatically sync
4. Scale deployment to 3 replicas

### 3. Manual Refresh (for immediate sync)

```bash
argocd app sync guestbook
```

## Self-Healing Demo

### 1. Manually Scale Deployment

```bash
kubectl scale deployment guestbook-ui -n guestbook --replicas=5
```

### 2. Watch ArgoCD Self-Heal

Within seconds, ArgoCD will:
1. Detect drift (5 replicas vs 3 in Git)
2. Automatically sync
3. Scale back to 3 replicas

## Rollback Example

### View History

```bash
argocd app history guestbook
```

### Rollback to Previous Version

```bash
# Get revision number from history
argocd app rollback guestbook <revision-number>
```

## Multi-Environment Setup

```yaml
# dev-application.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: guestbook-dev
spec:
  source:
    repoURL: https://github.com/yourorg/guestbook.git
    path: overlays/dev
  destination:
    namespace: guestbook-dev

---
# staging-application.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: guestbook-staging
spec:
  source:
    repoURL: https://github.com/yourorg/guestbook.git
    path: overlays/staging
  destination:
    namespace: guestbook-staging

---
# prod-application.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: guestbook-prod
spec:
  source:
    repoURL: https://github.com/yourorg/guestbook.git
    path: overlays/prod
  destination:
    namespace: guestbook-prod
  syncPolicy:
    automated: null  # Manual sync for production
```

## Monitoring

### ArgoCD UI
- Application health
- Sync status
- Resource tree view
- Events and logs

### Prometheus Metrics
http://localhost:9090

```promql
# Sync success rate
argocd_app_sync_total{phase="Succeeded"}

# Out-of-sync apps
argocd_app_info{sync_status="OutOfSync"}
```

### Grafana Dashboard
http://localhost:3000
- Pre-configured ArgoCD dashboard
- Sync metrics
- Health status

## Best Practices

1. **Use declarative configs**: Store Application manifests in Git
2. **Enable auto-sync**: For non-production environments
3. **Manual approval for prod**: Disable auto-sync for production
4. **Use projects**: Organize apps by team/product
5. **Health checks**: Define custom health assessments
6. **Prune carefully**: Test pruning in dev first

## Troubleshooting

**Application stuck in Progressing:**
```bash
argocd app get guestbook --show-operation
argocd app logs guestbook
```

**Sync fails:**
```bash
# Check sync status
argocd app sync-status guestbook

# Force sync
argocd app sync guestbook --force
```

**Out of sync but no changes:**
```bash
# Refresh app
argocd app diff guestbook

# Hard refresh
argocd app get guestbook --hard-refresh
```

## Next Steps

- Try [flux-helm-release](../flux-helm-release/) example
- Implement [multi-env-promotion](../multi-env-promotion/)
- Add [sealed-secrets](../sealed-secrets/) for secrets management
