# ServiceMeshOps - Service Mesh Operations

Advanced service mesh operations stack for microservices architecture with traffic management, observability, and security.

## Stack Components

### Service Mesh Control Planes
- **Istio** (ports 15010-15017) - Complete service mesh with traffic management
- **Linkerd** (ports 9995-9996) - Lightweight and secure service mesh
- **Consul** (port 8500) - Service discovery and mesh with HashiCorp ecosystem
- **Kuma** (ports 5681-5683) - Universal control plane built on Envoy

### Data Plane
- **Envoy Proxy** (ports 10000, 9901) - High-performance proxy for service mesh

### Observability
- **Jaeger** (port 16686) - Distributed tracing and monitoring
- **Zipkin** (port 9412) - Alternative distributed tracing system
- **Kiali** (port 20001) - Service mesh observability console
- **Prometheus** (port 9090) - Metrics collection
- **Grafana** (port 3000) - Metrics visualization
- **OpenTelemetry Collector** (ports 4317-4318) - Telemetry data collection

### Demo Services
- **Service A** (port 8081) - Sample microservice
- **Service B** (port 8082) - Sample microservice
- **Service C** (port 8083) - Sample microservice

## Quick Start

```bash
# Start the service mesh stack
docker-compose up -d

# View all services
docker-compose ps

# View logs
docker-compose logs -f

# Stop all services
docker-compose down
```

## Service Access

| Service | URL | Credentials |
|---------|-----|-------------|
| Consul | http://localhost:8500 | - |
| Jaeger UI | http://localhost:16686 | - |
| Zipkin UI | http://localhost:9412 | - |
| Kiali | http://localhost:20001 | admin / admin |
| Prometheus | http://localhost:9090 | - |
| Grafana | http://localhost:3000 | admin / admin |
| Service A | http://localhost:8081 | - |
| Service B | http://localhost:8082 | - |
| Service C | http://localhost:8083 | - |

## Use Cases

### Traffic Management
- **Load Balancing**: Distribute traffic across service instances
- **Circuit Breaking**: Prevent cascading failures
- **Retries**: Automatic retry policies
- **Timeouts**: Request timeout configuration
- **Canary Deployments**: Gradual rollout of new versions
- **A/B Testing**: Route traffic based on headers/conditions

### Security
- **mTLS**: Automatic mutual TLS between services
- **Authorization**: Service-to-service access control
- **Authentication**: Identity verification
- **Encryption**: End-to-end encryption

### Observability
- **Distributed Tracing**: Track requests across services
- **Metrics Collection**: Monitor service health and performance
- **Service Topology**: Visualize service dependencies
- **Traffic Flow**: Understand communication patterns

## Service Mesh Patterns

### Istio Configuration

```yaml
# VirtualService for traffic routing
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: service-a
spec:
  hosts:
  - service-a
  http:
  - match:
    - headers:
        version:
          exact: v2
    route:
    - destination:
        host: service-a
        subset: v2
  - route:
    - destination:
        host: service-a
        subset: v1
      weight: 90
    - destination:
        host: service-a
        subset: v2
      weight: 10
```

### Envoy Proxy Configuration

```yaml
# Basic Envoy configuration
static_resources:
  listeners:
  - name: listener_0
    address:
      socket_address:
        address: 0.0.0.0
        port_value: 10000
    filter_chains:
    - filters:
      - name: envoy.filters.network.http_connection_manager
        typed_config:
          "@type": type.googleapis.com/envoy.extensions.filters.network.http_connection_manager.v3.HttpConnectionManager
          stat_prefix: ingress_http
          route_config:
            name: local_route
            virtual_hosts:
            - name: backend
              domains: ["*"]
              routes:
              - match:
                  prefix: "/"
                route:
                  cluster: service_backend
```

### Consul Service Registration

```bash
# Register service with Consul
curl -X PUT -d @- http://localhost:8500/v1/agent/service/register << EOF
{
  "ID": "service-a-1",
  "Name": "service-a",
  "Tags": ["v1", "production"],
  "Address": "service-a",
  "Port": 8080,
  "Check": {
    "HTTP": "http://service-a:8080/health",
    "Interval": "10s"
  }
}
EOF
```

## Observability Setup

### Jaeger Tracing

```bash
# View traces in Jaeger UI
open http://localhost:16686

# Generate sample traces
for i in {1..100}; do
  curl http://localhost:8081
done
```

