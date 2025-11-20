# Data Product Creation

Complete data product lifecycle demonstration including schema creation, quality validation, and catalog registration.

## Overview

This example shows how to create a production-ready data product following data mesh principles:

1. **Domain Ownership**: Sales domain owns sales-monthly-metrics
2. **Data as Product**: Includes schema, quality SLOs, documentation
3. **Self-Serve**: Automated creation and registration
4. **Federated Governance**: Quality validation and catalog registration

## Quick Start

### 1. Start DataMeshOps Stack

```bash
cd ../../
docker-compose up -d postgres atlas amundsen datahub
```

Wait for services to be ready (~2 minutes):
```bash
# Check Atlas
curl http://localhost:21000

# Check DataHub
curl http://localhost:9002
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Demo

```bash
python create_product.py
```

## What It Does

### 1. Schema Creation
Creates PostgreSQL schema and table based on `data-product.yaml`:

```sql
CREATE SCHEMA sales;

CREATE TABLE sales.sales_monthly_metrics (
    month DATE NOT NULL,
    region VARCHAR NOT NULL,
    category VARCHAR NOT NULL,
    revenue DECIMAL NOT NULL,
    orders INTEGER NOT NULL,
    customers INTEGER NOT NULL,
    _created_at TIMESTAMP,
    _updated_at TIMESTAMP
);
```

### 2. Sample Data Generation
Generates 100 rows of sample sales data:
- 3 regions (NA, EU, APAC)
- 4 categories (Electronics, Clothing, Food, Books)
- 12 months of data (2024)
- Random but realistic metrics

### 3. Quality Validation
Validates against SLOs defined in config:

**Completeness Check**:
```python
# All required fields must be present (99% threshold)
for column in required_columns:
    assert non_null_count / total_count >= 0.99
```

**Accuracy Checks**:
```python
# Revenue must be positive
assert revenue >= 0

# Orders must be positive
assert orders >= 0

# Customers must be positive
assert customers >= 0

# Region must be valid
assert region IN ('NA', 'EU', 'APAC')
```

### 4. Catalog Registration
Registers the data product in Apache Atlas:

```python
entity = {
    "typeName": "DataSet",
    "attributes": {
        "name": "sales.sales-monthly-metrics",
        "qualifiedName": "sales.sales-monthly-metrics@cluster",
        "description": "Monthly sales metrics...",
        "owner": "sales-analytics@company.com",
        "dataType": "parquet"
    },
    "classifications": ["DataProduct", "Domain_sales"]
}
```

### 5. Metadata Storage
Saves product metadata for discovery:

```python
DataProductMetadata(
    name="sales-monthly-metrics",
    domain="sales",
    version="1.0.0",
    owner_team="sales-analytics",
    owner_email="sales-analytics@company.com",
    description="...",
    schema_location="s3://data-products/sales/monthly-metrics/"
)
```

## Example Output

```
============================================================
Publishing Data Product: sales/sales-monthly-metrics
============================================================

📦 Initialized data product: sales/sales-monthly-metrics v1.0.0
🗄️  Creating schema for sales-monthly-metrics
✅ Schema created: sales.sales_monthly_metrics
📊 Loading sample data (100 rows)
✅ Loaded 100 rows
🔍 Validating data quality
✅ Accuracy check passed: revenue >= 0
✅ Accuracy check passed: orders >= 0
✅ Accuracy check passed: customers >= 0
✅ Accuracy check passed: region IN ('NA', 'EU', 'APAC')
✅ All quality checks passed
📋 Registering in Apache Atlas
✅ Registered in Atlas
💾 Saving metadata
✅ Metadata saved

============================================================
Publication Complete
============================================================

Publication Results:
============================================================
✅ Schema: success
✅ Data: success
✅ Quality: passed
✅ Atlas: success
✅ Metadata: success

============================================================
Access the data product:
============================================================
Database: postgresql://datamesh:datamesh@localhost:5433/products
Table: sales.sales_monthly_metrics
Atlas: http://localhost:21000
============================================================
```

## Querying the Data Product

### Using psql

```bash
docker exec -it datameshops-product-db psql -U datamesh -d products

# Query the data
SELECT 
    month,
    region,
    SUM(revenue) as total_revenue,
    SUM(orders) as total_orders
FROM sales.sales_monthly_metrics
GROUP BY month, region
ORDER BY month DESC, total_revenue DESC;
```

### Using Python

```python
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://datamesh:datamesh@localhost:5433/products')

# Read data product
df = pd.read_sql('SELECT * FROM sales.sales_monthly_metrics', engine)

# Analyze
revenue_by_region = df.groupby('region')['revenue'].sum()
print(revenue_by_region)
```

### Using Trino (Federated Query)

```sql
-- Query across multiple data products
SELECT 
    s.region,
    s.revenue,
    c.customer_count
