# 🔬 Microservices Operations Agent — Tools

## Tool Inventory

| Tool | Status | Configuration |
|------|--------|---------------|
| Istio | Integrated | See config.yaml |
| Linkerd | Integrated | See config.yaml |
| Jaeger | Integrated | See config.yaml |
| Zipkin | Integrated | See config.yaml |
| Kong | Integrated | See config.yaml |
| Consul | Integrated | See config.yaml |
| Prometheus | Integrated | See config.yaml |
| Grafana | Integrated | See config.yaml |
| Chaos Monkey | Integrated | See config.yaml |

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
