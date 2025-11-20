# EventOps - Event-Driven Operations

Event streaming, processing, and event-driven architecture management.

## 🎯 Overview

- Event streaming (Kafka, Pulsar, NATS)
- Event processing (Flink, Spark Streaming)
- Schema registry (Confluent, Apicurio)
- Event replay and debugging
- Dead letter queues
- Event monitoring and analytics

## 📦 Components

| Service | Port | Description |
|---------|------|-------------|
| Kafka | 9092 | Event streaming |
| Pulsar | 6650 | Multi-tenant messaging |
| NATS | 4222 | Cloud-native messaging |
| Redpanda | 9092 | Kafka-compatible |
| Schema Registry | 8081 | Schema management |
| Kafka UI | 8080 | Web interface |

## 🚀 Quick Start

```bash
cd EventOps
cp .env.example .env
./scripts/start.sh
```
