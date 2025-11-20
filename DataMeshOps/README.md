# DataMeshOps - Data Mesh Operations

Complete Data Mesh architecture stack implementing decentralized data ownership with domain-driven data products.

## Stack Components

### Data Catalogs & Discovery
- **Apache Atlas** (port 21000) - Enterprise data governance and metadata management
- **Amundsen** (port 5000) - Data discovery and metadata platform
- **DataHub** (ports 8080, 9002) - Modern metadata platform for data observability

### Metadata & Schema Management
- **Neo4j** (ports 7474, 7687) - Graph database for metadata relationships
- **Elasticsearch** (ports 9200, 9300) - Search and indexing
- **Schema Registry** (port 8081) - Schema versioning and data contracts
- **Hive Metastore** (port 9083) - Metadata for data lakes

### Data Infrastructure
- **Apache Kafka** (port 9092) - Event streaming for data products
- **Trino** (port 8082) - Distributed SQL query engine across domains
- **MinIO** (ports 9000, 9001) - S3-compatible object storage
- **PostgreSQL** (port 5432) - Sample data product database

### Observability
- **Prometheus** (port 9090) - Metrics collection
- **Grafana** (port 3000) - Dashboards and visualization

## Quick Start

```bash
# Start the data mesh stack
docker-compose up -d

# View services
docker-compose ps

# Check logs
docker-compose logs -f

# Stop services
docker-compose down
```

## Service Access

| Service | URL | Credentials |
|---------|-----|-------------|
| Atlas | http://localhost:21000 | admin / admin |
| Amundsen | http://localhost:5000 | - |
| DataHub | http://localhost:9002 | - |
| Neo4j Browser | http://localhost:7474 | neo4j / neo4j123 |
| Elasticsearch | http://localhost:9200 | - |
| Schema Registry | http://localhost:8081 | - |
| Trino | http://localhost:8082 | - |
| MinIO Console | http://localhost:9001 | minioadmin / minioadmin |
| Prometheus | http://localhost:9090 | - |
| Grafana | http://localhost:3000 | admin / admin |

## Data Mesh Principles

### 1. Domain-Oriented Ownership
Each business domain owns its data products.

### 2. Data as a Product
Treat data with product thinking - discoverable, addressable, trustworthy, secure.

### 3. Self-Serve Data Infrastructure
Platform that enables domain teams to build data products easily.

### 4. Federated Computational Governance
Automated governance policies across domains.

## Use Cases

### Creating Data Products

```python
# Register a data product in DataHub
from datahub.emitter.mce_builder import make_dataset_urn
from datahub.emitter.rest_emitter import DatahubRestEmitter

emitter = DatahubRestEmitter("http://localhost:8080")

dataset_urn = make_dataset_urn(
    platform="postgres",
    name="customer_360",
    env="PROD"
)

# Define data product metadata
metadata = {
    "description": "Complete customer view across all touchpoints",
    "owners": ["customer-domain-team"],
    "tags": ["customer", "360-view", "product"],
    "schema": {...}
}
```

### Data Product Discovery

```bash
# Search in Amundsen
curl http://localhost:5000/api/search/v2 \
  -d '{"term": "customer", "resource": "table"}'

# Query DataHub GraphQL API
curl -X POST http://localhost:8080/api/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "{ search(input: {type: DATASET, query: \"customer\"}) { searchResults { entity { urn } } } }"}'
```

### Cross-Domain Queries with Trino

```sql
-- Query across multiple domains
SELECT 
  c.customer_id,
  c.name,
  o.order_count,
  s.support_tickets
FROM 
  sales_domain.customers c
JOIN 
  orders_domain.order_summary o ON c.customer_id = o.customer_id
LEFT JOIN 
  support_domain.ticket_summary s ON c.customer_id = s.customer_id
WHERE 
  c.segment = 'enterprise';
```

### Data Contracts with Schema Registry

