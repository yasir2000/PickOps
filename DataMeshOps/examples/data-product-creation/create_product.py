"""
Data Product Creation and Registration
Demonstrates: Data product lifecycle, catalog registration, quality validation
"""

import os
import json
import yaml
from datetime import datetime
from typing import Dict, List, Optional
import pandas as pd
from sqlalchemy import create_engine, Column, String, Integer, Float, DateTime, MetaData, Table
from sqlalchemy.orm import declarative_base, sessionmaker
import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration
ATLAS_URL = os.getenv('ATLAS_URL', 'http://localhost:21000')
ATLAS_USER = os.getenv('ATLAS_USER', 'admin')
ATLAS_PASS = os.getenv('ATLAS_PASS', 'admin')

DATAHUB_URL = os.getenv('DATAHUB_URL', 'http://localhost:9002')
DATAHUB_TOKEN = os.getenv('DATAHUB_TOKEN', '')

DB_URL = os.getenv('DB_URL', 'postgresql://datamesh:datamesh@localhost:5433/products')

Base = declarative_base()

class DataProductMetadata(Base):
    """Data product metadata storage"""
    __tablename__ = 'data_products'

    name = Column(String, primary_key=True)
    domain = Column(String, nullable=False)
    version = Column(String, nullable=False)
    owner_team = Column(String, nullable=False)
    owner_email = Column(String, nullable=False)
    description = Column(String)
    schema_location = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class DataProduct:
    """Data Product representation"""

    def __init__(self, config_path: str = None, config_dict: dict = None):
        if config_path:
            with open(config_path, 'r') as f:
                self.config = yaml.safe_load(f)
        elif config_dict:
            self.config = config_dict
        else:
            raise ValueError("Either config_path or config_dict must be provided")

        self.name = self.config['name']
        self.domain = self.config['domain']
        self.version = self.config['version']

        logger.info(f"📦 Initialized data product: {self.domain}/{self.name} v{self.version}")

    def create_schema(self, engine):
        """Create database schema for data product"""

        logger.info(f"🗄️  Creating schema for {self.name}")

        # Parse schema definition
        schema_def = self.config['schema']

        metadata = MetaData()

        columns = []
        for col in schema_def['columns']:
            col_type = {
                'string': String,
                'integer': Integer,
                'float': Float,
                'decimal': Float,
                'date': DateTime,
                'timestamp': DateTime
            }.get(col['type'], String)

            columns.append(Column(col['name'], col_type))

        # Add metadata columns
        columns.extend([
            Column('_created_at', DateTime, default=datetime.utcnow),
            Column('_updated_at', DateTime, default=datetime.utcnow)
        ])

        table = Table(
            self.name.replace('-', '_'),
            metadata,
            *columns,
            schema=self.domain
        )

        # Create schema and table
        with engine.connect() as conn:
            conn.execute(f"CREATE SCHEMA IF NOT EXISTS {self.domain}")
            conn.commit()

        metadata.create_all(engine)

        logger.info(f"✅ Schema created: {self.domain}.{self.name}")

        return table

    def load_sample_data(self, engine, sample_data: pd.DataFrame):
        """Load sample data into product table"""

        logger.info(f"📊 Loading sample data ({len(sample_data)} rows)")

        table_name = self.name.replace('-', '_')
        sample_data.to_sql(
            table_name,
            engine,
            schema=self.domain,
            if_exists='append',
            index=False
        )

        logger.info(f"✅ Loaded {len(sample_data)} rows")

    def validate_quality(self, engine) -> Dict:
        """Validate data quality against SLOs"""

        logger.info(f"🔍 Validating data quality")

        quality_config = self.config.get('quality', {})
        table_name = f"{self.domain}.{self.name.replace('-', '_')}"

        results = {
            'passed': True,
            'checks': []
        }

        with engine.connect() as conn:
            # Check completeness
            completeness = quality_config.get('completeness', 100)
            for col in self.config['schema']['columns']:
                if col.get('nullable', True):
                    continue

                query = f"""
                    SELECT
                        COUNT(*) as total,
                        COUNT({col['name']}) as non_null
                    FROM {table_name}
                """
                result = conn.execute(query).fetchone()

                actual_completeness = (result.non_null / result.total * 100) if result.total > 0 else 0
                passed = actual_completeness >= completeness

                results['checks'].append({
                    'type': 'completeness',
                    'column': col['name'],
                    'expected': completeness,
                    'actual': actual_completeness,
                    'passed': passed
                })

                if not passed:
                    results['passed'] = False
                    logger.warning(f"❌ Completeness check failed for {col['name']}: "
                                 f"{actual_completeness:.2f}% < {completeness}%")

            # Check accuracy rules
            for check in quality_config.get('accuracy_checks', []):
                query = f"""
                    SELECT COUNT(*) as violations
                    FROM {table_name}
                    WHERE NOT ({check})
                """
                violations = conn.execute(query).fetchone().violations
                passed = violations == 0

                results['checks'].append({
                    'type': 'accuracy',
                    'rule': check,
                    'violations': violations,
                    'passed': passed
                })

                if not passed:
                    results['passed'] = False
                    logger.warning(f"❌ Accuracy check failed: {check} ({violations} violations)")
                else:
                    logger.info(f"✅ Accuracy check passed: {check}")

        if results['passed']:
            logger.info(f"✅ All quality checks passed")
        else:
            logger.error(f"❌ Quality validation failed")

        return results

    def register_in_atlas(self) -> bool:
        """Register data product in Apache Atlas"""

        logger.info(f"📋 Registering in Apache Atlas")

        try:
            # Create entity in Atlas
            entity = {
                "entity": {
                    "typeName": "DataSet",
                    "attributes": {
                        "name": f"{self.domain}.{self.name}",
                        "qualifiedName": f"{self.domain}.{self.name}@cluster",
                        "description": self.config.get('description', ''),
                        "owner": self.config['owner']['email'],
                        "dataType": self.config['schema']['type']
                    },
                    "classifications": [
                        {"typeName": "DataProduct"},
                        {"typeName": f"Domain_{self.domain}"}
                    ]
                }
            }

            response = requests.post(
                f"{ATLAS_URL}/api/atlas/v2/entity",
                json=entity,
                auth=(ATLAS_USER, ATLAS_PASS),
                headers={'Content-Type': 'application/json'}
            )

            if response.status_code in [200, 201]:
                logger.info(f"✅ Registered in Atlas")
                return True
            else:
                logger.error(f"❌ Atlas registration failed: {response.text}")
                return False

        except Exception as e:
            logger.error(f"❌ Atlas registration error: {str(e)}")
            return False

    def save_metadata(self, engine):
        """Save metadata to catalog database"""

        logger.info(f"💾 Saving metadata")

        Session = sessionmaker(bind=engine)
        session = Session()

        metadata = DataProductMetadata(
            name=self.name,
            domain=self.domain,
            version=self.version,
            owner_team=self.config['owner']['team'],
            owner_email=self.config['owner']['email'],
            description=self.config.get('description', ''),
            schema_location=self.config['schema']['location']
        )

        session.merge(metadata)
        session.commit()
        session.close()

        logger.info(f"✅ Metadata saved")

    def publish(self, engine, sample_data: pd.DataFrame = None) -> Dict:
        """Complete data product publication workflow"""

        logger.info(f"\n{'='*60}")
        logger.info(f"Publishing Data Product: {self.domain}/{self.name}")
        logger.info(f"{'='*60}\n")

        results = {
            'name': self.name,
            'domain': self.domain,
            'version': self.version,
            'steps': {}
        }

        # 1. Create schema
        try:
            self.create_schema(engine)
            results['steps']['schema'] = 'success'
        except Exception as e:
            logger.error(f"Schema creation failed: {str(e)}")
            results['steps']['schema'] = f'failed: {str(e)}'
            return results

        # 2. Load sample data
        if sample_data is not None:
            try:
                self.load_sample_data(engine, sample_data)
                results['steps']['data'] = 'success'
            except Exception as e:
                logger.error(f"Data loading failed: {str(e)}")
                results['steps']['data'] = f'failed: {str(e)}'

        # 3. Validate quality
        try:
            quality_results = self.validate_quality(engine)
            results['steps']['quality'] = 'passed' if quality_results['passed'] else 'failed'
            results['quality_checks'] = quality_results['checks']
        except Exception as e:
            logger.error(f"Quality validation failed: {str(e)}")
            results['steps']['quality'] = f'failed: {str(e)}'

        # 4. Register in catalogs
        try:
            atlas_success = self.register_in_atlas()
            results['steps']['atlas'] = 'success' if atlas_success else 'failed'
        except Exception as e:
            logger.error(f"Atlas registration failed: {str(e)}")
            results['steps']['atlas'] = f'failed: {str(e)}'

        # 5. Save metadata
        try:
            self.save_metadata(engine)
            results['steps']['metadata'] = 'success'
        except Exception as e:
            logger.error(f"Metadata save failed: {str(e)}")
            results['steps']['metadata'] = f'failed: {str(e)}'

        logger.info(f"\n{'='*60}")
        logger.info(f"Publication Complete")
        logger.info(f"{'='*60}\n")

        return results

