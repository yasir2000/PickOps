# ServiceMeshOps Examples

Production-ready service mesh implementations demonstrating traffic management, observability, and security patterns.

## Available Examples

### 1. [Istio Traffic Management](./istio-traffic-management/)
Complete Istio service mesh with:
- Virtual services and destination rules
- Traffic splitting (canary deployments)
- Circuit breaking and retries
- Fault injection for chaos testing
- Multi-version deployments

**Technologies**: Istio, Envoy, Kubernetes simulation, Python microservices

### 2. [Linkerd mTLS Security](./linkerd-mtls/)
Zero-trust security with automatic mTLS:
- Service-to-service encryption
- Traffic authorization policies
- Service profiles for observability
- Tap debugging utilities

**Technologies**: Linkerd, mTLS, gRPC, Go microservices

### 3. [Consul Service Discovery](./consul-discovery/)
Dynamic service discovery and configuration:
- Service registration and health checks
- KV store for configuration
- Distributed locking
- Connect service mesh integration

**Technologies**: Consul, Service Mesh, Configuration Management

### 4. [Observability Stack](./observability-stack/)
Complete observability for service mesh:
- Distributed tracing with Jaeger/Zipkin
- Service graph visualization (Kiali)
- Metrics collection (Prometheus)
- Dashboards and alerts (Grafana)
- OpenTelemetry instrumentation

**Technologies**: Jaeger, Zipkin, Kiali, Prometheus, Grafana, OpenTelemetry

### 5. [Multi-Mesh Architecture](./multi-mesh/)
Federated service mesh across environments:
- Multiple control planes
- Cross-mesh communication
- Gateway federation
- Traffic routing between meshes

**Technologies**: Istio, Linkerd, Consul, Envoy Gateway

## Getting Started

1. **Start ServiceMeshOps stack**:
```bash
cd ServiceMeshOps
docker-compose up -d
```

2. **Choose an example**:
```bash
cd examples/istio-traffic-management
```

3. **Follow example README** for specific setup instructions

## Service Mesh Comparison

| Feature | Istio | Linkerd | Consul |
|---------|-------|---------|--------|
| Complexity | High | Low | Medium |
| Performance | Good | Excellent | Good |
| Features | Complete | Focused | Service Discovery |
| mTLS | Manual | Automatic | Optional |
| Protocol | HTTP/gRPC/TCP | HTTP/gRPC/TCP | HTTP/gRPC |
| Observability | Full | Full | Basic |

## Common Patterns

### Canary Deployments
```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: my-service
spec:
  hosts:
  - my-service
  http:
  - match:
    - headers:
        version:
          exact: v2
    route:
    - destination:
        host: my-service
        subset: v2
  - route:
    - destination:
        host: my-service
        subset: v1
      weight: 90
    - destination:
        host: my-service
        subset: v2
      weight: 10
```

### Circuit Breaking
```yaml
apiVersion: networking.istio.io/v1alpha3
kind: DestinationRule
metadata:
  name: my-service
spec:
  host: my-service
  trafficPolicy:
    connectionPool:
      tcp:
        maxConnections: 100
      http:
        http1MaxPendingRequests: 50
        maxRequestsPerConnection: 5
    outlierDetection:
      consecutiveErrors: 5
      interval: 30s
      baseEjectionTime: 30s
```

## Prerequisites

- Docker and Docker Compose
- Basic understanding of microservices
- Familiarity with networking concepts
- (Optional) Kubernetes knowledge for production deployments

## Resources

- [Istio Documentation](https://istio.io/latest/docs/)
- [Linkerd Documentation](https://linkerd.io/2/overview/)
- [Consul Documentation](https://www.consul.io/docs)
- [Service Mesh Patterns](https://www.servicemeshpatterns.com/)
