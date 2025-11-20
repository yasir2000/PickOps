"""
LocalStack AWS Testing Example
Demonstrates: Local AWS service testing, S3, Lambda, DynamoDB, SQS
"""

import boto3
import json
import zipfile
from io import BytesIO
import time

# LocalStack endpoint
LOCALSTACK_ENDPOINT = "http://localhost:4566"

# AWS clients pointing to LocalStack
s3_client = boto3.client(
    's3',
    endpoint_url=LOCALSTACK_ENDPOINT,
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

lambda_client = boto3.client(
    'lambda',
    endpoint_url=LOCALSTACK_ENDPOINT,
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

dynamodb = boto3.resource(
    'dynamodb',
    endpoint_url=LOCALSTACK_ENDPOINT,
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

sqs_client = boto3.client(
    'sqs',
    endpoint_url=LOCALSTACK_ENDPOINT,
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

def setup_s3():
    """Create S3 bucket and upload files"""
    print("\n📦 Setting up S3...")

    bucket_name = 'test-bucket'

    # Create bucket
    s3_client.create_bucket(Bucket=bucket_name)
    print(f"  Created bucket: {bucket_name}")

    # Upload sample files
    files = {
        'data/users.json': json.dumps([
            {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
            {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'}
        ]),
        'data/config.json': json.dumps({'env': 'test', 'version': '1.0'}),
        'logs/app.log': 'Log entry 1\nLog entry 2\n'
    }

    for key, content in files.items():
        s3_client.put_object(
            Bucket=bucket_name,
            Key=key,
            Body=content.encode() if isinstance(content, str) else content
        )
        print(f"  Uploaded: s3://{bucket_name}/{key}")

    return bucket_name

def setup_dynamodb():
    """Create DynamoDB table"""
    print("\n🗄️  Setting up DynamoDB...")

    table_name = 'users'

    # Create table
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {'AttributeName': 'user_id', 'KeyType': 'HASH'},
        ],
        AttributeDefinitions=[
            {'AttributeName': 'user_id', 'AttributeType': 'S'},
        ],
        BillingMode='PAY_PER_REQUEST'
    )

    print(f"  Created table: {table_name}")

    # Insert sample data
    users = [
        {'user_id': '1', 'name': 'Alice', 'email': 'alice@example.com', 'credits': 100},
        {'user_id': '2', 'name': 'Bob', 'email': 'bob@example.com', 'credits': 50},
        {'user_id': '3', 'name': 'Charlie', 'email': 'charlie@example.com', 'credits': 75}
    ]

    for user in users:
        table.put_item(Item=user)
        print(f"  Inserted: {user['name']}")

    return table

def setup_lambda():
    """Deploy Lambda function"""
    print("\n⚡ Setting up Lambda...")

    function_name = 'process-data'

    # Lambda function code
    lambda_code = """
import json

def lambda_handler(event, context):
    print("Processing event:", json.dumps(event))

    # Example processing
    result = {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Data processed successfully',
            'input': event
        })
    }

    return result
"""

    # Create deployment package
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.writestr('lambda_function.py', lambda_code)

    # Deploy function
    lambda_client.create_function(
        FunctionName=function_name,
        Runtime='python3.9',
        Role='arn:aws:iam::000000000000:role/lambda-role',
        Handler='lambda_function.lambda_handler',
        Code={'ZipFile': zip_buffer.getvalue()},
        Timeout=30,
        MemorySize=128
    )

    print(f"  Created function: {function_name}")

    return function_name

def setup_sqs():
    """Create SQS queue"""
    print("\n📬 Setting up SQS...")

    queue_name = 'data-processing-queue'

    # Create queue
    response = sqs_client.create_queue(
        QueueName=queue_name,
        Attributes={
            'MessageRetentionPeriod': '86400',  # 1 day
            'VisibilityTimeout': '30'
        }
    )

    queue_url = response['QueueUrl']
    print(f"  Created queue: {queue_name}")
    print(f"  Queue URL: {queue_url}")

    return queue_url

def test_s3_operations(bucket_name):
    """Test S3 read/write operations"""
    print("\n🧪 Testing S3 operations...")

    # List objects
    objects = s3_client.list_objects_v2(Bucket=bucket_name)
    print(f"  Objects in bucket: {objects['KeyCount']}")

    # Read object
    obj = s3_client.get_object(Bucket=bucket_name, Key='data/users.json')
    data = json.loads(obj['Body'].read())
    print(f"  Read users.json: {len(data)} users")

    # Write new object
    s3_client.put_object(
        Bucket=bucket_name,
        Key='test/output.txt',
        Body=b'Test output'
    )
    print("  ✅ S3 operations successful")

def test_dynamodb_operations(table):
    """Test DynamoDB queries"""
    print("\n🧪 Testing DynamoDB operations...")

    # Get item
    response = table.get_item(Key={'user_id': '1'})
    user = response.get('Item')
    print(f"  Retrieved user: {user['name']}")

    # Query
    response = table.scan()
    print(f"  Total users: {response['Count']}")

    # Update item
    table.update_item(
        Key={'user_id': '1'},
        UpdateExpression='SET credits = credits + :val',
        ExpressionAttributeValues={':val': 50}
    )
    print("  ✅ DynamoDB operations successful")

def test_lambda_invocation(function_name):
    """Test Lambda function invocation"""
    print("\n🧪 Testing Lambda invocation...")

    # Invoke function
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType='RequestResponse',
        Payload=json.dumps({
            'action': 'test',
            'data': {'key': 'value'}
        })
    )

    result = json.loads(response['Payload'].read())
    print(f"  Lambda response: {result['statusCode']}")
    print("  ✅ Lambda invocation successful")

def test_sqs_operations(queue_url):
    """Test SQS message operations"""
    print("\n🧪 Testing SQS operations...")

    # Send message
    sqs_client.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps({
            'type': 'test',
            'timestamp': time.time()
        })
    )
    print("  Sent message to queue")

    # Receive message
    messages = sqs_client.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1
    )

    if 'Messages' in messages:
        message = messages['Messages'][0]
        print(f"  Received message: {message['MessageId'][:20]}...")

        # Delete message
        sqs_client.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=message['ReceiptHandle']
        )
        print("  ✅ SQS operations successful")

