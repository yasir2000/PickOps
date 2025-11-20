# DataMeshOps Examples

Production-ready data mesh implementations demonstrating domain-oriented data products, federated governance, and self-serve data infrastructure.

## Available Examples

### 1. [Data Product Creation](./data-product-creation/)
Complete data product lifecycle:
- Domain-driven data modeling
- Data quality validation
- Schema evolution and versioning
- Metadata registration in catalogs
- Access control and governance
- SLO monitoring and observability

**Technologies**: Apache Atlas, Amundsen, DataHub, PostgreSQL, Kafka

### 2. [Federated Data Governance](./federated-governance/)
Decentralized governance framework:
- Domain ownership policies
- Data quality rules and monitoring
- Automated compliance checking
- Cross-domain data sharing agreements
- Lineage tracking and impact analysis

**Technologies**: Apache Atlas, Great Expectations, dbt, Airflow

### 3. [Self-Serve Data Platform](./self-serve-platform/)
Enable domain teams with self-service:
- Data product templates
- Automated infrastructure provisioning
- Data pipeline scaffolding
- Monitoring and alerting setup
- Documentation generation

**Technologies**: Terraform, dbt, Airflow, Amundsen, DataHub

### 4. [Cross-Domain Analytics](./cross-domain-analytics/)
Federated query and analytics:
- Trino-based query federation
- Cross-domain joins
- Data product discovery
- Query optimization
- Result caching

**Technologies**: Trino, Hive Metastore, MinIO, Iceberg

### 5. [Data Lineage & Discovery](./lineage-discovery/)
End-to-end data lineage:
- Automated lineage extraction
- Interactive lineage visualization
- Impact analysis for changes
- Data catalog integration
- Search and discovery

**Technologies**: Apache Atlas, Amundsen, DataHub, Neo4j, OpenLineage

## Getting Started

1. **Start DataMeshOps stack**:
```bash
cd DataMeshOps
docker-compose up -d
```

2. **Access UIs**:
   - **Apache Atlas**: http://localhost:21000 (admin/admin)
   - **Amundsen**: http://localhost:5000
   - **DataHub**: http://localhost:9002 (datahub/datahub)
   - **Trino**: http://localhost:8082
   - **MinIO**: http://localhost:9001 (minioadmin/minioadmin)

3. **Choose an example**:
```bash
cd examples/data-product-creation
```

4. **Follow example README** for specific setup

## Data Mesh Principles

### 1. Domain Ownership
```
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│  Sales Domain   │  │ Customer Domain │  │ Product Domain  │
│                 │  │                 │  │                 │
│ - Sales Data    │  │ - Customer Data │  │ - Product Data  │
│ - Team Owns     │  │ - Team Owns     │  │ - Team Owns     │
│ - Full Lifecycle│  │ - Full Lifecycle│  │ - Full Lifecycle│
└─────────────────┘  └─────────────────┘  └─────────────────┘
```

### 2. Data as a Product
Each data product includes:
- **Discovery**: Searchable metadata in catalogs
- **Understanding**: Clear documentation and schemas
- **Trust**: Quality SLOs and monitoring
- **Access**: Self-serve APIs and access control
- **Interoperability**: Standard formats and protocols

### 3. Self-Serve Data Infrastructure
Platform capabilities:
- Data product templates
- Automated provisioning
- CI/CD pipelines
- Monitoring and alerting
- Cost tracking

### 4. Federated Computational Governance
- Domain-level policies
- Global standards
- Automated compliance
- Decentralized enforcement
- Lineage-based impact

## Data Product Template

```yaml
# data-product.yaml
name: sales-monthly-metrics
domain: sales
version: 1.0.0

description: |
  Monthly aggregated sales metrics by region and product category
  
owner:
  team: sales-analytics
  email: sales-analytics@company.com
  slack: #sales-analytics

schema:
  type: parquet
  location: s3://data-products/sales/monthly-metrics/
  columns:
    - name: month
      type: date
      description: Reporting month
    - name: region
      type: string
      description: Sales region
    - name: revenue
      type: decimal
      description: Total revenue in USD

quality:
  freshness_sla: 24h
  completeness: 99.9%
  accuracy_checks:
    - revenue >= 0
    - region IN ('NA', 'EU', 'APAC')

access:
  public: false
  allowed_domains:
    - finance
    - executive
  
catalog:
  - atlas
  - amundsen
  - datahub
```

## Common Patterns

### Data Product Registration

