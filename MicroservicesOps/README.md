# MicroservicesOps

Complete microservices architecture stack with API gateway, service discovery, distributed tracing, messaging, and observability.

## Overview

MicroservicesOps provides a production-ready infrastructure for building, deploying, and managing microservices-based applications. It includes all essential components for a robust microservices ecosystem.

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     API Gateway (Kong)                      │
│                   http://localhost:8000                     │
└────────────────────────┬────────────────────────────────────┘
                         │
         ┌───────────────┼───────────────┐
         │               │               │
    ┌────▼────┐    ┌────▼────┐    ┌────▼────┐
    │Service A│    │Service B│    │Service C│
    └────┬────┘    └────┬────┘    └────┬────┘
         │               │               │
         └───────────────┼───────────────┘
                         │
         ┌───────────────┼───────────────┐
         │               │               │
    ┌────▼────┐    ┌────▼────┐    ┌────▼────┐
    │ Consul  │    │RabbitMQ │    │  Redis  │
    │Discovery│    │Messaging│    │ Cache   │
    └─────────┘    └─────────┘    └─────────┘
         │               │               │
         └───────────────┼───────────────┘
                         │
              ┌──────────▼──────────┐
              │  Jaeger (Tracing)   │
              │  Prometheus (Metrics)│
              │  Grafana (Dashboards)│
              └─────────────────────┘
```

## Components

### API Gateway & Routing
- **Kong (8000-8004)**: Enterprise API gateway with plugins, rate limiting, authentication
- **HAProxy (8080, 9000)**: High-performance load balancer with stats dashboard

### Service Discovery & Registry
- **Consul (8500)**: Service discovery, health checking, KV store
- **Eureka (8761)**: Spring Cloud service registry

### Configuration Management
- **Spring Cloud Config (8888)**: Centralized configuration server
- **Consul KV**: Distributed configuration store

### Messaging & Events
- **RabbitMQ (5672, 15672)**: AMQP message broker with management UI
- **Kafka (9092, 29092)**: Event streaming platform
- **NATS (4222)**: Lightweight, high-performance messaging

### Distributed Tracing
- **Jaeger (16686)**: End-to-end distributed tracing
- **OpenTelemetry Collector (4317)**: Telemetry data collection

### Observability
- **Prometheus (9090)**: Metrics collection and alerting
- **Grafana (3000)**: Metrics visualization and dashboards

### Data Layer
- **PostgreSQL (5432)**: Relational database
- **Redis (6379)**: In-memory cache and session store

### Resilience
- **Hystrix Dashboard (9002)**: Circuit breaker monitoring
- **Istio Pilot (15010)**: Service mesh control plane

## Quick Start

### 1. Start All Services

```bash
cd MicroservicesOps
docker-compose up -d
```

### 2. Start Core Services Only

```bash
# API Gateway + Service Discovery + Messaging
docker-compose up -d kong consul rabbitmq postgres redis
```

### 3. Verify Services

```bash
# Check all services
docker-compose ps

# Check health
curl http://localhost:8001/status  # Kong
curl http://localhost:8500/v1/status/leader  # Consul
```

## Service Access

### API Gateway
- **Kong Proxy**: http://localhost:8000
- **Kong Admin API**: http://localhost:8001
- **Kong Manager**: http://localhost:8002

### Service Discovery
- **Consul UI**: http://localhost:8500
- **Eureka Dashboard**: http://localhost:8761

### Messaging
- **RabbitMQ Management**: http://localhost:15672 (admin/admin)
- **Kafka**: localhost:29092

### Observability
- **Jaeger UI**: http://localhost:16686
- **Prometheus**: http://localhost:9090
- **Grafana**: http://localhost:3000 (admin/admin)

### Load Balancer
- **HAProxy Stats**: http://localhost:9000

### Circuit Breaker
- **Hystrix Dashboard**: http://localhost:9002

## Usage Examples

### 1. Register Service with Consul

```bash
# Register a service
curl -X PUT http://localhost:8500/v1/agent/service/register \
  -d '{
    "ID": "my-service-1",
    "Name": "my-service",
    "Port": 8080,
    "Tags": ["v1"],
    "Check": {
      "HTTP": "http://my-service:8080/health",
      "Interval": "10s"
    }
  }'

# Query services
curl http://localhost:8500/v1/catalog/service/my-service
```

### 2. Configure Kong Route

```bash
# Create a service
curl -X POST http://localhost:8001/services \
  --data "name=my-api" \
  --data "url=http://my-service:8080"

# Add a route
curl -X POST http://localhost:8001/services/my-api/routes \
  --data "paths[]=/api" \
  --data "methods[]=GET"

