"""
AI-Powered Anomaly Detection
Demonstrates: Log analysis, pattern detection, automated alerting
"""

import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from datetime import datetime, timedelta
import random
from typing import List, Dict, Any

class AIOpsAnomalyDetector:
    """AI-powered anomaly detection for operations"""

    def __init__(self):
        self.model = IsolationForest(
            contamination=0.1,  # 10% anomalies expected
            random_state=42
        )
        self.scaler = StandardScaler()
        self.trained = False

    def generate_metrics(self, hours: int = 24, anomaly_rate: float = 0.05) -> List[Dict]:
        """Generate sample metrics data"""

        print(f"📊 Generating {hours} hours of metrics data...")

        metrics = []
        base_time = datetime.now() - timedelta(hours=hours)

        for i in range(hours * 60):  # Minute-by-minute
            timestamp = base_time + timedelta(minutes=i)

            # Normal patterns with daily cycle
            hour_of_day = timestamp.hour
            base_cpu = 30 + 20 * np.sin(2 * np.pi * hour_of_day / 24)
            base_memory = 50 + 15 * np.sin(2 * np.pi * hour_of_day / 24)
            base_latency = 100 + 50 * np.sin(2 * np.pi * hour_of_day / 24)

            # Add noise
            cpu = base_cpu + np.random.normal(0, 5)
            memory = base_memory + np.random.normal(0, 3)
            latency = base_latency + np.random.normal(0, 10)

            # Inject anomalies
            if random.random() < anomaly_rate:
                cpu += random.uniform(30, 50)
                memory += random.uniform(20, 40)
                latency += random.uniform(100, 300)

            metrics.append({
                'timestamp': timestamp.isoformat(),
                'cpu_percent': max(0, min(100, cpu)),
                'memory_percent': max(0, min(100, memory)),
                'latency_ms': max(0, latency),
                'error_rate': random.uniform(0, 5) if random.random() > 0.95 else 0,
                'requests_per_sec': max(0, 100 + np.random.normal(0, 20))
            })

        return metrics

    def extract_features(self, metrics: List[Dict]) -> np.ndarray:
        """Extract features for anomaly detection"""

        features = []

        for metric in metrics:
            features.append([
                metric['cpu_percent'],
                metric['memory_percent'],
                metric['latency_ms'],
                metric['error_rate'],
                metric['requests_per_sec']
            ])

        return np.array(features)

    def train(self, metrics: List[Dict]):
        """Train anomaly detection model"""

        print("\n🤖 Training anomaly detection model...")

        features = self.extract_features(metrics)

        # Normalize features
        features_scaled = self.scaler.fit_transform(features)

        # Train model
        self.model.fit(features_scaled)
        self.trained = True

        print("✅ Model trained")

    def detect_anomalies(self, metrics: List[Dict]) -> List[Dict]:
        """Detect anomalies in metrics"""

        if not self.trained:
            raise Exception("Model not trained")

        print("\n🔍 Detecting anomalies...")

        features = self.extract_features(metrics)
        features_scaled = self.scaler.transform(features)

        # Predict anomalies (-1 = anomaly, 1 = normal)
        predictions = self.model.predict(features_scaled)

        # Get anomaly scores
        scores = self.model.score_samples(features_scaled)

        anomalies = []

        for i, (prediction, score) in enumerate(zip(predictions, scores)):
            if prediction == -1:  # Anomaly detected
                anomaly = {
                    'timestamp': metrics[i]['timestamp'],
                    'anomaly_score': float(score),
                    'metrics': metrics[i],
                    'severity': 'critical' if score < -0.5 else 'warning'
                }
                anomalies.append(anomaly)

        print(f"   Found {len(anomalies)} anomalies")

        return anomalies

    def analyze_anomaly(self, anomaly: Dict) -> Dict:
        """Analyze anomaly and determine root cause"""

        metrics = anomaly['metrics']

        # Determine which metrics are abnormal
        issues = []

        if metrics['cpu_percent'] > 80:
            issues.append(('High CPU Usage', metrics['cpu_percent'], '%'))

        if metrics['memory_percent'] > 80:
            issues.append(('High Memory Usage', metrics['memory_percent'], '%'))

        if metrics['latency_ms'] > 200:
            issues.append(('High Latency', metrics['latency_ms'], 'ms'))

        if metrics['error_rate'] > 2:
            issues.append(('Elevated Error Rate', metrics['error_rate'], '%'))

        # Generate recommendations
        recommendations = []

        for issue, value, unit in issues:
            if 'CPU' in issue:
                recommendations.append("Scale up compute resources")
                recommendations.append("Check for CPU-intensive processes")
            elif 'Memory' in issue:
                recommendations.append("Increase memory allocation")
                recommendations.append("Check for memory leaks")
            elif 'Latency' in issue:
                recommendations.append("Investigate network issues")
                recommendations.append("Check database query performance")
            elif 'Error' in issue:
                recommendations.append("Review recent deployments")
                recommendations.append("Check application logs")

        return {
            'issues': issues,
            'recommendations': list(set(recommendations))
        }

    def create_alert(self, anomaly: Dict, analysis: Dict) -> Dict:
        """Create alert for anomaly"""

        alert = {
            'alert_id': f"ALERT-{int(datetime.now().timestamp())}",
            'timestamp': anomaly['timestamp'],
            'severity': anomaly['severity'],
            'title': f"Anomaly Detected - {anomaly['severity'].upper()}",
            'description': f"Anomaly score: {anomaly['anomaly_score']:.3f}",
            'issues': analysis['issues'],
            'recommendations': analysis['recommendations'],
            'metrics': anomaly['metrics']
        }

        return alert

