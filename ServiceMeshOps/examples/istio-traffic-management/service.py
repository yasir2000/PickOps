"""
Istio Traffic Management Demo
Demonstrates: Canary deployments, circuit breaking, fault injection
"""

from flask import Flask, jsonify, request
import os
import random
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Service configuration
SERVICE_NAME = os.getenv('SERVICE_NAME', 'demo-service')
VERSION = os.getenv('VERSION', 'v1')
PORT = int(os.getenv('PORT', 5000))

app = Flask(__name__)

# Simulate different behavior between versions
FEATURES = {
    'v1': {
        'cache': False,
        'ml_model': 'basic',
        'response_time': 0.1
    },
    'v2': {
        'cache': True,
        'ml_model': 'advanced',
        'response_time': 0.05
    },
    'v3': {
        'cache': True,
        'ml_model': 'experimental',
        'response_time': 0.03
    }
}

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': SERVICE_NAME,
        'version': VERSION
    })

@app.route('/ready')
def ready():
    """Readiness check endpoint"""
    # Simulate readiness delay for new versions
    if VERSION == 'v3':
        time.sleep(0.5)

    return jsonify({
        'status': 'ready',
        'service': SERVICE_NAME,
        'version': VERSION
    })

@app.route('/')
def index():
    """Main endpoint"""

    # Get version features
    features = FEATURES.get(VERSION, FEATURES['v1'])

    # Simulate response time
    time.sleep(features['response_time'])

    # Simulate occasional errors in v3 (experimental)
    if VERSION == 'v3' and random.random() < 0.1:
        logger.error("Simulated error in v3")
        return jsonify({
            'error': 'Internal server error',
            'version': VERSION
        }), 500

    return jsonify({
        'message': f'Hello from {SERVICE_NAME}',
        'version': VERSION,
        'features': features,
        'timestamp': time.time()
    })

@app.route('/api/data')
def get_data():
    """Data endpoint with version-specific behavior"""

    features = FEATURES.get(VERSION, FEATURES['v1'])

    # Simulate cache hit in v2/v3
    if features['cache']:
        logger.info(f"Cache hit for version {VERSION}")
        time.sleep(0.01)
    else:
        logger.info(f"Cache miss for version {VERSION}")
        time.sleep(0.1)

    # Generate data based on ML model
    data = {
        'basic': [random.randint(1, 100) for _ in range(10)],
        'advanced': [random.gauss(50, 15) for _ in range(20)],
        'experimental': [random.expovariate(0.1) for _ in range(30)]
    }

    return jsonify({
        'version': VERSION,
        'model': features['ml_model'],
        'cached': features['cache'],
        'data': data[features['ml_model']]
    })

@app.route('/api/slow')
def slow_endpoint():
    """Intentionally slow endpoint for testing timeouts"""

    delay = float(request.args.get('delay', 2.0))
    time.sleep(delay)

    return jsonify({
        'version': VERSION,
        'delay': delay,
        'message': 'Slow response'
    })

@app.route('/api/error')
def error_endpoint():
    """Endpoint for testing error handling"""

    error_rate = float(request.args.get('rate', 0.5))

    if random.random() < error_rate:
        logger.error(f"Simulated error (rate={error_rate})")
        return jsonify({
            'error': 'Simulated failure',
            'version': VERSION
        }), 500

    return jsonify({
        'version': VERSION,
        'message': 'Success'
    })

@app.route('/api/upstream')
def call_upstream():
    """Call another service (for testing service mesh)"""

    import requests

    upstream = os.getenv('UPSTREAM_SERVICE', 'http://demo-service-v2:5000')

    try:
        response = requests.get(f'{upstream}/', timeout=2)
        data = response.json()

        return jsonify({
            'current_version': VERSION,
            'upstream_response': data
        })

    except Exception as e:
        logger.error(f"Upstream call failed: {str(e)}")
        return jsonify({
            'error': 'Upstream service unavailable',
            'current_version': VERSION
        }), 503

if __name__ == '__main__':
    logger.info(f"Starting {SERVICE_NAME} {VERSION} on port {PORT}")
    app.run(host='0.0.0.0', port=PORT, debug=False)
