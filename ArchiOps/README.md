# ArchiOps - Architecture Operations (All Industries)

**Comprehensive architecture operations stack for building architecture, software architecture, enterprise architecture, system architecture, and solution architecture.**

ArchiOps provides a complete platform for architects across all disciplines - from building architects using BIM and CAD tools to software architects designing complex systems using C4 models and architecture diagrams.

---

## 🏗️ Architecture Disciplines Supported

### Building & Physical Architecture
- **BIM (Building Information Modeling)** - Full 3D modeling and lifecycle management
- **CAD Design** - Computer-aided design tools
- **Blueprint Management** - Technical drawings and specifications
- **Site Planning** - Urban planning and landscape architecture

### Software & System Architecture
- **C4 Model** - Context, Containers, Components, Code diagrams
- **UML Diagrams** - Unified modeling language
- **Architecture Decision Records** - ADR management
- **Design Patterns** - Software architecture patterns

### Enterprise Architecture
- **TOGAF Framework** - Enterprise architecture framework
- **Business Process Modeling** - BPM and workflow design
- **Capability Mapping** - Business capability models
- **Technology Roadmaps** - Strategic planning

### Solution Architecture
- **Integration Patterns** - Service integration designs
- **API Architecture** - API gateway and management designs
- **Cloud Architecture** - Cloud-native architecture patterns
- **Microservices Design** - Distributed system architecture

---

## 🚀 Services Included (20 Components)

### Core Infrastructure
1. **PostgreSQL** (Port 5432) - Architecture projects database
2. **Redis** (Port 6379) - Session cache & real-time collaboration
3. **MinIO** (Ports 9000-9001) - BIM files, 3D models & blueprint storage
4. **Elasticsearch** (Port 9200) - Full-text search for designs
5. **RabbitMQ** (Ports 5672, 15672) - Event-driven collaboration

### CAD & BIM Tools
6. **FreeCAD Web** (Port 3010) - Open-source CAD platform
7. **BIMServer** (Port 8081) - Building Information Modeling server
8. **MinIO Console** (Port 9001) - File management interface

### Diagramming & Visualization
9. **Draw.io** (Port 8083) - Architecture diagrams & blueprints
10. **Structurizr** (Port 8084) - C4 model software architecture
11. **PlantUML** (Port 8085) - Diagram as code (UML, sequence, etc.)
12. **Mermaid Live** (Port 8086) - Interactive diagram editor
13. **Excalidraw** (Port 8087) - Collaborative whiteboarding

### Application Layer
14. **Backend API** (Port 3000) - RESTful API for architecture data
15. **Frontend Portal** (Port 8080) - Architecture management interface

### Analytics & Monitoring
16. **Metabase** (Port 3001) - Project analytics & BI
17. **Kibana** (Port 5601) - Search analytics dashboard
18. **Prometheus** (Port 9090) - Metrics collection
19. **Grafana** (Port 3003) - Architecture dashboards

### Version Control
20. **Gitea** (Ports 3002, 2222) - Documentation & code repository

---

## 📋 Quick Start

### 1. Initial Setup
```bash
cd ArchiOps
cp .env.example .env
# Edit .env with your credentials
```

### 2. Launch All Services
```bash
docker-compose up -d
```

### 3. Verify Services
```bash
docker-compose ps
```

### 4. Access Platforms

| Service | URL | Default Credentials |
|---------|-----|---------------------|
| **Architecture Portal** | http://localhost:8080 | - |
| **BIMServer** | http://localhost:8081 | admin@bimserver.org / admin |
| **Draw.io** | http://localhost:8083 | - |
| **Structurizr (C4)** | http://localhost:8084 | - |
| **PlantUML** | http://localhost:8085 | - |
| **Mermaid** | http://localhost:8086 | - |
| **Excalidraw** | http://localhost:8087 | - |
| **FreeCAD Web** | http://localhost:3010 | - |
| **MinIO Console** | http://localhost:9001 | minioadmin / minioadmin123 |
| **Metabase** | http://localhost:3001 | Setup on first access |
| **Kibana** | http://localhost:5601 | - |
| **Gitea** | http://localhost:3002 | Setup on first access |
| **RabbitMQ** | http://localhost:15672 | admin / archiops123 |
| **Grafana** | http://localhost:3003 | admin / archiops123 |
| **Prometheus** | http://localhost:9090 | - |

