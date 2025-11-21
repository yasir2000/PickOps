# ArchiOps Examples

Production-ready examples for **Architecture Operations** across all disciplines.

## 📁 Available Examples

### 1. Building Architecture Project
Complete BIM workflow for construction projects.

**Files:**
- `building-architecture/` - Building design workflow
- `bim-workflow.md` - BIM process documentation
- `sample-project.ifc` - Sample IFC file

**Tools Used:**
- BIMServer for model management
- FreeCAD for 3D modeling
- Draw.io for 2D blueprints
- MinIO for file storage

### 2. Software Architecture with C4 Model
Complete software system architecture using C4 model.

**Files:**
- `software-architecture/` - C4 model examples
- `workspace.dsl` - Structurizr DSL workspace
- `diagrams/` - PlantUML diagrams

**Includes:**
- Context diagrams
- Container diagrams
- Component diagrams
- Deployment diagrams

### 3. Enterprise Architecture
Business capability mapping and technology roadmaps.

**Files:**
- `enterprise-architecture/` - EA framework examples
- `capability-map.drawio` - Business capability map
- `technology-roadmap.md` - Strategic planning

**Frameworks:**
- TOGAF alignment
- Capability-based planning
- Technology stack visualization

### 4. API Architecture Design
RESTful API and microservices architecture patterns.

**Files:**
- `api-architecture/` - API design examples
- `api-patterns.puml` - PlantUML API diagrams
- `openapi.yaml` - API specifications

**Patterns:**
- API Gateway pattern
- Backend for Frontend (BFF)
- Service mesh architecture
- Event-driven architecture

### 5. Diagram Templates
Ready-to-use architecture diagram templates.

**Includes:**
- PlantUML templates
- Mermaid templates
- Draw.io templates
- Structurizr templates

---

## 🚀 Getting Started

### Example 1: Create Building Architecture Project

```bash
# 1. Access BIMServer
http://localhost:8081

# 2. Create new project
# 3. Upload IFC model
# 4. Share with team

# 5. Generate 2D drawings in Draw.io
http://localhost:8083
```

### Example 2: Document Software Architecture

```bash
# 1. Create Structurizr workspace
cd examples/software-architecture
cp workspace.dsl /workspaces/

# 2. Access Structurizr
http://localhost:8084

# 3. View C4 diagrams
# 4. Export to images or HTML
```

### Example 3: Generate PlantUML Diagrams

```bash
# Create sequence diagram
curl -X POST http://localhost:8085/png/ \
  -d '@startuml
  actor User
  participant "API Gateway" as Gateway
  participant "Auth Service" as Auth
  participant "User Service" as Users
  
  User -> Gateway: Login Request
  Gateway -> Auth: Validate Credentials
  Auth -> Gateway: JWT Token
  Gateway -> User: Token Response
  
  User -> Gateway: Get Profile
  Gateway -> Auth: Validate Token
  Auth -> Gateway: Valid
  Gateway -> Users: Fetch Profile
  Users -> Gateway: Profile Data
  Gateway -> User: Profile Response
  @enduml' > architecture.png
```

### Example 4: Interactive Mermaid Diagrams

```bash
# Access Mermaid Live Editor
http://localhost:8086

# Paste this flowchart:
flowchart TD
    A[Requirements] --> B{Architecture Type?}
    B -->|Building| C[BIM Model]
    B -->|Software| D[C4 Diagram]
    B -->|Enterprise| E[Capability Map]
    C --> F[Construction Docs]
    D --> G[Implementation]
    E --> H[Roadmap]
```

---

## 📊 Example Workflows

### Building Architecture Workflow

```
1. Initial Design
   ├─ Sketches in Excalidraw
   ├─ 3D Model in FreeCAD
   └─ Store in MinIO

2. BIM Development
   ├─ Upload to BIMServer
   ├─ Collaborative editing
   └─ Version control in Gitea

3. Documentation
   ├─ 2D drawings in Draw.io
   ├─ Specifications in Gitea
   └─ Project tracking in Metabase

4. Review & Approval
   ├─ Design reviews
   ├─ Client feedback
   └─ Final approvals
```

### Software Architecture Workflow