def main():
    """Run complete LocalStack demo"""

    print("🚀 LocalStack AWS Testing Demo")
    print("=" * 60)

    try:
        # Setup services
        bucket_name = setup_s3()
        table = setup_dynamodb()
        function_name = setup_lambda()
        queue_url = setup_sqs()

        # Test operations
        print("\n" + "=" * 60)
        print("Running Tests")
        print("=" * 60)

        test_s3_operations(bucket_name)
        test_dynamodb_operations(table)
        test_lambda_invocation(function_name)
        test_sqs_operations(queue_url)

        # Integration test: S3 → Lambda → DynamoDB → SQS
        print("\n" + "=" * 60)
        print("Integration Test")
        print("=" * 60)
        print("\n🔗 Running integration workflow...")

        # 1. Read from S3
        obj = s3_client.get_object(Bucket=bucket_name, Key='data/users.json')
        users = json.loads(obj['Body'].read())
        print(f"  Step 1: Read {len(users)} users from S3")

        # 2. Process with Lambda
        for user in users:
            response = lambda_client.invoke(
                FunctionName=function_name,
                Payload=json.dumps(user)
            )
            print(f"  Step 2: Processed {user['name']} with Lambda")

        # 3. Update DynamoDB
        for user in users:
            table.update_item(
                Key={'user_id': str(user['id'])},
                UpdateExpression='SET last_processed = :time',
                ExpressionAttributeValues={':time': int(time.time())}
            )
        print(f"  Step 3: Updated {len(users)} records in DynamoDB")

        # 4. Send to SQS
        for user in users:
            sqs_client.send_message(
                QueueUrl=queue_url,
                MessageBody=json.dumps({
                    'user_id': user['id'],
                    'status': 'processed'
                })
            )
        print(f"  Step 4: Sent {len(users)} messages to SQS")

        print("\n✅ Integration workflow complete!")

        print("\n" + "=" * 60)
        print("✨ All tests passed!")
        print("=" * 60)

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        raise

if __name__ == "__main__":
    # Install: pip install boto3
    main()