```python
from datamesh import DataProduct, Catalog

# Create data product
product = DataProduct(
    name="customer-360",
    domain="customer",
    owner="customer-team@company.com"
)

# Add schema
product.add_schema(
    format="parquet",
    location="s3://products/customer-360/",
    schema=customer_schema
)

# Set quality SLOs
product.set_slo(
    freshness="1h",
    completeness=99.9,
    accuracy=["email is not null", "age > 0"]
)

# Register in catalogs
Catalog.register(product, ["atlas", "amundsen", "datahub"])
```

### Federated Queries

```sql
-- Query across domains using Trino
SELECT 
    s.month,
    s.region,
    s.revenue,
    c.customer_count,
    p.product_launches
FROM sales.monthly_metrics s
JOIN customer.regional_stats c
    ON s.region = c.region 
    AND s.month = c.month
JOIN product.launch_calendar p
    ON s.month = p.month
WHERE s.month >= date '2024-01-01';
```

### Data Quality Validation

```python
import great_expectations as ge

# Load data product
df = ge.read_parquet("s3://products/sales-metrics/")

# Validate expectations
df.expect_column_values_to_not_be_null("revenue")
df.expect_column_values_to_be_between("revenue", min_value=0)
df.expect_column_distinct_values_to_be_in_set(
    "region", 
    ["NA", "EU", "APAC"]
)

# Save validation results
results = df.validate()
```

### Lineage Tracking

```python
from openlineage import OpenLineageClient, RunEvent

client = OpenLineageClient(url="http://localhost:21000")

# Track pipeline run
event = RunEvent(
    eventType="START",
    job=Job(namespace="sales", name="monthly-metrics-pipeline"),
    inputs=[
        Dataset(namespace="raw", name="transactions"),
        Dataset(namespace="raw", name="returns")
    ],
    outputs=[
        Dataset(namespace="products", name="sales-monthly-metrics")
    ]
)

client.emit(event)
```

## Architecture Patterns

### Centralized Catalog, Decentralized Data

```
                    ┌──────────────────┐
                    │  Data Catalogs   │
                    │  (Atlas, etc.)   │
                    └────────┬─────────┘
                             │
        ┌───────────┬────────┴────────┬───────────┐
        │           │                 │           │
┌───────▼─────┐ ┌──▼──────────┐ ┌────▼──────┐ ┌─▼────────┐
│   Sales     │ │  Customer   │ │  Product  │ │ Finance  │
│   Domain    │ │   Domain    │ │  Domain   │ │  Domain  │
│             │ │             │ │           │ │          │
│ - Own Data  │ │ - Own Data  │ │ - Own Data│ │- Own Data│
│ - Own Infra │ │ - Own Infra │ │ - Own     │ │- Own     │
└─────────────┘ └─────────────┘ └───────────┘ └──────────┘
```

### Event-Driven Data Products

```
Domain A                Domain B                Domain C
┌────────┐             ┌────────┐             ┌────────┐
│ Source │─┐           │        │             │        │
└────────┘ │           │        │             │        │
           ▼           │        │             │        │
        ┌─────┐        │        │             │        │
        │Kafka│────────┼───────►│ Subscribe  │         │
        └─────┘        │        │      │      │        │
           ▲           │        │      ▼      │        │
           │           │        │  ┌──────┐   │        │
           │           │        │  │Process   │        │
           └───────────┼────────┼──┤      │   │        │
                       │        │  └──┬───┘   │        │
                       │        │     │       │        │
                       │        │     ▼       │        │
                       └────────┘  ┌─────┐    │        │
                                   │Kafka│────┼───────►│
                                   └─────┘    │        │
                                              └────────┘
```

## Best Practices

### 1. Data Product Design
- Clear ownership and SLOs
- Semantic layer for business terms
- Versioning strategy
- Backward compatibility
- Documentation as code

### 2. Quality and Trust
- Automated quality checks
- SLO monitoring and alerting
- Data profiling and drift detection
- Lineage for troubleshooting
- Transparent quality scores

### 3. Governance
- Domain-level policies
- Automated compliance checks
- Lineage-based impact analysis
- Access control and audit logs
- Cost allocation by domain

### 4. Platform Capabilities
- Self-serve provisioning
- Standard templates
- CI/CD automation
- Monitoring and observability
- Cost optimization

## Prerequisites

- Docker and Docker Compose
- Basic SQL knowledge
- Understanding of data warehousing concepts
- Python 3.8+ for examples

## Resources

- [Data Mesh Book - Zhamak Dehghani](https://www.oreilly.com/library/view/data-mesh/9781492092384/)
- [Apache Atlas Documentation](https://atlas.apache.org/)
- [Amundsen Documentation](https://www.amundsen.io/)
- [DataHub Documentation](https://datahubproject.io/)
- [Trino Documentation](https://trino.io/docs/current/)
