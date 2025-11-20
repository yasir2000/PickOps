"""
AWS Lambda Deployment and Testing
Demonstrates: Lambda function deployment, invocation, monitoring
"""

import boto3
import json
import zipfile
import io
from typing import Dict, Any

LAMBDA_ROLE_ARN = "arn:aws:iam::123456789012:role/lambda-execution-role"

class LambdaDeployer:
    """Deploy and manage AWS Lambda functions"""

    def __init__(self):
        self.lambda_client = boto3.client('lambda')
        self.logs_client = boto3.client('logs')

    def create_lambda_package(self, function_code: str) -> bytes:
        """Create deployment package"""

        print("📦 Creating deployment package...")

        # Create in-memory zip file
        zip_buffer = io.BytesIO()

        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            zip_file.writestr('lambda_function.py', function_code)

        zip_buffer.seek(0)
        return zip_buffer.read()

    def deploy_function(self, function_name: str, code: str, handler: str = 'lambda_function.handler') -> Dict:
        """Deploy Lambda function"""

        print(f"\n🚀 Deploying function: {function_name}...")

        # Create package
        zip_content = self.create_lambda_package(code)

        try:
            # Update existing function
            response = self.lambda_client.update_function_code(
                FunctionName=function_name,
                ZipFile=zip_content
            )
            print("✅ Function updated")

        except self.lambda_client.exceptions.ResourceNotFoundException:
            # Create new function
            response = self.lambda_client.create_function(
                FunctionName=function_name,
                Runtime='python3.9',
                Role=LAMBDA_ROLE_ARN,
                Handler=handler,
                Code={'ZipFile': zip_content},
                Timeout=30,
                MemorySize=256,
                Environment={
                    'Variables': {
                        'ENVIRONMENT': 'demo'
                    }
                }
            )
            print("✅ Function created")

        return response

    def invoke_function(self, function_name: str, payload: Dict) -> Dict:
        """Invoke Lambda function"""

        print(f"\n📞 Invoking function: {function_name}...")

        response = self.lambda_client.invoke(
            FunctionName=function_name,
            InvocationType='RequestResponse',
            Payload=json.dumps(payload)
        )

        result = json.loads(response['Payload'].read())

        print(f"   Status: {response['StatusCode']}")
        print(f"   Result: {json.dumps(result, indent=2)}")

        return result

    def get_function_logs(self, function_name: str, limit: int = 10):
        """Get recent function logs"""

        print(f"\n📋 Getting logs for: {function_name}...")

        log_group = f"/aws/lambda/{function_name}"

        try:
            # Get log streams
            streams = self.logs_client.describe_log_streams(
                logGroupName=log_group,
                orderBy='LastEventTime',
                descending=True,
                limit=1
            )

            if not streams['logStreams']:
                print("   No logs found")
                return

            stream_name = streams['logStreams'][0]['logStreamName']

            # Get events
            events = self.logs_client.get_log_events(
                logGroupName=log_group,
                logStreamName=stream_name,
                limit=limit
            )

            print(f"\n   Recent log events:")
            for event in events['events']:
                print(f"   {event['message'].strip()}")

        except Exception as e:
            print(f"   ❌ Error getting logs: {str(e)}")

# Sample Lambda functions
HELLO_WORLD_FUNCTION = """
import json

def handler(event, context):
    name = event.get('name', 'World')

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': f'Hello, {name}!',
            'event': event
        })
    }
"""

DATA_PROCESSOR_FUNCTION = """
import json

def handler(event, context):
    records = event.get('records', [])

    processed = []
    for record in records:
        # Process record
        processed_record = {
            'id': record.get('id'),
            'value': record.get('value', 0) * 2,
            'processed': True
        }
        processed.append(processed_record)

    return {
        'statusCode': 200,
        'body': json.dumps({
            'processed_count': len(processed),
            'records': processed
        })
    }
"""

API_HANDLER_FUNCTION = """
import json

def handler(event, context):
    http_method = event.get('httpMethod', 'GET')
    path = event.get('path', '/')

    # Route handling
    if path == '/users' and http_method == 'GET':
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({
                'users': [
                    {'id': 1, 'name': 'Alice'},
                    {'id': 2, 'name': 'Bob'}
                ]
            })
        }

    elif path.startswith('/users/') and http_method == 'GET':
        user_id = path.split('/')[-1]
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({
                'id': int(user_id),
                'name': f'User {user_id}'
            })
        }

    return {
        'statusCode': 404,
        'body': json.dumps({'error': 'Not found'})
    }
"""

def demo_lambda_deployment():
    """Demo Lambda deployment and testing"""

    print("⚡ AWS Lambda Deployment Demo")
    print("=" * 60)

    deployer = LambdaDeployer()

    # Deploy functions
    functions = [
        ('demo-hello-world', HELLO_WORLD_FUNCTION),
        ('demo-data-processor', DATA_PROCESSOR_FUNCTION),
        ('demo-api-handler', API_HANDLER_FUNCTION),
    ]

    deployed = []

    for func_name, func_code in functions:
        try:
            deployer.deploy_function(func_name, func_code)
            deployed.append(func_name)
        except Exception as e:
            print(f"❌ Failed to deploy {func_name}: {str(e)}")

    # Test functions
    print("\n" + "=" * 60)
    print("🧪 Testing Functions")
    print("=" * 60)

    # Test 1: Hello World
    if 'demo-hello-world' in deployed:
        deployer.invoke_function('demo-hello-world', {'name': 'Lambda'})
        deployer.get_function_logs('demo-hello-world', limit=5)

    # Test 2: Data Processor
    if 'demo-data-processor' in deployed:
        deployer.invoke_function('demo-data-processor', {
            'records': [
                {'id': 1, 'value': 10},
                {'id': 2, 'value': 20},
                {'id': 3, 'value': 30},
            ]
        })

    # Test 3: API Handler
    if 'demo-api-handler' in deployed:
        # GET /users
        deployer.invoke_function('demo-api-handler', {
            'httpMethod': 'GET',
            'path': '/users'
        })

        # GET /users/123
        deployer.invoke_function('demo-api-handler', {
            'httpMethod': 'GET',
            'path': '/users/123'
        })

    # Summary
    print("\n" + "=" * 60)
    print("📊 Summary")
    print("=" * 60)
    print(f"\n✅ Deployed {len(deployed)} functions:")
    for func in deployed:
        print(f"   - {func}")

if __name__ == "__main__":
    # Install: pip install boto3
    # Configure: aws configure
    demo_lambda_deployment()
