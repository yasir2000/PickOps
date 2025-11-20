# AWSOps - AWS Operations

AWS-specific tooling, automation, and management platform.

## 🎯 Overview

- AWS CLI and SDK tools
- Infrastructure as Code (CloudFormation, CDK)
- Cost monitoring (AWS Cost Explorer integration)
- Security compliance (AWS Config, Security Hub)
- Resource management and automation
- Multi-account governance

## 📦 Components

| Service | Port | Description |
|---------|------|-------------|
| LocalStack | 4566 | AWS local development |
| Terraform | - | IaC provisioning |
| CloudWatch Exporter | 9106 | Metrics export |
| AWS Vault | - | Credential management |
| Steampipe | 9193 | AWS querying |
| Prowler | - | Security scanning |

## 🚀 Quick Start

```bash
cd AWSOps
cp .env.example .env
./scripts/start.sh
```
