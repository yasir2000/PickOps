# SecOps - Security Operations

Production security monitoring, threat detection, and incident response platform.

## 🎯 Overview

- Security monitoring (Wazuh, OSSEC)
- Threat intelligence (MISP)
- Vulnerability scanning (OpenVAS, Trivy)
- Log analysis (ELK Stack)
- Incident response
- Security automation (TheHive, Cortex)

## 📦 Components

| Service | Port | Description |
|---------|------|-------------|
| Wazuh | 443 | Security monitoring |
| TheHive | 9000 | Incident response |
| MISP | 8080 | Threat intelligence |
| OpenVAS | 9392 | Vulnerability scanner |
| Elasticsearch | 9200 | Log storage |
| Kibana | 5601 | Visualization |

## 🚀 Quick Start

```bash
cd SecOps
cp .env.example .env
./scripts/start.sh
```
