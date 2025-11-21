# MediOps - Medical Operations

Comprehensive operational stack for Medical Operations.

## Services

- **PostgreSQL**: Core database
- **Redis**: Caching and session store
- **Backend API**: RESTful API service
- **Frontend**: Web interface
- **RabbitMQ**: Message queue
- **Metabase**: Analytics and BI
- **Prometheus**: Metrics collection
- **Grafana**: Dashboards and monitoring

## Quick Start

```bash
cd MediOps
cp .env.example .env
docker-compose up -d
```

## Access Points

- **Frontend**: http://localhost:8080
- **Backend API**: http://localhost:3000
- **RabbitMQ Management**: http://localhost:15672 (admin/admin)
- **Analytics**: http://localhost:3001
- **Grafana**: http://localhost:3002 (admin/admin)
- **Prometheus**: http://localhost:9090

## Key Services

emr-system,appointment-scheduler,lab-integration,pharmacy-management,billing

## Configuration

Edit `.env` file for custom configuration:
- Database credentials
- Service ports
- Admin passwords

## Examples

See `examples/` directory for:
- API integration examples
- Dashboard configurations
- Workflow automation
- Data analytics

## Resource Requirements

**Minimum**: 4 cores, 8GB RAM, 50GB disk
**Recommended**: 8 cores, 16GB RAM, 100GB disk

## License

See main repository LICENSE file.
