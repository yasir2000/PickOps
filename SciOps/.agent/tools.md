# 🔭 Scientific Operations Agent — Tools

## Tool Inventory

| Tool | Status | Configuration |
|------|--------|---------------|
| Slurm API | Integrated | See config.yaml |
| Apache Airflow | Integrated | See config.yaml |
| MLflow | Integrated | See config.yaml |
| MinIO | Integrated | See config.yaml |
| PostgreSQL | Integrated | See config.yaml |
| Jupyter | Integrated | See config.yaml |
| FastAPI | Integrated | See config.yaml |

## Tool Integration Patterns

### Direct API Calls
Tools that expose REST/GraphQL APIs are called directly with authenticated clients.

### Message Queue Tools
Kafka-based tools use producer/consumer patterns for async processing.

### Database Tools
PostgreSQL and time-series databases are accessed via connection pools with
parameterized queries (no string interpolation — SQL injection safe).

### Sensor / IoT Tools
MQTT-based tools subscribe to topic hierarchies and push data to InfluxDB.

## Tool Authentication

All credentials are stored in **HashiCorp Vault** or environment variables.
Never hardcoded. Rotated on a schedule defined in `config.yaml`.

## Adding New Tools

1. Define tool in `agents/tools/` as a `BaseTool` subclass
2. Register in `config.yaml` under `tools:`
3. Add integration test in `tests/tools/`
4. Document here with status and config reference