def create_sample_product():
    """Create sample data product"""

    config = {
        'name': 'sales-monthly-metrics',
        'domain': 'sales',
        'version': '1.0.0',
        'description': 'Monthly aggregated sales metrics by region and product category',
        'owner': {
            'team': 'sales-analytics',
            'email': 'sales-analytics@company.com',
            'slack': '#sales-analytics'
        },
        'schema': {
            'type': 'parquet',
            'location': 's3://data-products/sales/monthly-metrics/',
            'columns': [
                {'name': 'month', 'type': 'date', 'description': 'Reporting month'},
                {'name': 'region', 'type': 'string', 'description': 'Sales region'},
                {'name': 'category', 'type': 'string', 'description': 'Product category'},
                {'name': 'revenue', 'type': 'decimal', 'description': 'Total revenue in USD'},
                {'name': 'orders', 'type': 'integer', 'description': 'Number of orders'},
                {'name': 'customers', 'type': 'integer', 'description': 'Unique customers'}
            ]
        },
        'quality': {
            'freshness_sla': '24h',
            'completeness': 99.0,
            'accuracy_checks': [
                'revenue >= 0',
                'orders >= 0',
                'customers >= 0',
                "region IN ('NA', 'EU', 'APAC')"
            ]
        },
        'access': {
            'public': False,
            'allowed_domains': ['finance', 'executive']
        },
        'catalog': ['atlas', 'amundsen', 'datahub']
    }

    return DataProduct(config_dict=config)

