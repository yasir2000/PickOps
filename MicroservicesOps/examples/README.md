# MicroservicesOps Examples

Production-ready microservices implementations demonstrating service discovery, API gateway, messaging, and distributed tracing.

## Available Examples

### 1. [Spring Boot Microservice](./spring-boot-service/)
Complete Spring Boot service with:
- Eureka service registration
- Config server integration
- REST API endpoints
- Health checks and metrics
- Distributed tracing with Jaeger

**Technologies**: Spring Boot, Spring Cloud, Eureka, Zipkin

### 2. [Kong API Gateway](./kong-gateway/)
Advanced API gateway configuration:
- Route and service management
- Plugin ecosystem (auth, rate limiting, CORS)
- Load balancing strategies
- Request/response transformation
- API composition

**Technologies**: Kong, PostgreSQL, Lua plugins

### 3. [RabbitMQ Event System](./rabbitmq-events/)
Event-driven microservices:
- Publisher-subscriber pattern
- Work queues
- Topic exchanges
- Dead letter queues
- Message durability and acknowledgments

**Technologies**: RabbitMQ, Python/Node.js, AMQP

### 4. [Kafka Streaming](./kafka-streaming/)
Real-time event streaming:
- Producer and consumer groups
- Stream processing
- Exactly-once semantics
- Schema registry integration
- Event sourcing patterns

**Technologies**: Kafka, Kafka Streams, Avro, Python

### 5. [Service Mesh with Istio](./istio-mesh/)
Advanced service mesh features:
- Traffic management and routing
- Mutual TLS (mTLS)
- Circuit breaking and retries
- Observability integration
- Fault injection

**Technologies**: Istio, Envoy, Kiali, Prometheus

## Getting Started

1. **Start MicroservicesOps stack**:
```bash
cd MicroservicesOps
docker-compose up -d
```

2. **Choose an example**:
```bash
cd examples/spring-boot-service
```

3. **Follow example README** for specific setup instructions

## Common Patterns

### Service Registration (Consul)

```bash
# Register service
curl -X PUT http://localhost:8500/v1/agent/service/register \
  -d '{
    "ID": "user-service-1",
    "Name": "user-service",
    "Port": 8080,
    "Tags": ["v1", "production"],
    "Check": {
      "HTTP": "http://user-service:8080/health",
      "Interval": "10s"
    }
  }'

# Discover services
curl http://localhost:8500/v1/catalog/service/user-service
```

### API Gateway (Kong)

```bash
# Create service
curl -X POST http://localhost:8001/services \
  --data "name=user-api" \
  --data "url=http://user-service:8080"

# Add route
curl -X POST http://localhost:8001/services/user-api/routes \
  --data "paths[]=/users" \
  --data "methods[]=GET" \
  --data "methods[]=POST"

# Add rate limiting
curl -X POST http://localhost:8001/services/user-api/plugins \
  --data "name=rate-limiting" \
  --data "config.minute=100" \
  --data "config.policy=local"
```

### Messaging (RabbitMQ)

```python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel()

# Declare exchange and queue
channel.exchange_declare(exchange='events', exchange_type='topic')
channel.queue_declare(queue='user_events', durable=True)
channel.queue_bind(exchange='events', queue='user_events', 
                   routing_key='user.*')

# Publish
channel.basic_publish(
    exchange='events',
    routing_key='user.created',
    body='{"user_id": 123}',
    properties=pika.BasicProperties(delivery_mode=2)
)

# Consume
def callback(ch, method, properties, body):
    print(f"Received: {body}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue='user_events', on_message_callback=callback)
channel.start_consuming()
```

### Distributed Tracing (Jaeger)

```python
from jaeger_client import Config
from opentracing.ext import tags
import time

config = Config(
    config={
        'sampler': {'type': 'const', 'param': 1},
        'local_agent': {
            'reporting_host': 'localhost',
            'reporting_port': 6831,
        },
    },
    service_name='user-service',
)
tracer = config.initialize_tracer()

# Create parent span
with tracer.start_span('create_user') as span:
    span.set_tag(tags.HTTP_METHOD, 'POST')
    span.set_tag(tags.HTTP_URL, '/users')
    
    # Child span
    with tracer.start_span('validate_user', child_of=span) as child:
        time.sleep(0.1)
        child.set_tag('validation', 'email')
    
    # Another child span
    with tracer.start_span('save_user', child_of=span) as child:
        time.sleep(0.2)
        child.set_tag('database', 'postgres')
```

## Architecture Patterns

### 1. API Gateway Pattern
- Single entry point
- Authentication/Authorization
- Rate limiting
- Request routing
- Response aggregation

### 2. Service Discovery
- Dynamic registration
- Health checking
- Load balancing
- Failover

### 3. Circuit Breaker
- Prevent cascading failures
- Fast failure
- Automatic recovery
- Fallback responses

### 4. Event-Driven Architecture
- Asynchronous communication
- Event sourcing
- CQRS
- Saga pattern

### 5. Sidecar Pattern
- Service mesh
- Observability
- Security
- Traffic management

## Best Practices

### 1. Design
- Domain-driven design
- Bounded contexts
- Loose coupling
- High cohesion
- API versioning

### 2. Communication
- Synchronous: REST, gRPC for queries
- Asynchronous: Events for commands
- Idempotency
- Timeouts and retries

### 3. Data
- Database per service
- Event sourcing
- CQRS
- Eventual consistency
- Distributed transactions (Saga)

### 4. Observability
- Structured logging
- Distributed tracing
- Metrics collection
- Health endpoints
- Centralized monitoring

### 5. Resilience
- Circuit breakers
- Bulkheads
- Rate limiting
- Graceful degradation
- Chaos engineering

## Testing Strategies

### Unit Testing
- Test individual components
- Mock external dependencies
- Fast execution

### Integration Testing
- Test service interactions
- Use test containers
- Verify contracts

### End-to-End Testing
- Full system testing
- Production-like environment
- Critical user journeys

### Contract Testing
- Consumer-driven contracts
- Pact framework
- API compatibility

## Monitoring & Debugging

### Health Checks

```bash
# Service health
curl http://localhost:8080/health

# Gateway health
curl http://localhost:8001/status

# Message broker
curl -u admin:admin http://localhost:15672/api/health/checks/alarms
```

### Distributed Tracing

```bash
# View in Jaeger UI
open http://localhost:16686

# Search for traces
# Filter by service, operation, tags
```

### Metrics

```bash
# Query Prometheus
curl 'http://localhost:9090/api/v1/query?query=up'

# View in Grafana
open http://localhost:3000
```

## Prerequisites

- Docker and Docker Compose
- Basic understanding of microservices
- Familiarity with REST APIs
- Knowledge of messaging systems

## Resources

- [Microservices.io](https://microservices.io/)
- [12 Factor App](https://12factor.net/)
- [Building Microservices - Sam Newman](https://www.oreilly.com/library/view/building-microservices/9781491950340/)
- [Kong Documentation](https://docs.konghq.com/)
- [Spring Cloud](https://spring.io/projects/spring-cloud)