### Kiali Service Graph

```bash
# Access Kiali dashboard
open http://localhost:20001

# View service topology, traffic flow, and health
```

### Grafana Dashboards

```bash
# Access Grafana
open http://localhost:3000

# Import service mesh dashboards:
# - Istio Service Dashboard
# - Envoy Proxy Stats
# - Service Performance
```

## Configuration Files

### Prometheus Scraping

Create `prometheus/prometheus.yml`:

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'envoy-proxy'
    static_configs:
      - targets: ['envoy:9901']
  
  - job_name: 'istio-mesh'
    static_configs:
      - targets: ['istiod:15014']
  
  - job_name: 'consul'
    static_configs:
      - targets: ['consul:8500']
  
  - job_name: 'services'
    static_configs:
      - targets:
        - 'service-a:8080'
        - 'service-b:8080'
        - 'service-c:8080'
```

### OpenTelemetry Configuration

Create `otel/config.yaml`:

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

processors:
  batch:

exporters:
  jaeger:
    endpoint: jaeger:14250
    tls:
      insecure: true
  
  prometheus:
    endpoint: "0.0.0.0:8888"

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

## Testing Service Mesh Features

### Traffic Splitting

```bash
# 90% traffic to v1, 10% to v2
# Configure in Istio VirtualService

# Test traffic distribution
for i in {1..100}; do
  curl -s http://localhost:8081 | grep -o "v[12]"
done | sort | uniq -c
```

### Circuit Breaking

```bash
# Configure circuit breaker in Istio DestinationRule
# Test by overwhelming service

# Generate load
ab -n 1000 -c 50 http://localhost:8081/
```

### Retry Logic

```bash
# Configure automatic retries
# Test with failing service

# Observe retries in Jaeger traces
```

## Performance Tuning

### Envoy Resource Limits

```yaml
resources:
  limits:
    cpu: "2"
    memory: "2Gi"
  requests:
    cpu: "100m"
    memory: "128Mi"
```

### Istio Pilot Tuning

```bash
# Increase pilot resources
PILOT_CPU=2
PILOT_MEMORY=4Gi
```

## Security Features

### Enable mTLS

```yaml
# Istio PeerAuthentication
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: istio-system
spec:
  mtls:
    mode: STRICT
```

### Authorization Policies

```yaml
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: allow-service-a
spec:
  selector:
    matchLabels:
      app: service-b
  rules:
  - from:
    - source:
        principals: ["cluster.local/ns/default/sa/service-a"]
```

## Troubleshooting

### Check Envoy Configuration

```bash
# View Envoy admin interface
curl http://localhost:9901/config_dump

# Check cluster health
curl http://localhost:9901/clusters
```

### Debug Istio

```bash
# Check control plane status
docker exec servicemeshops-istiod pilot-discovery version

# Verify proxy configuration
docker exec servicemeshops-envoy curl localhost:15000/config_dump
```

### Consul Health Checks

```bash
# View service health
curl http://localhost:8500/v1/health/service/service-a

# Check agent members
curl http://localhost:8500/v1/agent/members
```

## Best Practices

1. **Start Simple**: Begin with one service mesh (Istio or Linkerd)
2. **Enable Observability First**: Set up tracing and metrics before traffic management
3. **Gradual Rollout**: Use canary deployments for mesh adoption
4. **Monitor Resource Usage**: Service mesh adds overhead
5. **Test Failure Scenarios**: Verify circuit breakers and retries work
6. **Secure by Default**: Enable mTLS from the start
7. **Version Control Configs**: Keep all mesh configurations in Git
8. **Use Sidecars Wisely**: Not every service needs a sidecar

## Resource Requirements

### Minimum
- CPU: 4 cores
- RAM: 8 GB
- Disk: 20 GB

### Recommended
- CPU: 8+ cores
- RAM: 16 GB
- Disk: 50 GB

## Migration Strategies

### Brownfield (Existing Services)
1. Deploy service mesh control plane
2. Add sidecars to one service at a time
3. Enable mTLS gradually
4. Migrate traffic management rules

### Greenfield (New Services)
1. Deploy full mesh from start
2. Use mesh for all inter-service communication
3. Build with mesh capabilities in mind

## License

Open source components under Apache 2.0, MIT, and other permissive licenses.
