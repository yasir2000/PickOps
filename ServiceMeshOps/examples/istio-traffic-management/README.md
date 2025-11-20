# Istio Traffic Management

Complete Istio-style traffic management using Envoy proxy with canary deployments, circuit breaking, and fault injection.

## Architecture

```
┌─────────────┐
│   Client    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    Envoy    │ ← Traffic routing, retries, circuit breaking
│   (Proxy)   │
└──────┬──────┘
       │
       ├─────70%────► ┌──────────────┐
       │              │  Service v1  │ (Stable)
       │              └──────────────┘
       │
       ├─────25%────► ┌──────────────┐
       │              │  Service v2  │ (Canary)
       │              └──────────────┘
       │
       └──────5%────► ┌──────────────┐
                      │  Service v3  │ (Experimental)
                      └──────────────┘
```

## Features

- **Traffic Splitting**: 70/25/5 distribution across versions
- **Circuit Breaking**: Connection limits and outlier detection
- **Retry Logic**: Automatic retries on failures
- **Health Checks**: Active health checking for all services
- **Timeout Handling**: Per-route timeout configuration

## Quick Start

### 1. Start Services

```bash
# Ensure ServiceMeshOps network exists
docker network create servicemeshops_servicemesh

# Start the demo
docker-compose up -d
```

### 2. Access Services

- **Envoy Proxy**: http://localhost:8000
- **Service v1**: http://localhost:5001
- **Service v2**: http://localhost:5002
- **Service v3**: http://localhost:5003
- **Envoy Admin**: http://localhost:9901

### 3. Test Traffic Routing

```bash
# Send requests and observe version distribution
for i in {1..20}; do
  curl -s http://localhost:8000/ | jq -r '.version'
done

# Should show ~70% v1, ~25% v2, ~5% v3
```

## Traffic Patterns

### Canary Deployment (70/25/5)

```yaml
# envoy.yaml
route:
  weighted_clusters:
    clusters:
    - name: service_v1
      weight: 70    # Stable version
    - name: service_v2
      weight: 25    # Canary version
    - name: service_v3
      weight: 5     # Experimental
```

Test it:
```bash
# Run 100 requests and count versions
for i in {1..100}; do
  curl -s http://localhost:8000/ | jq -r '.version'
done | sort | uniq -c
```

### Circuit Breaker

```yaml
circuit_breakers:
  thresholds:
  - priority: DEFAULT
    max_connections: 50
    max_pending_requests: 25
    max_requests: 50
    max_retries: 2
```

Test it:
```bash
# Generate high error rate
for i in {1..50}; do
  curl http://localhost:8000/api/error?rate=0.8 &
done

# Circuit should open, protecting upstream services
```

### Outlier Detection

```yaml
outlier_detection:
  consecutive_5xx: 5        # 5 consecutive errors
  interval: 30s             # Check every 30s
  base_ejection_time: 30s   # Eject for 30s
  max_ejection_percent: 50  # Max 50% of hosts
```

Trigger it:
```bash
# Service v3 has 10% error rate
# After 5 consecutive errors, it gets ejected
for i in {1..20}; do
  curl -s http://localhost:8000/ | jq -r '.version'
  sleep 0.5
done
```

### Retry Policy

```yaml
retry_policy:
  retry_on: "5xx"
  num_retries: 3
  per_try_timeout: 2s
```

Test it:
```bash
# Retries happen automatically on 5xx errors
curl -v http://localhost:8000/api/error?rate=0.5

# Check Envoy stats for retry counts
curl http://localhost:9901/stats | grep retry
```

### Timeout Configuration

```yaml
route:
  timeout: 5s
  retry_policy:
    per_try_timeout: 2s
```

Test it:
```bash
# 1s delay - should succeed
curl http://localhost:8000/api/slow?delay=1

# 3s delay - should timeout per attempt, retry
curl http://localhost:8000/api/slow?delay=3

# 6s delay - should timeout completely
curl http://localhost:8000/api/slow?delay=6
```

## Monitoring

### Envoy Admin Interface

Access at http://localhost:9901

#### Key Endpoints

```bash
# Stats
curl http://localhost:9901/stats

# Cluster health
curl http://localhost:9901/clusters

# Configuration dump
curl http://localhost:9901/config_dump

# Runtime settings
curl http://localhost:9901/runtime
```

#### Important Metrics

```bash
# Upstream requests
curl http://localhost:9901/stats | grep upstream_rq

# Circuit breaker stats
curl http://localhost:9901/stats | grep circuit_breakers

# Retry stats
curl http://localhost:9901/stats | grep retry

# Timeout stats
curl http://localhost:9901/stats | grep timeout
```

### Service Endpoints

Each service version exposes:

