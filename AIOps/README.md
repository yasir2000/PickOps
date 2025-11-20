# AIOps - AI for IT Operations

AI-powered IT operations, anomaly detection, and predictive maintenance.

## 🎯 Overview

- Log anomaly detection
- Metric forecasting and alerting
- Root cause analysis
- Automated incident response
- Capacity planning
- Performance optimization

## 📦 Components

| Service | Port | Description |
|---------|------|-------------|
| Prometheus | 9090 | Metrics collection |
| Grafana | 3000 | Visualization |
| Loki | 3100 | Log aggregation |
| Mimir | 9009 | Long-term metrics |
| Elastic | 9200 | Log analytics |
| Prophet Server | 5000 | Time series forecasting |

## 🚀 Quick Start

```bash
cd AIOps
cp .env.example .env
./scripts/start.sh
```