def demo_aiops():
    """Run AIOps demo"""

    print("🤖 AI-Powered Operations Demo")
    print("=" * 60)

    detector = AIOpsAnomalyDetector()

    # Generate training data
    print("\n1️⃣  Generating training data...")
    training_metrics = detector.generate_metrics(hours=48, anomaly_rate=0.02)

    # Train model
    detector.train(training_metrics)

    # Generate test data with more anomalies
    print("\n2️⃣  Generating test data...")
    test_metrics = detector.generate_metrics(hours=6, anomaly_rate=0.08)

    # Detect anomalies
    anomalies = detector.detect_anomalies(test_metrics)

    # Analyze and alert
    print("\n3️⃣  Analyzing anomalies...")
    print("=" * 60)

    alerts = []

    for i, anomaly in enumerate(anomalies[:5], 1):  # Show top 5
        print(f"\n🚨 Anomaly #{i}")
        print(f"   Time: {anomaly['timestamp']}")
        print(f"   Severity: {anomaly['severity']}")
        print(f"   Score: {anomaly['anomaly_score']:.3f}")

        # Analyze
        analysis = detector.analyze_anomaly(anomaly)

        print(f"\n   Issues detected:")
        for issue, value, unit in analysis['issues']:
            print(f"     - {issue}: {value:.1f}{unit}")

        print(f"\n   Recommendations:")
        for rec in analysis['recommendations']:
            print(f"     • {rec}")

        # Create alert
        alert = detector.create_alert(anomaly, analysis)
        alerts.append(alert)

    # Summary
    print("\n" + "=" * 60)
    print("📊 Summary")
    print("=" * 60)

    print(f"\nTotal metrics analyzed: {len(test_metrics)}")
    print(f"Anomalies detected: {len(anomalies)}")
    print(f"Alerts created: {len(alerts)}")

    severity_counts = {}
    for alert in alerts:
        severity_counts[alert['severity']] = severity_counts.get(alert['severity'], 0) + 1

    print(f"\nBy severity:")
    for severity, count in severity_counts.items():
        print(f"  {severity}: {count}")

    print(f"\n✅ AIOps analysis complete!")

if __name__ == "__main__":
    # Install: pip install numpy scikit-learn
    demo_aiops()
