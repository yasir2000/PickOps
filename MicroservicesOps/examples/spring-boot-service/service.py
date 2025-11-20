"""
Spring Boot Microservice Example (Python Simulation)
Demonstrates: Service registration, health checks, REST API, distributed tracing
"""

from flask import Flask, jsonify, request
import requests
import os
import logging
from datetime import datetime
import json
import socket

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Service Configuration
SERVICE_NAME = os.getenv('SERVICE_NAME', 'user-service')
SERVICE_PORT = int(os.getenv('SERVICE_PORT', 8080))
SERVICE_HOST = socket.gethostname()
SERVICE_VERSION = os.getenv('SERVICE_VERSION', '1.0.0')

# External Services
CONSUL_HOST = os.getenv('CONSUL_HOST', 'localhost:8500')
EUREKA_HOST = os.getenv('EUREKA_HOST', 'localhost:8761')
JAEGER_HOST = os.getenv('JAEGER_HOST', 'localhost')
JAEGER_PORT = int(os.getenv('JAEGER_PORT', 6831))

app = Flask(__name__)

# In-memory data store
users = {}
user_id_counter = 1

class ServiceRegistry:
    """Handle service registration with Consul and Eureka"""

    @staticmethod
    def register_consul():
        """Register service with Consul"""
        try:
            service_def = {
                "ID": f"{SERVICE_NAME}-{SERVICE_HOST}-{SERVICE_PORT}",
                "Name": SERVICE_NAME,
                "Tags": [SERVICE_VERSION, "microservice"],
                "Address": SERVICE_HOST,
                "Port": SERVICE_PORT,
                "Check": {
                    "HTTP": f"http://{SERVICE_HOST}:{SERVICE_PORT}/health",
                    "Interval": "10s",
                    "Timeout": "5s"
                },
                "Meta": {
                    "version": SERVICE_VERSION,
                    "environment": "development"
                }
            }

            response = requests.put(
                f"http://{CONSUL_HOST}/v1/agent/service/register",
                json=service_def
            )

            if response.status_code == 200:
                logger.info(f"✅ Registered with Consul: {SERVICE_NAME}")
                return True
            else:
                logger.error(f"❌ Consul registration failed: {response.text}")
                return False

        except Exception as e:
            logger.error(f"❌ Consul registration error: {str(e)}")
            return False

    @staticmethod
    def register_eureka():
        """Register service with Eureka"""
        try:
            instance = {
                "instance": {
                    "instanceId": f"{SERVICE_HOST}:{SERVICE_NAME}:{SERVICE_PORT}",
                    "hostName": SERVICE_HOST,
                    "app": SERVICE_NAME.upper(),
                    "ipAddr": SERVICE_HOST,
                    "status": "UP",
                    "port": {
                        "$": SERVICE_PORT,
                        "@enabled": "true"
                    },
                    "healthCheckUrl": f"http://{SERVICE_HOST}:{SERVICE_PORT}/health",
                    "statusPageUrl": f"http://{SERVICE_HOST}:{SERVICE_PORT}/info",
                    "homePageUrl": f"http://{SERVICE_HOST}:{SERVICE_PORT}/",
                    "dataCenterInfo": {
                        "@class": "com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo",
                        "name": "MyOwn"
                    },
                    "metadata": {
                        "version": SERVICE_VERSION,
                        "environment": "development"
                    }
                }
            }

            response = requests.post(
                f"http://{EUREKA_HOST}/eureka/apps/{SERVICE_NAME.upper()}",
                json=instance,
                headers={"Content-Type": "application/json"}
            )

            if response.status_code in [200, 204]:
                logger.info(f"✅ Registered with Eureka: {SERVICE_NAME}")
                return True
            else:
                logger.error(f"❌ Eureka registration failed: {response.text}")
                return False

        except Exception as e:
            logger.error(f"❌ Eureka registration error: {str(e)}")
            return False

    @staticmethod
    def deregister_consul():
        """Deregister from Consul"""
        try:
            service_id = f"{SERVICE_NAME}-{SERVICE_HOST}-{SERVICE_PORT}"
            requests.put(f"http://{CONSUL_HOST}/v1/agent/service/deregister/{service_id}")
            logger.info(f"🔌 Deregistered from Consul")
        except Exception as e:
            logger.error(f"❌ Consul deregistration error: {str(e)}")

# Health Check Endpoint
@app.route('/health')
def health():
    """Health check endpoint for service discovery"""
    return jsonify({
        'status': 'UP',
        'service': SERVICE_NAME,
        'version': SERVICE_VERSION,
        'timestamp': datetime.utcnow().isoformat(),
        'checks': {
            'database': 'UP',
            'cache': 'UP',
            'messaging': 'UP'
        }
    }), 200