# Test the route
curl http://localhost:8000/api
```

### 3. Add Kong Plugins

```bash
# Rate limiting
curl -X POST http://localhost:8001/services/my-api/plugins \
  --data "name=rate-limiting" \
  --data "config.minute=100"

# Authentication
curl -X POST http://localhost:8001/services/my-api/plugins \
  --data "name=key-auth"

# CORS
curl -X POST http://localhost:8001/services/my-api/plugins \
  --data "name=cors" \
  --data "config.origins=*"
```

### 4. Publish to RabbitMQ

```python
import pika

# Connect
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost', 5672, '/', 
    pika.PlainCredentials('admin', 'admin'))
)
channel = connection.channel()

# Declare queue
channel.queue_declare(queue='tasks', durable=True)

# Publish message
channel.basic_publish(
    exchange='',
    routing_key='tasks',
    body='Hello Microservices!',
    properties=pika.BasicProperties(delivery_mode=2)
)

connection.close()
```

### 5. Kafka Producer/Consumer

```python
from kafka import KafkaProducer, KafkaConsumer

# Producer
producer = KafkaProducer(bootstrap_servers='localhost:29092')
producer.send('events', b'Event data')
producer.flush()

# Consumer
consumer = KafkaConsumer(
    'events',
    bootstrap_servers='localhost:29092',
    auto_offset_reset='earliest'
)

for message in consumer:
    print(message.value)
```

### 6. Distributed Tracing with Jaeger

```python
from jaeger_client import Config

# Initialize tracer
config = Config(
    config={
        'sampler': {'type': 'const', 'param': 1},
        'local_agent': {
            'reporting_host': 'localhost',
            'reporting_port': 6831,
        },
    },
    service_name='my-service',
)
tracer = config.initialize_tracer()

# Create span
with tracer.start_span('operation-name') as span:
    span.set_tag('http.method', 'GET')
    # Your code here
```

### 7. Use Redis Cache

```python
import redis

# Connect
r = redis.Redis(host='localhost', port=6379, db=0)

# Set/Get
r.set('key', 'value')
value = r.get('key')

# Hash operations
r.hset('user:1', mapping={'name': 'John', 'age': 30})
user = r.hgetall('user:1')
```

### 8. OpenTelemetry Instrumentation

```python
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# Configure
trace.set_tracer_provider(TracerProvider())
otlp_exporter = OTLPSpanExporter(endpoint="localhost:4317", insecure=True)
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(otlp_exporter)
)

# Use
tracer = trace.get_tracer(__name__)
with tracer.start_as_current_span("my-operation"):
    # Your code
    pass
```

## Configuration

### Environment Variables

Create `.env` file:

```bash
# RabbitMQ
RABBITMQ_USER=admin
RABBITMQ_PASS=admin

# PostgreSQL
POSTGRES_USER=microservices
POSTGRES_PASS=microservices

# Grafana
GRAFANA_USER=admin
GRAFANA_PASS=admin

# Config Server
CONFIG_GIT_URI=https://github.com/your-org/config-repo
```

### HAProxy Configuration

Edit `configs/haproxy.cfg`:

```haproxy
global
    maxconn 4096

defaults
    mode http
    timeout connect 5s
    timeout client 50s
    timeout server 50s

frontend http-in
    bind *:8080
    default_backend services

backend services
    balance roundrobin
    server service1 service-1:8080 check
    server service2 service-2:8080 check
    server service3 service-3:8080 check

listen stats
    bind *:9000
    stats enable
    stats uri /
    stats refresh 10s
```

### Prometheus Configuration

Edit `configs/prometheus.yml`:

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'services'
    consul_sd_configs:
      - server: 'consul:8500'
    relabel_configs:
      - source_labels: [__meta_consul_service]
        target_label: service

  - job_name: 'rabbitmq'
    static_configs:
      - targets: ['rabbitmq:15692']

  - job_name: 'kong'
    static_configs:
      - targets: ['kong:8001']
```

### Grafana Datasources

Edit `configs/grafana-datasources.yml`:

```yaml
apiVersion: 1

datasources:
  - name: Prometheus
    type: prometheus
    access: proxy
    url: http://prometheus:9090
    isDefault: true

  - name: Jaeger
    type: jaeger
    access: proxy
    url: http://jaeger:16686
```

### OpenTelemetry Collector

Edit `configs/otel-collector-config.yml`:

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

exporters:
  jaeger:
    endpoint: jaeger:14250
    tls:
      insecure: true
  
  prometheus:
    endpoint: "0.0.0.0:8889"

processors:
  batch:

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [jaeger]
    metrics:
      receivers: [otlp]
      processors: [batch]
      exporters: [prometheus]