def generate_sample_data(n_rows: int = 100) -> pd.DataFrame:
    """Generate sample sales data"""

    import random
    from datetime import timedelta

    regions = ['NA', 'EU', 'APAC']
    categories = ['Electronics', 'Clothing', 'Food', 'Books']

    data = []
    start_date = datetime(2024, 1, 1)

    for i in range(n_rows):
        month = start_date + timedelta(days=30*random.randint(0, 11))
        data.append({
            'month': month,
            'region': random.choice(regions),
            'category': random.choice(categories),
            'revenue': round(random.uniform(10000, 100000), 2),
            'orders': random.randint(100, 1000),
            'customers': random.randint(50, 500)
        })

    return pd.DataFrame(data)

def main():
    """Run data product creation demo"""

    logger.info("=" * 60)
    logger.info("Data Product Creation Demo")
    logger.info("=" * 60)

    # Initialize database
    engine = create_engine(DB_URL)
    Base.metadata.create_all(engine)

    # Create data product
    product = create_sample_product()

    # Generate sample data
    sample_data = generate_sample_data(100)

    # Publish data product
    results = product.publish(engine, sample_data)

    # Print results
    logger.info(f"\n{'='*60}")
    logger.info("Publication Results:")
    logger.info(f"{'='*60}")
    for step, status in results['steps'].items():
        emoji = '✅' if status == 'success' or status == 'passed' else '❌'
        logger.info(f"{emoji} {step.title()}: {status}")

    logger.info(f"\n{'='*60}")
    logger.info("Access the data product:")
    logger.info(f"{'='*60}")
    logger.info(f"Database: {DB_URL}")
    logger.info(f"Table: {product.domain}.{product.name.replace('-', '_')}")
    logger.info(f"Atlas: {ATLAS_URL}")
    logger.info(f"{'='*60}")

if __name__ == "__main__":
    # Install: pip install pandas sqlalchemy psycopg2-binary pyyaml requests
    main()