---

## 🎯 Key Features

### Multi-Discipline Architecture Support
- **Building Architecture** - BIM, CAD, blueprints, site plans
- **Software Architecture** - C4 models, UML, sequence diagrams
- **Enterprise Architecture** - Business capability maps, roadmaps
- **Solution Architecture** - Integration patterns, API designs
- **System Architecture** - Infrastructure diagrams, topology maps

### Collaborative Design
- Real-time collaboration via Redis
- Version control with Gitea
- Event-driven updates via RabbitMQ
- Shared whiteboarding with Excalidraw
- Comment and review workflows

### Documentation as Code
- PlantUML for diagram versioning
- Structurizr DSL for C4 models
- Mermaid for embedded diagrams
- Markdown-based documentation
- Git-based version control

### Project Management
- Project tracking and milestones
- Resource allocation
- Timeline management
- Budget tracking
- Stakeholder management

### Analytics & Reporting
- Project KPIs and metrics
- Resource utilization reports
- Design iteration analytics
- Collaboration statistics
- Cost analysis

---

## 💼 Use Cases

### 1. Building Architecture Project
```bash
# Access BIMServer for 3D modeling
http://localhost:8081

# Upload blueprints to MinIO
http://localhost:9001

# Create site plans in Draw.io
http://localhost:8083

# Track project in Metabase
http://localhost:3001
```

### 2. Software Architecture Documentation
```bash
# Create C4 model in Structurizr
http://localhost:8084

# Generate UML diagrams with PlantUML
http://localhost:8085

# Interactive diagrams in Mermaid
http://localhost:8086

# Version control with Gitea
http://localhost:3002
```

### 3. Enterprise Architecture Planning
```bash
# Business capability maps in Draw.io
http://localhost:8083

# Collaborative planning in Excalidraw
http://localhost:8087

# Analytics in Metabase
http://localhost:3001

# Documentation in Gitea
http://localhost:3002
```

### 4. Solution Architecture Design
```bash
# API architecture in PlantUML
curl -X POST http://localhost:8085/png/ \
  -d '@startuml
  package "API Gateway" {
    [Kong]
  }
  package "Services" {
    [User Service]
    [Order Service]
  }
  [Kong] --> [User Service]
  [Kong] --> [Order Service]
  @enduml'

# Integration patterns in Structurizr
# Cloud architecture in Draw.io
# Version control in Gitea
```

---

## 🏗️ Architecture Patterns

### C4 Model (Software Architecture)
ArchiOps includes Structurizr for creating C4 model diagrams:
- **Level 1: Context** - System context diagrams
- **Level 2: Container** - Container diagrams
- **Level 3: Component** - Component diagrams
- **Level 4: Code** - Class diagrams

### BIM Workflow (Building Architecture)
Complete BIM workflow support:
1. **Design** - FreeCAD for 3D modeling
2. **Collaboration** - BIMServer for model sharing
3. **Documentation** - Draw.io for 2D drawings
4. **Storage** - MinIO for file management
5. **Review** - Version control with Gitea

### Diagram as Code
Multiple diagram-as-code tools:
- **PlantUML** - UML, sequence, activity diagrams
- **Mermaid** - Flowcharts, Gantt, state diagrams
- **Structurizr DSL** - C4 model diagrams

---

## 📊 API Examples

### Create Architecture Project
```bash
curl -X POST http://localhost:3000/api/projects \
  -H "Content-Type: application/json" \
  -d '{
    "name": "City Hall Renovation",
    "type": "building_architecture",
    "client": "City Government",
    "status": "planning",
    "budget": 5000000
  }'
```

### Upload BIM Model
```bash
curl -X POST http://localhost:3000/api/models/upload \
  -F "file=@building-model.ifc" \
  -F "project_id=123" \
  -F "type=bim"
```

### Generate Architecture Diagram
```bash
curl -X POST http://localhost:3000/api/diagrams/generate \
  -H "Content-Type: application/json" \
  -d '{
    "type": "c4_container",
    "system": "E-Commerce Platform",
    "containers": [
      {"name": "Web App", "technology": "React"},
      {"name": "API", "technology": "Node.js"},
      {"name": "Database", "technology": "PostgreSQL"}
    ]
  }'
```