```

## Architecture Patterns

### 1. API Gateway Pattern
- Single entry point for all clients
- Request routing and composition
- Authentication and authorization
- Rate limiting and throttling

### 2. Service Discovery Pattern
- Dynamic service registration
- Health checking
- Load balancing
- Failover handling

### 3. Circuit Breaker Pattern
- Prevent cascading failures
- Graceful degradation
- Automatic recovery
- Fallback mechanisms

### 4. Event-Driven Pattern
- Asynchronous communication
- Event sourcing
- CQRS (Command Query Responsibility Segregation)
- Saga pattern for distributed transactions

### 5. Database per Service
- Service data isolation
- Independent scaling
- Technology diversity
- Eventual consistency

## Microservices Best Practices

### 1. Design Principles
- Single Responsibility
- Loose Coupling
- High Cohesion
- Autonomous Services
- Decentralized Governance

### 2. Communication
- Synchronous: REST, gRPC
- Asynchronous: Message Queues, Event Streams
- API Versioning
- Backward Compatibility

### 3. Data Management
- Database per Service
- Event Sourcing
- CQRS
- Distributed Transactions (Saga)

### 4. Observability
- Centralized Logging
- Distributed Tracing
- Metrics Collection
- Health Checks

### 5. Resilience
- Circuit Breakers
- Retries with Exponential Backoff
- Timeouts
- Bulkheads

## Monitoring & Troubleshooting

### Health Checks

```bash
# Check all services
docker-compose ps

# Kong health
curl http://localhost:8001/status

# Consul health
curl http://localhost:8500/v1/health/state/any

# RabbitMQ health
curl -u admin:admin http://localhost:15672/api/health/checks/alarms
```

### Logs

```bash
# View logs
docker-compose logs -f kong
docker-compose logs -f consul
docker-compose logs -f rabbitmq

# Tail specific service
docker-compose logs --tail=100 -f jaeger
```

### Metrics

```bash
# Prometheus metrics
curl http://localhost:9090/api/v1/query?query=up

# RabbitMQ metrics
curl -u admin:admin http://localhost:15672/api/overview

# Kong metrics
curl http://localhost:8001/metrics
```

## Resource Requirements

### Minimum
- **CPU**: 4 cores
- **RAM**: 8GB
- **Disk**: 20GB

### Recommended
- **CPU**: 8 cores
- **RAM**: 16GB
- **Disk**: 50GB

### Individual Service Requirements
- Kong: 512MB RAM
- Consul: 256MB RAM
- RabbitMQ: 512MB RAM
- Kafka + Zookeeper: 1GB RAM
- Jaeger: 512MB RAM
- Prometheus: 1GB RAM
- Grafana: 256MB RAM

## Scaling

### Horizontal Scaling

```bash
# Scale services
docker-compose up -d --scale service-a=3

# Scale Kafka brokers
docker-compose up -d --scale kafka=3
```

### Load Balancing

```bash
# Configure Kong load balancing
curl -X POST http://localhost:8001/upstreams \
  --data "name=my-upstream"

curl -X POST http://localhost:8001/upstreams/my-upstream/targets \
  --data "target=service-1:8080" \
  --data "weight=100"

curl -X POST http://localhost:8001/upstreams/my-upstream/targets \
  --data "target=service-2:8080" \
  --data "weight=100"
```

## Security

### API Gateway Security

```bash
# Enable HTTPS
curl -X POST http://localhost:8001/certificates \
  --form "cert=@cert.pem" \
  --form "key=@key.pem"

# JWT authentication
curl -X POST http://localhost:8001/plugins \
  --data "name=jwt"

# IP restriction
curl -X POST http://localhost:8001/plugins \
  --data "name=ip-restriction" \
  --data "config.allow=192.168.1.0/24"
```

### Service-to-Service Authentication

```bash
# mTLS with Consul Connect
consul connect ca get-config

# Service mesh with Istio
# Automatic mTLS between services
```

## Cleanup

```bash
# Stop all services
docker-compose down

# Remove volumes
docker-compose down -v

# Remove everything
docker-compose down -v --rmi all
```

## Examples

See the `examples/` directory for complete implementations:

1. **Spring Boot Microservice**: Service with Eureka registration
2. **Node.js API Gateway**: Custom gateway with Kong
3. **Python Event Consumer**: RabbitMQ/Kafka consumer
4. **gRPC Service**: Inter-service communication
5. **Saga Pattern**: Distributed transaction example

## References

- [Microservices.io](https://microservices.io/)
- [Kong Documentation](https://docs.konghq.com/)
- [Consul Documentation](https://www.consul.io/docs)
- [RabbitMQ Documentation](https://www.rabbitmq.com/documentation.html)
- [Kafka Documentation](https://kafka.apache.org/documentation/)
- [Jaeger Documentation](https://www.jaegertracing.io/docs/)
- [Spring Cloud](https://spring.io/projects/spring-cloud)

## License

See main repository LICENSE file.
