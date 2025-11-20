# AzureOps - Azure Operations

Azure-specific tooling, automation, and management platform.

## 🎯 Overview

- Azure CLI and PowerShell tools
- Infrastructure as Code (Bicep, ARM Templates)
- Cost monitoring (Azure Cost Management)
- Security compliance (Azure Policy, Defender)
- Resource management and automation
- Multi-subscription governance

## 📦 Components

| Service | Port | Description |
|---------|------|-------------|
| Azurite | 10000 | Azure Storage emulator |
| Azure CLI | - | Azure management |
| Terraform | - | IaC provisioning |
| Azure DevOps Agent | - | CI/CD agent |
| Prometheus | 9090 | Metrics |
| Grafana | 3000 | Dashboards |

## 🚀 Quick Start

```bash
cd AzureOps
cp .env.example .env
./scripts/start.sh
```
