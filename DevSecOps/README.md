# DevSecOps - Development Security Operations

Secure SDLC with integrated security scanning and compliance.

## 🎯 Overview

- SAST/DAST scanning (SonarQube, OWASP ZAP)
- Dependency scanning (Snyk, Trivy)
- Secret detection (Gitleaks, TruffleHog)
- Container security (Anchore, Clair)
- Compliance as Code (InSpec, OpenSCAP)
- Security policy enforcement (OPA)

## 📦 Components

| Service | Port | Description |
|---------|------|-------------|
| SonarQube | 9000 | SAST analysis |
| OWASP ZAP | 8090 | DAST scanning |
| Trivy | 8081 | Vulnerability scanner |
| Anchore | 8228 | Container security |
| Vault | 8200 | Secret management |
| OPA | 8181 | Policy engine |

## 🚀 Quick Start

```bash
cd DevSecOps
cp .env.example .env
./scripts/start.sh
```
