# DataOps - Data Operations

Production data pipeline, quality, and governance platform.

## 🎯 Overview

- Data ingestion (Apache NiFi, Airbyte)
- Data processing (Apache Spark, Flink)
- Data quality (Great Expectations)
- Data catalog (DataHub, Amundsen)
- Workflow orchestration (Apache Airflow)
- Data lineage and governance

## 📦 Components

| Service | Port | Description |
|---------|------|-------------|
| Airflow | 8080 | Workflow orchestration |
| NiFi | 8443 | Data ingestion |
| Spark | 8081 | Data processing |
| DataHub | 9002 | Data catalog |
| Airbyte | 8000 | Data integration |
| PostgreSQL | 5432 | Metadata store |

## 🚀 Quick Start

```bash
cd DataOps
cp .env.example .env
./scripts/start.sh
```