# Info Endpoint
@app.route('/info')
def info():
    """Service information endpoint"""
    return jsonify({
        'service': SERVICE_NAME,
        'version': SERVICE_VERSION,
        'host': SERVICE_HOST,
        'port': SERVICE_PORT,
        'description': 'User management microservice',
        'capabilities': ['create', 'read', 'update', 'delete'],
        'dependencies': ['postgres', 'redis', 'rabbitmq']
    })

# Metrics Endpoint (Prometheus format)
@app.route('/metrics')
def metrics():
    """Prometheus metrics endpoint"""
    metrics_data = f"""
# HELP user_service_requests_total Total requests
# TYPE user_service_requests_total counter
user_service_requests_total{{service="{SERVICE_NAME}",version="{SERVICE_VERSION}"}} {len(users)}

# HELP user_service_users_total Total users
# TYPE user_service_users_total gauge
user_service_users_total{{service="{SERVICE_NAME}"}} {len(users)}

# HELP user_service_up Service up status
# TYPE user_service_up gauge
user_service_up{{service="{SERVICE_NAME}"}} 1
"""
    return metrics_data, 200, {'Content-Type': 'text/plain; charset=utf-8'}

# REST API Endpoints

@app.route('/users', methods=['GET'])
def get_users():
    """Get all users"""
    logger.info(f"GET /users - Retrieved {len(users)} users")
    return jsonify({
        'users': list(users.values()),
        'total': len(users)
    })

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get user by ID"""
    if user_id not in users:
        logger.warning(f"GET /users/{user_id} - User not found")
        return jsonify({'error': 'User not found'}), 404

    logger.info(f"GET /users/{user_id} - User retrieved")
    return jsonify(users[user_id])

@app.route('/users', methods=['POST'])
def create_user():
    """Create new user"""
    global user_id_counter

    data = request.get_json()

    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Name and email are required'}), 400

    user = {
        'id': user_id_counter,
        'name': data['name'],
        'email': data['email'],
        'created_at': datetime.utcnow().isoformat(),
        'version': SERVICE_VERSION
    }

    users[user_id_counter] = user
    logger.info(f"POST /users - Created user {user_id_counter}")

    # Publish event to RabbitMQ (simulated)
    publish_event('user.created', user)

    user_id_counter += 1
    return jsonify(user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update user"""
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()

    if 'name' in data:
        users[user_id]['name'] = data['name']
    if 'email' in data:
        users[user_id]['email'] = data['email']

    users[user_id]['updated_at'] = datetime.utcnow().isoformat()

    logger.info(f"PUT /users/{user_id} - User updated")

    # Publish event
    publish_event('user.updated', users[user_id])

    return jsonify(users[user_id])

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete user"""
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404

    user = users[user_id]
    del users[user_id]

    logger.info(f"DELETE /users/{user_id} - User deleted")

    # Publish event
    publish_event('user.deleted', user)

    return '', 204

def publish_event(event_type: str, data: dict):
    """Publish event to message broker (simulated)"""
    try:
        event = {
            'type': event_type,
            'service': SERVICE_NAME,
            'timestamp': datetime.utcnow().isoformat(),
            'data': data
        }
        logger.info(f"📤 Publishing event: {event_type}")
        # In real implementation, publish to RabbitMQ/Kafka
    except Exception as e:
        logger.error(f"Event publishing failed: {str(e)}")

@app.route('/service-to-service/example')
def service_to_service():
    """Example of service-to-service communication"""
    try:
        # Discover service from Consul
        response = requests.get(f"http://{CONSUL_HOST}/v1/catalog/service/order-service")

        if response.status_code == 200:
            services = response.json()
            if services:
                service = services[0]
                service_url = f"http://{service['ServiceAddress']}:{service['ServicePort']}"

                # Call other service
                orders_response = requests.get(f"{service_url}/orders", timeout=5)

                return jsonify({
                    'message': 'Service-to-service communication successful',
                    'service': 'order-service',
                    'response': orders_response.json()
                })

        return jsonify({'error': 'Service not found'}), 404

    except Exception as e:
        logger.error(f"Service communication error: {str(e)}")
        return jsonify({'error': 'Service communication failed'}), 503

def startup():
    """Service startup routine"""
    logger.info("=" * 60)
    logger.info(f"Starting {SERVICE_NAME} v{SERVICE_VERSION}")
    logger.info(f"Host: {SERVICE_HOST}:{SERVICE_PORT}")
    logger.info("=" * 60)

    # Register with service discovery
    ServiceRegistry.register_consul()
    ServiceRegistry.register_eureka()

    logger.info("✅ Service started successfully")

def shutdown():
    """Service shutdown routine"""
    logger.info("Shutting down service...")
    ServiceRegistry.deregister_consul()

if __name__ == '__main__':
    startup()

    try:
        app.run(host='0.0.0.0', port=SERVICE_PORT, debug=False)
    finally:
        shutdown()
