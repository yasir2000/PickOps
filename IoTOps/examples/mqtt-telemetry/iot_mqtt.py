"""
IoT Device Telemetry with MQTT
Demonstrates: MQTT messaging, device simulation, data processing, monitoring
"""

import paho.mqtt.client as mqtt
import json
import time
from datetime import datetime
import random
from typing import Dict, Any
import threading

MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC_TELEMETRY = "devices/+/telemetry"
MQTT_TOPIC_COMMANDS = "devices/+/commands"

class IoTDevice:
    """Simulated IoT device sending telemetry"""

    def __init__(self, device_id: str, device_type: str):
        self.device_id = device_id
        self.device_type = device_type
        self.client = mqtt.Client(client_id=f"device-{device_id}")
        self.running = False

        # Device state
        self.temperature = 20.0
        self.humidity = 50.0
        self.battery = 100.0

        # Setup callbacks
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        """Called when device connects to broker"""
        if rc == 0:
            print(f"✅ Device {self.device_id} connected to MQTT broker")
            # Subscribe to commands for this device
            client.subscribe(f"devices/{self.device_id}/commands")
        else:
            print(f"❌ Connection failed with code {rc}")

    def on_message(self, client, userdata, msg):
        """Handle incoming commands"""
        try:
            command = json.loads(msg.payload.decode())
            print(f"📨 Device {self.device_id} received command: {command}")

            # Handle different commands
            if command['action'] == 'reboot':
                print(f"  🔄 Rebooting device {self.device_id}...")
            elif command['action'] == 'update_interval':
                print(f"  ⏱️  Updating telemetry interval to {command['interval']}s")

        except Exception as e:
            print(f"❌ Error processing command: {str(e)}")

    def generate_telemetry(self) -> Dict[str, Any]:
        """Generate realistic telemetry data"""

        # Simulate sensor drift and noise
        self.temperature += random.uniform(-0.5, 0.5)
        self.humidity += random.uniform(-2, 2)
        self.battery -= random.uniform(0.01, 0.05)

        # Keep values in realistic ranges
        self.temperature = max(15, min(35, self.temperature))
        self.humidity = max(30, min(90, self.humidity))
        self.battery = max(0, min(100, self.battery))

        return {
            'device_id': self.device_id,
            'device_type': self.device_type,
            'timestamp': datetime.utcnow().isoformat(),
            'telemetry': {
                'temperature': round(self.temperature, 2),
                'humidity': round(self.humidity, 2),
                'battery': round(self.battery, 2),
            },
            'metadata': {
                'firmware_version': '1.2.3',
                'signal_strength': random.randint(-90, -30)
            }
        }

    def start(self, interval: int = 5):
        """Start sending telemetry"""
        self.client.connect(MQTT_BROKER, MQTT_PORT, 60)
        self.client.loop_start()
        self.running = True

        try:
            while self.running:
                # Generate and send telemetry
                telemetry = self.generate_telemetry()
                topic = f"devices/{self.device_id}/telemetry"

                self.client.publish(
                    topic,
                    json.dumps(telemetry),
                    qos=1
                )

                print(f"📤 {self.device_id}: T={telemetry['telemetry']['temperature']}°C, "
                      f"H={telemetry['telemetry']['humidity']}%, "
                      f"Battery={telemetry['telemetry']['battery']}%")

                time.sleep(interval)

        except KeyboardInterrupt:
            print(f"\n⏸️  Device {self.device_id} stopped")
        finally:
            self.stop()

    def stop(self):
        """Stop device"""
        self.running = False
        self.client.loop_stop()
        self.client.disconnect()