### Search Architecture Documents
```bash
curl "http://localhost:9200/architecture/_search?q=microservices"
```

---

## 🔐 Security Features

### Authentication & Authorization
- JWT-based API authentication
- Role-based access control (RBAC)
- Project-level permissions
- User group management
- SSO integration ready

### Data Protection
- Encrypted storage for sensitive designs
- Audit logging for all changes
- Version control for all documents
- Backup and disaster recovery
- Data retention policies

### Compliance
- ISO 19650 (BIM standard) support
- Architecture documentation standards
- Design review workflows
- Change management processes
- Quality assurance gates

---

## 📈 Resource Requirements

### Minimum Configuration
- **CPU**: 8 cores
- **RAM**: 16 GB
- **Disk**: 100 GB SSD
- **Network**: 100 Mbps

### Recommended Configuration
- **CPU**: 16 cores
- **RAM**: 32 GB
- **Disk**: 500 GB SSD (NVMe preferred)
- **Network**: 1 Gbps
- **GPU**: Optional for 3D rendering

### Storage Estimates
- **BIM Models**: 100-500 MB per model
- **CAD Files**: 10-100 MB per drawing
- **Diagrams**: 1-10 MB per diagram
- **Documentation**: 1-5 MB per project
- **Analytics Data**: 10 GB for 1 year

---

## 🔧 Configuration

### Environment Variables
All configuration in `.env` file:
```bash
# Database
POSTGRES_PASS=archiops2024
POSTGRES_PORT=5432

# Cache
REDIS_PORT=6379

# Object Storage
MINIO_USER=minioadmin
MINIO_PASS=minioadmin123
MINIO_PORT=9000

# Security
JWT_SECRET=archiops-secret-key-2024
GRAFANA_PASS=archiops123
RABBITMQ_PASS=archiops123

# Service Ports
BACKEND_PORT=3000
FRONTEND_PORT=8080
BIMSERVER_PORT=8081
DRAWIO_PORT=8083
STRUCTURIZR_PORT=8084
PLANTUML_PORT=8085
MERMAID_PORT=8086
EXCALIDRAW_PORT=8087
```

---

## 📚 Examples

See the `examples/` directory for:
1. **BIM Workflow** - Complete building architecture project
2. **Software Architecture** - C4 model implementation
3. **Enterprise Architecture** - Capability mapping example
4. **API Integration** - REST API usage patterns
5. **Diagram Templates** - Ready-to-use architecture diagrams

---

## 🎓 Architecture Frameworks Supported

- **TOGAF** - The Open Group Architecture Framework
- **Zachman** - Zachman Framework for Enterprise Architecture
- **DoDAF** - Department of Defense Architecture Framework
- **FEAF** - Federal Enterprise Architecture Framework
- **C4 Model** - Context, Containers, Components, Code
- **4+1** - Logical, Process, Development, Physical, Scenarios
- **ISO 19650** - Building Information Modeling standards

---

## 🌟 Best Practices

### Version Control
- Store all diagrams in Git (diagram-as-code)
- Use semantic versioning for designs
- Tag major milestones
- Maintain changelog for each project

### Documentation
- Keep architecture decision records (ADRs)
- Document design rationale
- Maintain stakeholder matrix
- Update diagrams with code changes

### Collaboration
- Daily standup via shared dashboards
- Design review workflows
- Comment-based feedback
- Real-time collaboration sessions

### Quality Assurance
- Peer review all designs
- Automated consistency checks
- Compliance validation
- Performance modeling

---

## 🔄 Integration

### CI/CD Integration
```yaml
# .gitlab-ci.yml example
architecture-validation:
  script:
    - plantuml -checkonly diagrams/*.puml
    - structurizr-cli validate workspace.json
```

### Webhooks
Configure webhooks for:
- Design change notifications
- Review status updates
- Build pipeline triggers
- Analytics data collection

---

## 📞 Support

- **Documentation**: http://localhost:8080/docs
- **API Reference**: http://localhost:3000/api-docs
- **Architecture Guide**: http://localhost:3002/architecture/guide

---

## 📄 License

See main repository LICENSE file.

---

**ArchiOps** - *Where all architecture disciplines converge into one powerful operational platform!*

From skyscrapers to microservices, from urban planning to cloud architecture - ArchiOps has you covered! 🏗️💻🏛️