FROM sales.sales_monthly_metrics s
JOIN customer.regional_stats c
    ON s.region = c.region
WHERE s.month = DATE '2024-01-01';
```

## Data Product Configuration

### Minimal Example

```yaml
# minimal-product.yaml
name: my-data-product
domain: my-domain
version: 1.0.0

owner:
  team: my-team
  email: team@company.com

schema:
  type: parquet
  location: s3://products/my-domain/my-product/
  columns:
    - name: id
      type: string
    - name: value
      type: decimal

quality:
  completeness: 99.0
  accuracy_checks:
    - value >= 0
```

### Full Featured Example

See `data-product.yaml` for complete configuration including:
- Detailed schema with descriptions
- Quality SLOs (freshness, completeness, accuracy)
- Access control policies
- Lineage tracking
- Documentation links
- Tags and classifications

## Advanced Usage

### Custom Data Loading

```python
# Load from CSV
df = pd.read_csv('sales_data.csv')
product.publish(engine, df)

# Load from Parquet
df = pd.read_parquet('s3://raw-data/sales/')
product.publish(engine, df)

# Load from API
response = requests.get('https://api.example.com/sales')
df = pd.DataFrame(response.json())
product.publish(engine, df)
```

### Incremental Updates

```python
# Update existing data product
product = DataProduct(config_path='data-product.yaml')

# Load new data
new_data = pd.read_csv('new_sales.csv')

# Append to existing table
new_data.to_sql(
    'sales_monthly_metrics',
    engine,
    schema='sales',
    if_exists='append',
    index=False
)

# Re-validate quality
quality_results = product.validate_quality(engine)
```

### Version Management

```python
# Create new version
config = load_config('data-product.yaml')
config['version'] = '2.0.0'

# Add new column to schema
config['schema']['columns'].append({
    'name': 'profit_margin',
    'type': 'decimal',
    'description': 'Profit margin percentage'
})

# Publish new version
product_v2 = DataProduct(config_dict=config)
product_v2.publish(engine, updated_data)
```

## Integration with Data Mesh Stack

### Apache Atlas

View in Atlas UI:
1. Open http://localhost:21000
2. Login: admin/admin
3. Search for "sales-monthly-metrics"
4. View lineage, schema, classifications

### Amundsen

```python
# Index in Amundsen
from amundsen import AmundsenClient

client = AmundsenClient('http://localhost:5000')
client.index_table(
    database='products',
    cluster='default',
    schema='sales',
    table='sales_monthly_metrics'
)
```

### DataHub

Access DataHub:
1. Open http://localhost:9002
2. Login: datahub/datahub
3. Search for data products
4. View documentation and metadata

## Quality Monitoring

### Continuous Validation

```python
# Run quality checks on schedule
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()

@scheduler.scheduled_job('cron', hour=2)  # Daily at 2 AM
def validate_quality():
    product = DataProduct(config_path='data-product.yaml')
    results = product.validate_quality(engine)
    
    if not results['passed']:
        send_alert(results)

scheduler.start()
```

### Custom Quality Rules

```python
# Add custom validation
def validate_revenue_trend(engine, table):
    """Ensure revenue is growing month-over-month"""
    query = """
        WITH monthly AS (
            SELECT 
                month,
                SUM(revenue) as total_revenue,
                LAG(SUM(revenue)) OVER (ORDER BY month) as prev_revenue
            FROM sales.sales_monthly_metrics
            GROUP BY month
        )
        SELECT COUNT(*)
        FROM monthly
        WHERE total_revenue < prev_revenue
    """
    
    result = engine.execute(query).scalar()
    
    if result > 2:  # Allow max 2 months of decline
        raise ValueError(f"Revenue declining for {result} months")
```

## Troubleshooting

### Database Connection Issues

```bash
# Test connection
docker exec -it datameshops-product-db psql -U datamesh -d products -c "SELECT 1"

# Check logs
docker logs datameshops-product-db
```

### Atlas Registration Fails

```bash
# Verify Atlas is running
curl http://localhost:21000/api/atlas/admin/version

# Check credentials
curl -u admin:admin http://localhost:21000/api/atlas/v2/types/typedefs

# View logs
docker logs datameshops-atlas
```

### Quality Validation Fails

```python
# Debug quality checks
results = product.validate_quality(engine)

# View detailed results
for check in results['checks']:
    print(f"{check['type']}: {check}")
    if not check['passed']:
        print(f"  Failed: {check}")
```

## Resources

- [Data Mesh Principles](https://martinfowler.com/articles/data-mesh-principles.html)
- [Apache Atlas Documentation](https://atlas.apache.org/)
- [Data Product Specification](https://github.com/datamesh-architecture/data-product-specification)
- [Great Expectations](https://greatexpectations.io/) - Advanced data quality
