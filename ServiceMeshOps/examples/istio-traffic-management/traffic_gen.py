"""
Traffic Generator for Service Mesh Testing
Generates various traffic patterns to test service mesh features
"""

import requests
import time
import random
import logging
from concurrent.futures import ThreadPoolExecutor
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TARGET_URL = os.getenv('TARGET_URL', 'http://envoy:8000')

def make_request(endpoint='/', expected_status=200):
    """Make HTTP request and track response"""
    try:
        start = time.time()
        response = requests.get(f"{TARGET_URL}{endpoint}", timeout=5)
        duration = time.time() - start

        version = response.json().get('version', 'unknown') if response.status_code == 200 else 'error'

        return {
            'endpoint': endpoint,
            'status': response.status_code,
            'duration': duration,
            'version': version,
            'success': response.status_code == expected_status
        }
    except Exception as e:
        logger.error(f"Request failed: {str(e)}")
        return {
            'endpoint': endpoint,
            'status': 0,
            'duration': 0,
            'version': 'error',
            'success': False
        }

def generate_normal_traffic(duration=60, rps=10):
    """Generate normal traffic pattern"""

    logger.info(f"Generating normal traffic: {rps} req/s for {duration}s")

    stats = {'v1': 0, 'v2': 0, 'v3': 0, 'error': 0}
    total = 0

    start_time = time.time()

    while time.time() - start_time < duration:
        result = make_request('/')
        stats[result['version']] += 1
        total += 1

        if total % 50 == 0:
            logger.info(f"Processed {total} requests - v1: {stats['v1']}, "
                       f"v2: {stats['v2']}, v3: {stats['v3']}, errors: {stats['error']}")

        time.sleep(1.0 / rps)

    logger.info(f"Final stats: {stats}")
    logger.info(f"Traffic split - v1: {stats['v1']/total*100:.1f}%, "
               f"v2: {stats['v2']/total*100:.1f}%, "
               f"v3: {stats['v3']/total*100:.1f}%")

def generate_burst_traffic(duration=30, burst_rps=50):
    """Generate burst traffic pattern"""

    logger.info(f"Generating burst traffic: {burst_rps} req/s for {duration}s")

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = []
        start_time = time.time()

        while time.time() - start_time < duration:
            futures.append(executor.submit(make_request, '/'))
            time.sleep(1.0 / burst_rps)

        results = [f.result() for f in futures]

        success_count = sum(1 for r in results if r['success'])
        avg_duration = sum(r['duration'] for r in results) / len(results)

        logger.info(f"Burst complete - Success rate: {success_count/len(results)*100:.1f}%, "
                   f"Avg duration: {avg_duration:.3f}s")

def test_circuit_breaker():
    """Test circuit breaker with error endpoint"""

    logger.info("Testing circuit breaker with error endpoint")

    # Send requests with high error rate
    for i in range(20):
        result = make_request('/api/error?rate=0.8')
        logger.info(f"Request {i+1}: status={result['status']}, version={result['version']}")
        time.sleep(0.5)

    # Circuit should be open, test normal endpoint
    logger.info("Circuit should be open, testing normal endpoint")
    for i in range(5):
        result = make_request('/')
        logger.info(f"Request {i+1}: status={result['status']}, version={result['version']}")
        time.sleep(1)

def test_timeout():
    """Test timeout handling"""

    logger.info("Testing timeout with slow endpoint")

    for delay in [1, 2, 3, 5]:
        logger.info(f"Testing {delay}s delay")
        result = make_request(f'/api/slow?delay={delay}')
        logger.info(f"Result: status={result['status']}, duration={result['duration']:.3f}s")
        time.sleep(1)

def test_canary_deployment():
    """Test canary deployment traffic distribution"""

    logger.info("Testing canary deployment (70/25/5 split)")

    stats = {'v1': 0, 'v2': 0, 'v3': 0, 'error': 0}

    # Send 100 requests
    for i in range(100):
        result = make_request('/')
        stats[result['version']] += 1
        time.sleep(0.1)

    logger.info(f"Canary results:")
    logger.info(f"  v1 (stable): {stats['v1']}% (expected ~70%)")
    logger.info(f"  v2 (canary): {stats['v2']}% (expected ~25%)")
    logger.info(f"  v3 (experimental): {stats['v3']}% (expected ~5%)")

def main():
    """Run traffic generation scenarios"""

    logger.info("=" * 60)
    logger.info("Service Mesh Traffic Generator")
    logger.info(f"Target: {TARGET_URL}")
    logger.info("=" * 60)

    # Wait for services to be ready
    logger.info("Waiting for services to be ready...")
    time.sleep(10)

    try:
        # Test 1: Canary deployment
        test_canary_deployment()
        time.sleep(5)

        # Test 2: Normal traffic
        generate_normal_traffic(duration=30, rps=5)
        time.sleep(5)

        # Test 3: Burst traffic
        generate_burst_traffic(duration=20, burst_rps=30)
        time.sleep(5)

        # Test 4: Circuit breaker
        test_circuit_breaker()
        time.sleep(5)

        # Test 5: Timeout handling
        test_timeout()

        logger.info("\n" + "=" * 60)
        logger.info("All tests complete!")
        logger.info("=" * 60)

        # Keep generating light traffic
        logger.info("Generating background traffic...")
        generate_normal_traffic(duration=300, rps=2)

    except KeyboardInterrupt:
        logger.info("Traffic generation stopped")

if __name__ == "__main__":
    main()