class IoTGateway:
    """IoT Gateway for processing device telemetry"""

    def __init__(self):
        self.client = mqtt.Client(client_id="iot-gateway")
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        self.device_states = {}
        self.alert_thresholds = {
            'temperature': (15, 30),
            'humidity': (40, 80),
            'battery': 20
        }

    def on_connect(self, client, userdata, flags, rc):
        """Called when gateway connects"""
        if rc == 0:
            print("✅ Gateway connected to MQTT broker")
            # Subscribe to all device telemetry
            client.subscribe(MQTT_TOPIC_TELEMETRY, qos=1)
        else:
            print(f"❌ Connection failed with code {rc}")

    def on_message(self, client, userdata, msg):
        """Process incoming telemetry"""
        try:
            data = json.loads(msg.payload.decode())
            device_id = data['device_id']
            telemetry = data['telemetry']

            # Update device state
            self.device_states[device_id] = {
                'last_seen': datetime.utcnow(),
                'telemetry': telemetry
            }

            # Check for alerts
            self.check_alerts(device_id, telemetry)

            # Log to console
            print(f"📊 Gateway processed: {device_id} - {telemetry}")

        except Exception as e:
            print(f"❌ Error processing telemetry: {str(e)}")

    def check_alerts(self, device_id: str, telemetry: Dict):
        """Check for alert conditions"""

        # Temperature alerts
        temp = telemetry['temperature']
        temp_min, temp_max = self.alert_thresholds['temperature']
        if temp < temp_min or temp > temp_max:
            self.send_alert(device_id, 'temperature', temp, f"out of range ({temp_min}-{temp_max})")

        # Humidity alerts
        humidity = telemetry['humidity']
        hum_min, hum_max = self.alert_thresholds['humidity']
        if humidity < hum_min or humidity > hum_max:
            self.send_alert(device_id, 'humidity', humidity, f"out of range ({hum_min}-{hum_max})")

        # Battery alerts
        battery = telemetry['battery']
        if battery < self.alert_thresholds['battery']:
            self.send_alert(device_id, 'battery', battery, "low battery")

    def send_alert(self, device_id: str, metric: str, value: float, reason: str):
        """Send alert"""
        alert = {
            'device_id': device_id,
            'metric': metric,
            'value': value,
            'reason': reason,
            'timestamp': datetime.utcnow().isoformat()
        }

        print(f"🚨 ALERT: {device_id} - {metric} = {value} ({reason})")

        # Publish to alerts topic
        self.client.publish(
            f"alerts/{device_id}",
            json.dumps(alert),
            qos=1
        )

    def send_command(self, device_id: str, command: Dict):
        """Send command to device"""
        topic = f"devices/{device_id}/commands"
        self.client.publish(topic, json.dumps(command), qos=1)
        print(f"📤 Sent command to {device_id}: {command}")

    def start(self):
        """Start gateway"""
        self.client.connect(MQTT_BROKER, MQTT_PORT, 60)
        print("🌐 IoT Gateway started")
        self.client.loop_forever()

    def stop(self):
        """Stop gateway"""
        self.client.disconnect()

def demo_devices():
    """Run device simulation"""

    print("🔌 Starting IoT Devices")
    print("=" * 60)

    # Create devices
    devices = [
        IoTDevice("sensor-001", "temperature_sensor"),
        IoTDevice("sensor-002", "humidity_sensor"),
        IoTDevice("sensor-003", "environmental_monitor"),
    ]

    # Start devices in threads
    threads = []
    for device in devices:
        thread = threading.Thread(target=device.start, args=(5,))
        thread.daemon = True
        thread.start()
        threads.append(thread)

    # Keep running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n⏸️  Stopping all devices...")
        for device in devices:
            device.stop()

def demo_gateway():
    """Run gateway"""

    print("🌐 Starting IoT Gateway")
    print("=" * 60)

    gateway = IoTGateway()

    try:
        gateway.start()
    except KeyboardInterrupt:
        print("\n⏸️  Gateway stopped")
        gateway.stop()

def main():
    """Run complete IoT demo"""

    import sys

    if len(sys.argv) > 1:
        mode = sys.argv[1]

        if mode == 'devices':
            demo_devices()
        elif mode == 'gateway':
            demo_gateway()
        else:
            print(f"Unknown mode: {mode}")
            print("Usage: python iot_mqtt.py [devices|gateway]")
    else:
        print("IoT MQTT Telemetry System")
        print("=" * 60)
        print("\nRun in separate terminals:")
        print("  Terminal 1: python iot_mqtt.py gateway")
        print("  Terminal 2: python iot_mqtt.py devices")

if __name__ == "__main__":
    # Install: pip install paho-mqtt
    main()