- `GET /` - Main endpoint with version info
- `GET /health` - Health check
- `GET /ready` - Readiness check
- `GET /api/data` - Version-specific data processing
- `GET /api/slow?delay=N` - Slow endpoint (N seconds)
- `GET /api/error?rate=N` - Error endpoint (N error rate 0-1)

## Load Testing

### Using Apache Bench

```bash
# 1000 requests, 10 concurrent
ab -n 1000 -c 10 http://localhost:8000/

# With POST data
ab -n 500 -c 5 -p data.json -T application/json http://localhost:8000/api/data
```

### Using wrk

```bash
# 30 seconds, 10 threads, 100 connections
wrk -t10 -c100 -d30s http://localhost:8000/

# With Lua script for complex scenarios
wrk -t10 -c100 -d30s -s script.lua http://localhost:8000/
```

### Automated Traffic Generator

The included traffic generator runs automatically:

```bash
# View logs
docker-compose logs -f traffic-gen
```

It tests:
1. Canary deployment distribution
2. Normal sustained traffic
3. Burst traffic patterns
4. Circuit breaker triggering
5. Timeout handling

## Advanced Scenarios

### Progressive Canary Rollout

Edit `envoy.yaml` to adjust weights:

```yaml
# Stage 1: 95/5/0
- name: service_v1
  weight: 95
- name: service_v2
  weight: 5

# Stage 2: 75/25/0
- name: service_v1
  weight: 75
- name: service_v2
  weight: 25

# Stage 3: 50/50/0
- name: service_v1
  weight: 50
- name: service_v2
  weight: 50

# Stage 4: Full rollout
- name: service_v2
  weight: 100
```

Reload Envoy:
```bash
docker-compose restart envoy
```

### Header-Based Routing

Add to `envoy.yaml`:

```yaml
routes:
- match:
    prefix: "/"
    headers:
    - name: "x-version"
      exact_match: "v2"
  route:
    cluster: service_v2
- match:
    prefix: "/"
  route:
    weighted_clusters:
      clusters:
      - name: service_v1
        weight: 90
      - name: service_v2
        weight: 10
```

Test:
```bash
# Force v2
curl -H "x-version: v2" http://localhost:8000/

# Default routing
curl http://localhost:8000/
```

### Fault Injection

Add to `envoy.yaml`:

```yaml
http_filters:
- name: envoy.filters.http.fault
  typed_config:
    "@type": type.googleapis.com/envoy.extensions.filters.http.fault.v3.HTTPFault
    delay:
      fixed_delay: 1s
      percentage:
        numerator: 10
        denominator: HUNDRED
    abort:
      http_status: 503
      percentage:
        numerator: 5
        denominator: HUNDRED
```

This injects:
- 1s delay for 10% of requests
- 503 errors for 5% of requests

## Integration with ServiceMeshOps

### Prometheus Metrics

Configure Envoy to expose metrics:

```yaml
stats_sinks:
- name: envoy.stat_sinks.prometheus
  typed_config:
    "@type": type.googleapis.com/envoy.config.metrics.v3.PrometheusSink
```

Scrape in Prometheus (add to ServiceMeshOps):

```yaml
scrape_configs:
- job_name: 'envoy'
  static_configs:
  - targets: ['demo-envoy:9901']
```

### Jaeger Tracing

Add tracing configuration:

```yaml
tracing:
  http:
    name: envoy.tracers.zipkin
    typed_config:
      "@type": type.googleapis.com/envoy.config.trace.v3.ZipkinConfig
      collector_cluster: jaeger
      collector_endpoint: "/api/v2/spans"
```

### Grafana Dashboards

Import Envoy dashboards:
- Dashboard ID: 11021 (Envoy Global)
- Dashboard ID: 6693 (Envoy Cluster)

## Troubleshooting

### High Error Rate

```bash
# Check service health
docker-compose ps

# View service logs
docker-compose logs demo-service-v1
docker-compose logs demo-service-v2
docker-compose logs demo-service-v3

# Check Envoy routing
curl http://localhost:9901/clusters | grep health
```

### Traffic Not Routing

```bash
# Verify Envoy config
curl http://localhost:9901/config_dump | jq '.configs[1]'

# Check listener status
curl http://localhost:9901/listeners

# View Envoy logs
docker-compose logs envoy
```

### Circuit Breaker Not Triggering

```bash
# Check circuit breaker stats
curl http://localhost:9901/stats | grep circuit_breakers

# Verify configuration
curl http://localhost:9901/config_dump | jq '.configs[2].dynamic_active_clusters[] | select(.cluster.name=="service_v3") | .cluster.circuit_breakers'
```

## Cleanup

```bash
docker-compose down
```

## Resources

- [Envoy Proxy Documentation](https://www.envoyproxy.io/docs)
- [Istio Traffic Management](https://istio.io/latest/docs/concepts/traffic-management/)
- [Service Mesh Patterns](https://www.servicemeshpatterns.com/)
