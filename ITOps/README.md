# ITOps - IT Operations

Traditional IT infrastructure management and monitoring platform.

## 🎯 Overview

- Infrastructure monitoring (Zabbix, Nagios)
- Log management (ELK Stack)
- Configuration management (Ansible, Puppet)
- Service desk (OTRS)
- Asset management
- Network monitoring (LibreNMS)
- Backup management

## 📦 Components

| Service | Port | Description |
|---------|------|-------------|
| Zabbix | 80 | Infrastructure monitoring |
| Grafana | 3000 | Visualization |
| Elasticsearch | 9200 | Log storage |
| Kibana | 5601 | Log analysis |
| AWX | 8043 | Ansible automation |
| NetBox | 8000 | IPAM/DCIM |
| LibreNMS | 8080 | Network monitoring |

## 🚀 Quick Start

```bash
cd ITOps
cp .env.example .env
./scripts/start.sh
```