```
1. Requirements Analysis
   ├─ Context diagram (C4 Level 1)
   └─ Stakeholder identification

2. High-Level Design
   ├─ Container diagram (C4 Level 2)
   ├─ Technology choices
   └─ Integration patterns

3. Detailed Design
   ├─ Component diagrams (C4 Level 3)
   ├─ API specifications
   └─ Database schema

4. Documentation
   ├─ Architecture Decision Records
   ├─ Diagram versioning in Git
   └─ Code generation from models
```

---

## 🎯 Use Case Examples

### UC-1: Multi-Story Building Design

**Objective:** Design a 10-story commercial building

**Steps:**
1. Create project in ArchiOps portal
2. Initial design in FreeCAD
3. Upload IFC model to BIMServer
4. Generate floor plans in Draw.io
5. Structural analysis documentation
6. Share with engineering team
7. Track progress in Metabase

### UC-2: Microservices Architecture

**Objective:** Design scalable e-commerce platform

**Steps:**
1. Create context diagram in Structurizr
2. Define containers (web, API, databases)
3. Detail component diagrams
4. Generate API specs with PlantUML
5. Document ADRs in Gitea
6. Create deployment diagrams
7. Export to team wiki

### UC-3: Enterprise Capability Mapping

**Objective:** Map business capabilities to applications

**Steps:**
1. Create capability model in Draw.io
2. Map applications to capabilities
3. Identify gaps and redundancies
4. Create technology roadmap
5. Present to stakeholders
6. Track implementation in Metabase

---

## 📝 Code Examples

### Example: API Endpoint for Creating Architecture Project

```javascript
// backend/routes/projects.js
const express = require('express');
const router = express.Router();
const { Pool } = require('pg');

const pool = new Pool({
  connectionString: process.env.DATABASE_URL
});

// Create new architecture project
router.post('/api/projects', async (req, res) => {
  const { name, type, client, budget } = req.body;
  
  try {
    const result = await pool.query(
      `INSERT INTO architecture_projects 
       (name, type, client, budget, status) 
       VALUES ($1, $2, $3, $4, 'planning') 
       RETURNING *`,
      [name, type, client, budget]
    );
    
    res.json(result.rows[0]);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Get all projects
router.get('/api/projects', async (req, res) => {
  try {
    const result = await pool.query(
      'SELECT * FROM architecture_projects ORDER BY created_at DESC'
    );
    res.json(result.rows);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

module.exports = router;
```

### Example: Structurizr DSL Workspace

```
workspace "E-Commerce Platform" "Software Architecture" {

    model {
        user = person "Customer" "A customer of the platform"
        
        ecommerce = softwareSystem "E-Commerce Platform" {
            webapp = container "Web Application" "React SPA"
            api = container "API Gateway" "Kong API Gateway"
            userService = container "User Service" "Node.js microservice"
            orderService = container "Order Service" "Node.js microservice"
            database = container "Database" "PostgreSQL"
        }
        
        user -> webapp "Uses"
        webapp -> api "Makes API calls"
        api -> userService "Routes requests"
        api -> orderService "Routes requests"
        userService -> database "Reads/Writes"
        orderService -> database "Reads/Writes"
    }

    views {
        systemContext ecommerce {
            include *
            autolayout lr
        }
        
        container ecommerce {
            include *
            autolayout lr
        }
    }
}
```

---

## 🎨 Diagram Templates

All templates available in `templates/` directory:

- **PlantUML**: Sequence, class, component, deployment
- **Mermaid**: Flowchart, Gantt, state, ER
- **Draw.io**: Network, cloud, building, process
- **Structurizr**: C4 context, container, component

---

## 📚 Documentation Standards

### Architecture Decision Records (ADR)

```markdown
# ADR-001: Use Microservices Architecture

## Status
Accepted

## Context
Need scalable, independently deployable services.

## Decision
Adopt microservices architecture pattern.

## Consequences
- Positive: Independent scaling, technology flexibility
- Negative: Increased operational complexity
```

---

## 🔗 Integration Examples

### Webhook Integration

```javascript
// Send architecture change notification
const webhook = {
  event: 'architecture.updated',
  project: 'ecommerce-platform',
  changes: ['Added payment service', 'Updated API gateway']
};

await fetch('http://rabbitmq:15672/api/exchanges/archiops/webhook', {
  method: 'POST',
  body: JSON.stringify(webhook)
});
```

---

Each example includes:
- Complete source code
- Configuration files
- Step-by-step instructions
- Best practices
- Common pitfalls to avoid

**Start with any example and customize for your architecture needs!** 🏗️
