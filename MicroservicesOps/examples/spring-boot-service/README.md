# Spring Boot Microservice Example

Production-ready microservice with service discovery, health checks, REST API, and distributed tracing.

## Features

- **Service Registration**: Automatic registration with Consul and Eureka
- **Health Checks**: Liveness and readiness probes
- **REST API**: Complete CRUD operations for user management
- **Service Discovery**: Dynamic service discovery and communication
- **Metrics**: Prometheus-compatible metrics endpoint
- **Event Publishing**: Event-driven architecture with message brokers
- **Distributed Tracing**: Integration with Jaeger

## Quick Start

### 1. Start MicroservicesOps Stack

```bash
cd ../../
docker-compose up -d consul eureka jaeger rabbitmq
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Service

```bash
python service.py
```

The service will:
- Start on http://localhost:8080
- Register with Consul (http://localhost:8500)
- Register with Eureka (http://localhost:8761)
- Enable distributed tracing with Jaeger

## API Endpoints

### Health & Info

```bash
# Health check
curl http://localhost:8080/health

# Service info
curl http://localhost:8080/info

# Prometheus metrics
curl http://localhost:8080/metrics
```

### User Management

```bash
# Create user
curl -X POST http://localhost:8080/users \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com"}'

# Get all users
curl http://localhost:8080/users

# Get specific user
curl http://localhost:8080/users/1

# Update user
curl -X PUT http://localhost:8080/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Jane Doe", "email": "jane@example.com"}'

# Delete user
curl -X DELETE http://localhost:8080/users/1
```

### Service-to-Service Communication

```bash
# Call another service through Consul discovery
curl http://localhost:8080/service-to-service/example
```

## Service Discovery

### Consul Registration

The service automatically registers with Consul on startup:

```json
{
  "ID": "user-service-hostname-8080",
  "Name": "user-service",
  "Tags": ["1.0.0", "microservice"],
  "Address": "hostname",
  "Port": 8080,
  "Check": {
    "HTTP": "http://hostname:8080/health",
    "Interval": "10s",
    "Timeout": "5s"
  },
  "Meta": {
    "version": "1.0.0",
    "environment": "development"
  }
}
```

Verify registration:
```bash
# Check Consul UI
open http://localhost:8500

# Query via API
curl http://localhost:8500/v1/catalog/service/user-service
```

### Eureka Registration

The service also registers with Eureka:

```json
{
  "instance": {
    "instanceId": "hostname:user-service:8080",
    "hostName": "hostname",
    "app": "USER-SERVICE",
    "status": "UP",
    "port": {
      "$": 8080,
      "@enabled": "true"
    },
    "healthCheckUrl": "http://hostname:8080/health"
  }
}
```

Verify registration:
```bash
# Check Eureka UI
open http://localhost:8761

# Query via API
curl http://localhost:8761/eureka/apps/USER-SERVICE
```

## Health Checks

### Liveness Check

```bash
curl http://localhost:8080/health
```

Response:
```json
{
  "status": "UP",
  "service": "user-service",
  "version": "1.0.0",
  "timestamp": "2024-01-15T10:30:00.000Z",
  "checks": {
    "database": "UP",
    "cache": "UP",
    "messaging": "UP"
  }
}
```

### Readiness Check

The health endpoint serves both liveness and readiness:
- **Liveness**: Service is running
- **Readiness**: Service is ready to accept traffic

## Metrics

### Prometheus Format

```bash
curl http://localhost:8080/metrics
```

Response:
```
# HELP user_service_requests_total Total requests
# TYPE user_service_requests_total counter
user_service_requests_total{service="user-service",version="1.0.0"} 42

# HELP user_service_users_total Total users
# TYPE user_service_users_total gauge
user_service_users_total{service="user-service"} 10

# HELP user_service_up Service up status
# TYPE user_service_up gauge
user_service_up{service="user-service"} 1
```

### Integration with Prometheus

Add to MicroservicesOps `configs/prometheus.yml`:

```yaml
scrape_configs:
  - job_name: 'user-service'
    consul_sd_configs:
      - server: 'consul:8500'
        services: ['user-service']
    relabel_configs:
      - source_labels: [__meta_consul_service]
        target_label: service
```

View metrics in Grafana:
```bash
open http://localhost:3000
```

## Distributed Tracing

### Jaeger Integration

The service automatically sends traces to Jaeger:

```python
from jaeger_client import Config

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
```

### View Traces

```bash
# Open Jaeger UI
open http://localhost:16686

# Search for user-service traces
# View trace details, spans, and timing
```

### Trace Example

```
Trace: Create User Request
├─ Span: POST /users (200ms)
   ├─ Span: validate_user (50ms)
   ├─ Span: save_to_database (100ms)
   └─ Span: publish_event (50ms)