```bash
# Register schema for data product
curl -X POST http://localhost:8081/subjects/customer-product-value/versions \
  -H "Content-Type: application/vnd.schemaregistry.v1+json" \
  -d '{
    "schema": "{\"type\":\"record\",\"name\":\"Customer\",\"fields\":[{\"name\":\"customer_id\",\"type\":\"string\"},{\"name\":\"email\",\"type\":\"string\"},{\"name\":\"segment\",\"type\":\"string\"}]}"
  }'

# Validate compatibility
curl -X POST http://localhost:8081/compatibility/subjects/customer-product-value/versions/latest \
  -H "Content-Type: application/vnd.schemaregistry.v1+json" \
  -d '{"schema": "..."}'
```

## Data Product Template

### Structure

```
data-product-customer-360/
├── README.md                 # Product documentation
├── schema/                   # Data contracts
│   ├── schema.avro
│   └── schema.json
├── pipeline/                 # ETL/ELT code
│   ├── ingestion.py
│   └── transformation.sql
├── tests/                    # Data quality tests
│   ├── test_schema.py
│   └── test_quality.py
├── metadata/                 # Governance metadata
│   ├── ownership.yaml
│   ├── sla.yaml
│   └── tags.yaml
└── docs/                     # User documentation
    ├── usage.md
    └── api.md
```

### Metadata Example

```yaml
# metadata/ownership.yaml
product:
  name: customer-360
  domain: customer
  version: 2.1.0
  description: Complete customer view across all touchpoints
  
ownership:
  team: customer-experience-team
  email: customer-team@company.com
  slack: #customer-data
  
sla:
  freshness: 1h
  availability: 99.9%
  completeness: 95%
  
access:
  public: false
  consumers:
    - marketing-domain
    - sales-domain
  
quality:
  - rule: no_null_customer_id
    severity: critical
  - rule: valid_email_format
    severity: high
```

## Governance Automation

### Data Quality Checks

```python
# Great Expectations data quality
import great_expectations as ge

df = ge.read_csv("customer_data.csv")

# Define expectations
df.expect_column_values_to_not_be_null("customer_id")
df.expect_column_values_to_be_unique("customer_id")
df.expect_column_values_to_match_regex("email", r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

# Validate
results = df.validate()
```

### Automated Lineage Tracking

```python
# Track data lineage in Atlas
from apache_atlas.client.base_client import AtlasClient

client = AtlasClient("http://localhost:21000", ("admin", "admin"))

# Create lineage relationship
lineage = {
    "typeName": "Process",
    "attributes": {
        "name": "customer_360_pipeline",
        "inputs": [
            {"typeName": "DataSet", "uniqueAttributes": {"qualifiedName": "sales_db.customers"}},
            {"typeName": "DataSet", "uniqueAttributes": {"qualifiedName": "support_db.tickets"}}
        ],
        "outputs": [
            {"typeName": "DataSet", "uniqueAttributes": {"qualifiedName": "analytics_db.customer_360"}}
        ]
    }
}
```

### Policy Enforcement

```yaml
# Define access policies
policies:
  - name: pii_protection
    description: Protect PII fields
    rules:
      - field: email
        encryption: required
        masking: email
      - field: ssn
        encryption: required
        access: restricted
        
  - name: gdpr_compliance
    description: GDPR right to be forgotten
    rules:
      - retention: 2y
      - deletion_process: automated
```

## Domain Architecture

### Sample Domain: Customer Domain

```
Customer Domain
├── Data Products
│   ├── customer-360           (Unified customer view)
│   ├── customer-segments      (ML-based segmentation)
│   └── customer-churn-risk    (Churn prediction)
├── Infrastructure
│   ├── PostgreSQL cluster
│   ├── Kafka topics
│   └── S3 buckets (MinIO)
└── APIs
    ├── REST API (customer data)
    ├── GraphQL API (queries)
    └── gRPC API (real-time)
```

## Federated Query Examples

### Setup Trino Catalogs

