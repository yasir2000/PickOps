"""
Airflow ETL Pipeline Example
Demonstrates: DAG creation, task dependencies, data extraction, transformation, loading
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
import pandas as pd
import requests
import json

# Default arguments
default_args = {
    'owner': 'dataops',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

def extract_api_data(**context):
    """Extract data from API"""
    print("📥 Extracting data from API...")

    # Example: fetch user data from JSONPlaceholder API
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    data = response.json()

    # Save to XCom for next task
    context['ti'].xcom_push(key='raw_data', value=data)

    print(f"✅ Extracted {len(data)} records")
    return len(data)

def transform_data(**context):
    """Transform extracted data"""
    print("🔄 Transforming data...")

    # Get data from previous task
    raw_data = context['ti'].xcom_pull(key='raw_data', task_ids='extract_data')

    # Convert to DataFrame
    df = pd.DataFrame(raw_data)

    # Transformations
    df['full_name'] = df['name']
    df['email_domain'] = df['email'].apply(lambda x: x.split('@')[1])
    df['city'] = df['address'].apply(lambda x: x['city'])
    df['company_name'] = df['company'].apply(lambda x: x['name'])

    # Select relevant columns
    df_clean = df[['id', 'full_name', 'email', 'email_domain', 'city', 'company_name', 'phone']]

    # Data quality checks
    assert df_clean['id'].is_unique, "IDs must be unique"
    assert df_clean['email'].notna().all(), "Email cannot be null"

    # Save transformed data
    transformed_data = df_clean.to_dict('records')
    context['ti'].xcom_push(key='transformed_data', value=transformed_data)

    print(f"✅ Transformed {len(transformed_data)} records")
    return len(transformed_data)

def load_to_database(**context):
    """Load data into PostgreSQL"""
    print("💾 Loading data to database...")

    # Get transformed data
    data = context['ti'].xcom_pull(key='transformed_data', task_ids='transform_data')

    # Get database connection
    pg_hook = PostgresHook(postgres_conn_id='postgres_default')
    conn = pg_hook.get_conn()
    cursor = conn.cursor()

    # Insert data
    insert_query = """
        INSERT INTO users (id, full_name, email, email_domain, city, company_name, phone)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (id) DO UPDATE SET
            full_name = EXCLUDED.full_name,
            email = EXCLUDED.email,
            email_domain = EXCLUDED.email_domain,
            city = EXCLUDED.city,
            company_name = EXCLUDED.company_name,
            phone = EXCLUDED.phone;
    """

    for record in data:
        cursor.execute(insert_query, (
            record['id'],
            record['full_name'],
            record['email'],
            record['email_domain'],
            record['city'],
            record['company_name'],
            record['phone']
        ))

    conn.commit()
    cursor.close()
    conn.close()

    print(f"✅ Loaded {len(data)} records to database")
    return len(data)

def generate_report(**context):
    """Generate data quality report"""
    print("📊 Generating report...")

    pg_hook = PostgresHook(postgres_conn_id='postgres_default')

    # Query statistics
    stats_query = """
        SELECT
            COUNT(*) as total_users,
            COUNT(DISTINCT email_domain) as unique_domains,
            COUNT(DISTINCT city) as unique_cities,
            COUNT(DISTINCT company_name) as unique_companies
        FROM users;
    """

    df = pg_hook.get_pandas_df(stats_query)

    # Create report
    report = {
        'pipeline_run': context['ds'],
        'statistics': df.to_dict('records')[0],
        'status': 'SUCCESS'
    }

    # Save report
    report_path = f"/tmp/etl_report_{context['ds']}.json"
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)

    print(f"✅ Report saved to {report_path}")
    print(json.dumps(report, indent=2))

    return report_path

def data_quality_check(**context):
    """Perform data quality checks"""
    print("🔍 Running data quality checks...")

    pg_hook = PostgresHook(postgres_conn_id='postgres_default')

    checks = []

    # Check 1: No duplicate emails
    dup_count = pg_hook.get_first("SELECT COUNT(*) FROM (SELECT email, COUNT(*) FROM users GROUP BY email HAVING COUNT(*) > 1) AS dups")[0]
    checks.append({
        'check': 'No duplicate emails',
        'passed': dup_count == 0,
        'value': dup_count
    })

    # Check 2: All records have valid email
    invalid_email_count = pg_hook.get_first("SELECT COUNT(*) FROM users WHERE email IS NULL OR email NOT LIKE '%@%.%'")[0]
    checks.append({
        'check': 'Valid email format',
        'passed': invalid_email_count == 0,
        'value': invalid_email_count
    })

    # Check 3: Minimum record count
    total_count = pg_hook.get_first("SELECT COUNT(*) FROM users")[0]
    checks.append({
        'check': 'Minimum 5 records',
        'passed': total_count >= 5,
        'value': total_count
    })

    # Print results
    print("\n📋 Quality Check Results:")
    for check in checks:
        status = "✅" if check['passed'] else "❌"
        print(f"  {status} {check['check']}: {check['value']}")

    # Fail if any check failed
    failed_checks = [c for c in checks if not c['passed']]
    if failed_checks:
        raise ValueError(f"{len(failed_checks)} quality checks failed!")

    print("\n✅ All quality checks passed")
    return True

# Define DAG
with DAG(
    'user_etl_pipeline',
    default_args=default_args,
    description='ETL pipeline for user data',
    schedule_interval='@daily',
    catchup=False,
    tags=['etl', 'example'],
) as dag:

    # Task 1: Create table if not exists
    create_table = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='postgres_default',
        sql="""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                full_name VARCHAR(255),
                email VARCHAR(255) UNIQUE,
                email_domain VARCHAR(255),
                city VARCHAR(255),
                company_name VARCHAR(255),
                phone VARCHAR(50),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE INDEX IF NOT EXISTS idx_email_domain ON users(email_domain);
            CREATE INDEX IF NOT EXISTS idx_city ON users(city);
        """
    )

    # Task 2: Extract data
    extract = PythonOperator(
        task_id='extract_data',
        python_callable=extract_api_data,
        provide_context=True
    )

    # Task 3: Transform data
    transform = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
        provide_context=True
    )

    # Task 4: Load data
    load = PythonOperator(
        task_id='load_data',
        python_callable=load_to_database,
        provide_context=True
    )

    # Task 5: Data quality checks
    quality_check = PythonOperator(
        task_id='quality_check',
        python_callable=data_quality_check,
        provide_context=True
    )

    # Task 6: Generate report
    report = PythonOperator(
        task_id='generate_report',
        python_callable=generate_report,
        provide_context=True
    )

    # Task 7: Success notification
    success_notification = BashOperator(
        task_id='success_notification',
        bash_command='echo "✅ ETL pipeline completed successfully!"'
    )

    # Define task dependencies
    create_table >> extract >> transform >> load >> quality_check >> report >> success_notification
