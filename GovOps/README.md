# GovOps - Government Operations

Complete e-government infrastructure for digital public services, citizen engagement, and transparent governance.

## Overview

GovOps provides a comprehensive platform for modern government operations including citizen services, document management, workflow automation, GIS mapping, public procurement, and data analytics.

## Services (17 Components)

### Citizen Services
- **Government Portal** (8080): Liferay-based citizen services portal
- **Identity Management** (8081): Keycloak for citizen authentication
- **API Gateway** (8084): Kong for secure API access

### Document & Records Management
- **Alfresco** (8082): Enterprise document management
- **Case Management** (5433): OpenCase for government cases
- **Elasticsearch** (9200): Full-text search across documents

### Workflow & Process
- **Camunda** (8083): BPMN workflow engine for government processes
- **RabbitMQ** (5672, 15672): Message queue for inter-service communication

### Geospatial Services
- **GeoServer** (8086): Geographic information system
- Maps, zoning, land registry, infrastructure planning

### Analytics & Reporting
- **Apache Superset** (8087): Census and statistical analysis
- **Metabase** (3000): Business intelligence and dashboards

### Procurement & Finance
- **Odoo** (8088): Public procurement and ERP system

### Elections & Democracy
- **Redis** (6379): Election data and real-time results

### Monitoring
- **Prometheus** (9090): Metrics collection
- **Grafana** (3001): Operational dashboards

## Quick Start

```bash
cd GovOps
docker-compose up -d
```

## Key Features

### 1. **Citizen Portal**
- Service requests and applications
- License renewals
- Tax payments
- Permit applications
- Complaint management

### 2. **Document Management**
- Secure document storage
- Version control
- Access permissions
- Full-text search
- Archival and retention policies

### 3. **Workflow Automation**
- Application approvals
- Multi-level reviews
- SLA tracking
- Escalation management
- Audit trails

### 4. **GIS Integration**
- Property mapping
- Zoning information
- Infrastructure planning
- Emergency response mapping
- Public transport routes

### 5. **Data Analytics**
- Population statistics
- Service usage metrics
- Budget analysis
- Performance dashboards
- Transparency reports

### 6. **Public Procurement**
- Tender management
- Vendor registration
- Bid evaluation
- Contract management
- Payment processing

## Use Cases

### Citizen Services
```bash
# Register new citizen
curl -X POST http://localhost:8084/api/citizens \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Citizen",
    "id_number": "123456789",
    "email": "john@example.com",
    "address": "123 Main St"
  }'

# Submit service request
curl -X POST http://localhost:8084/api/requests \
  -H "Authorization: Bearer $TOKEN" \
  -d '{
    "type": "building_permit",
    "details": "New construction",
    "attachments": ["blueprint.pdf"]
  }'
```

### Workflow Management
```bash
# Start approval workflow
curl -X POST http://localhost:8083/engine-rest/process-definition/key/permit-approval/start \
  -H "Content-Type: application/json" \
  -d '{
    "variables": {
      "applicant": {"value": "John Citizen"},
      "permit_type": {"value": "building"}
    }
  }'
```

### GIS Queries
```bash
# Get zoning information
curl "http://localhost:8086/geoserver/wfs?service=WFS&version=1.0.0&request=GetFeature&typeName=zoning&CQL_FILTER=parcel_id='12345'"
```

## Access Points

- **Citizen Portal**: http://localhost:8080
- **Admin Dashboard**: http://localhost:8081 (admin/admin)
- **Document Management**: http://localhost:8082
- **Workflow Console**: http://localhost:8083/camunda
- **GIS Maps**: http://localhost:8086/geoserver
- **Analytics**: http://localhost:8087
- **Reports**: http://localhost:3000
- **Procurement**: http://localhost:8088

## Configuration

See `.env.example` for configuration options:
- Database credentials
- Admin passwords
- API keys
- Service URLs

## Security Features

- Multi-factor authentication
- Role-based access control (RBAC)
- Audit logging
- Data encryption
- API rate limiting
- GDPR compliance

## Compliance

- **ISO 27001**: Information security
- **WCAG 2.1**: Web accessibility
- **GDPR**: Data protection
- **Open Government**: Transparency standards

## Resource Requirements

**Minimum**:
- CPU: 8 cores
- RAM: 16GB
- Disk: 100GB

**Recommended**:
- CPU: 16 cores
- RAM: 32GB
- Disk: 500GB SSD

## Examples

See `examples/` directory for:
1. Citizen registration workflow
2. Permit application process
3. GIS data integration
4. Analytics dashboard setup
5. Procurement tender automation

## License

Open source - See LICENSE file