Create `trino/etc/catalog/postgres.properties`:

```properties
connector.name=postgresql
connection-url=jdbc:postgresql://data-product-db:5432/dataproducts
connection-user=dataproduct
connection-password=dataproduct
```

Create `trino/etc/catalog/minio.properties`:

```properties
connector.name=hive
hive.metastore.uri=thrift://hive-metastore:9083
hive.s3.endpoint=http://minio:9000
hive.s3.path-style-access=true
hive.s3.aws-access-key=minioadmin
hive.s3.aws-secret-key=minioadmin
```

### Cross-Platform Queries

```sql
-- Join data from PostgreSQL and S3 (via Hive)
SELECT 
  p.customer_id,
  p.email,
  s.total_spend
FROM 
  postgres.public.customers p
JOIN 
  minio.analytics.customer_metrics s 
ON 
  p.customer_id = s.customer_id
WHERE 
  s.total_spend > 10000;
```

## Data Product Lifecycle

### 1. Design Phase
- Define domain boundaries
- Identify data consumers
- Design data contracts
- Plan SLAs

### 2. Build Phase
- Implement pipelines
- Set up quality checks
- Configure lineage tracking
- Write documentation

### 3. Publish Phase
- Register in data catalog
- Publish schemas
- Set access controls
- Announce to consumers

### 4. Maintain Phase
- Monitor SLAs
- Track usage metrics
- Update documentation
- Evolve schema versions

### 5. Retire Phase
- Notify consumers
- Migrate dependencies
- Archive data
- Remove from catalog

## Monitoring & Observability

### Data Product Metrics

```promql
# Query freshness SLA
data_product_freshness_seconds{product="customer-360"} < 3600

# Quality score
data_product_quality_score{product="customer-360"} > 0.95

# Usage metrics
sum(rate(data_product_queries_total{product="customer-360"}[5m]))
```

### Dashboards

Create Grafana dashboards for:
- Data product health
- Domain metrics
- Consumer usage
- SLA compliance
- Data quality scores

## Migration Strategy

### From Centralized to Data Mesh

1. **Identify Domains**: Map organizational domains
2. **Prioritize Products**: Start with high-value data products
3. **Build Platform**: Deploy self-serve infrastructure
4. **Migrate Incrementally**: One domain at a time
5. **Enable Discovery**: Populate data catalogs
6. **Establish Governance**: Automate policies
7. **Train Teams**: Domain ownership training

## Best Practices

1. **Start Small**: Begin with 2-3 domains
2. **Product Thinking**: Treat data as a first-class product
3. **Clear Contracts**: Use schema registry for all products
4. **Automated Quality**: Build quality into pipelines
5. **Rich Metadata**: Document everything in catalogs
6. **Federated Governance**: Automate policy enforcement
7. **Consumer Focus**: Design for data consumers
8. **Evolutionary Architecture**: Allow schema evolution
9. **Measure Everything**: Track metrics religiously
10. **Domain Autonomy**: Trust domain teams

## Resource Requirements

### Minimum
- CPU: 8 cores
- RAM: 16 GB
- Disk: 100 GB

### Recommended
- CPU: 16+ cores
- RAM: 32 GB
- Disk: 500 GB SSD

## Troubleshooting

### Atlas Not Starting
```bash
# Check database connection
docker-compose logs atlas-postgres

# Increase memory
# Edit docker-compose.yml: ATLAS_OPTS=-Xmx4096m
```

### DataHub Issues
```bash
# Check GMS logs
docker-compose logs datahub-gms

# Reindex Elasticsearch
curl -X POST http://localhost:8080/gms/operations?action=restoreIndices
```

### Trino Query Failures
```bash
# Check catalog configuration
docker exec datameshops-trino cat /etc/trino/catalog/postgres.properties

# View query details
curl http://localhost:8082/v1/query/{queryId}
```

## License

Components use various open source licenses (Apache 2.0, MIT, etc.). Review individual project licenses.