```

## Event Publishing

### Message Events

The service publishes events for:
- `user.created`: When a user is created
- `user.updated`: When a user is updated
- `user.deleted`: When a user is deleted

Event format:
```json
{
  "type": "user.created",
  "service": "user-service",
  "timestamp": "2024-01-15T10:30:00.000Z",
  "data": {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "created_at": "2024-01-15T10:30:00.000Z",
    "version": "1.0.0"
  }
}
```

### RabbitMQ Integration

To actually publish to RabbitMQ, install `pika`:

```bash
pip install pika
```

Update `publish_event` function:

```python
import pika

def publish_event(event_type: str, data: dict):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost', 5672, '/',
        pika.PlainCredentials('admin', 'admin'))
    )
    channel = connection.channel()
    
    channel.exchange_declare(exchange='events', exchange_type='topic')
    
    event = {
        'type': event_type,
        'service': SERVICE_NAME,
        'timestamp': datetime.utcnow().isoformat(),
        'data': data
    }
    
    channel.basic_publish(
        exchange='events',
        routing_key=event_type,
        body=json.dumps(event),
        properties=pika.BasicProperties(delivery_mode=2)
    )
    
    connection.close()
```

## Service-to-Service Communication

### Discovery Pattern

```python
# Discover service from Consul
response = requests.get(
    "http://localhost:8500/v1/catalog/service/order-service"
)

services = response.json()
if services:
    service = services[0]
    service_url = f"http://{service['ServiceAddress']}:{service['ServicePort']}"
    
    # Call the service
    orders = requests.get(f"{service_url}/orders")
```

### Load Balancing

Consul returns all healthy instances. Implement client-side load balancing:

```python
import random

def get_service_instance(service_name):
    response = requests.get(
        f"http://localhost:8500/v1/health/service/{service_name}?passing"
    )
    
    instances = response.json()
    if instances:
        # Random selection
        instance = random.choice(instances)
        service = instance['Service']
        return f"http://{service['Address']}:{service['Port']}"
    
    raise Exception(f"No healthy instances of {service_name}")
```

## Configuration

### Environment Variables

```bash
# Service configuration
export SERVICE_NAME=user-service
export SERVICE_PORT=8080
export SERVICE_VERSION=1.0.0

# Service discovery
export CONSUL_HOST=localhost:8500
export EUREKA_HOST=localhost:8761

# Distributed tracing
export JAEGER_HOST=localhost
export JAEGER_PORT=6831

# Run service
python service.py
```

### Multiple Instances

Run multiple instances for load balancing:

```bash
# Instance 1
SERVICE_PORT=8081 python service.py &

# Instance 2
SERVICE_PORT=8082 python service.py &

# Instance 3
SERVICE_PORT=8083 python service.py &
```

All instances automatically register with Consul and Eureka.

## Testing

### Unit Tests

```python
import unittest
from service import app

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_health(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'UP')
    
    def test_create_user(self):
        response = self.app.post('/users', json={
            'name': 'Test User',
            'email': 'test@example.com'
        })
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['name'], 'Test User')

if __name__ == '__main__':
    unittest.main()
```

### Integration Tests

```bash
# Start dependencies
docker-compose up -d consul eureka

# Run tests
python -m pytest tests/

# Cleanup
docker-compose down
```

### Load Testing

```bash
# Using Apache Bench
ab -n 1000 -c 10 http://localhost:8080/users

# Using wrk
wrk -t4 -c100 -d30s http://localhost:8080/users
```

## Production Deployment

### Docker

Create `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY service.py .

ENV SERVICE_PORT=8080

EXPOSE 8080

CMD ["python", "service.py"]
```

Build and run:

```bash
docker build -t user-service:1.0.0 .
docker run -p 8080:8080 \
  -e CONSUL_HOST=consul:8500 \
  -e EUREKA_HOST=eureka:8761 \
  user-service:1.0.0
```

### Kubernetes

Create deployment:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: user-service
spec:
  replicas: 3
  selector:
    matchLabels:
      app: user-service
  template:
    metadata:
      labels:
        app: user-service
    spec:
      containers:
      - name: user-service
        image: user-service:1.0.0
        ports:
        - containerPort: 8080
        env:
        - name: CONSUL_HOST
          value: "consul:8500"
        - name: EUREKA_HOST
          value: "eureka:8761"
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 5
```

## Troubleshooting

### Service Not Registering

```bash
# Check Consul connectivity
curl http://localhost:8500/v1/status/leader

# Check Eureka connectivity
curl http://localhost:8761/eureka/apps

# View service logs
tail -f service.log
```

### Health Check Failing

```bash
# Test health endpoint
curl -v http://localhost:8080/health

# Check service status
docker-compose ps

# View detailed logs
docker-compose logs -f user-service
```

### Service Discovery Issues

```bash
# List all registered services
curl http://localhost:8500/v1/catalog/services

# Query specific service
curl http://localhost:8500/v1/health/service/user-service?passing
```

## Resources

- [Spring Cloud Documentation](https://spring.io/projects/spring-cloud)
- [Consul Service Discovery](https://www.consul.io/docs/discovery/services)
- [Netflix Eureka](https://github.com/Netflix/eureka)
- [Jaeger Tracing](https://www.jaegertracing.io/docs/)
- [Microservices Patterns](https://microservices.io/patterns/)
