"""
Kafka Producer-Consumer Example
Demonstrates: Event publishing, consuming, processing, error handling
"""

from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import KafkaError
import json
import time
from datetime import datetime
from typing import Dict, Any
import random

KAFKA_BOOTSTRAP_SERVERS = ['localhost:9092']
TOPIC_NAME = 'user-events'

class EventProducer:
    """Kafka event producer"""

    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            key_serializer=lambda k: k.encode('utf-8') if k else None,
            acks='all',  # Wait for all replicas
            retries=3,
            max_in_flight_requests_per_connection=1
        )

    def send_event(self, event_type: str, data: Dict[str, Any]) -> bool:
        """Send event to Kafka"""

        event = {
            'event_id': f"evt-{int(time.time() * 1000)}",
            'event_type': event_type,
            'timestamp': datetime.utcnow().isoformat(),
            'data': data
        }

        try:
            # Use user_id as partition key for ordering
            key = data.get('user_id', 'default')

            future = self.producer.send(
                TOPIC_NAME,
                value=event,
                key=key
            )

            # Wait for send to complete
            record_metadata = future.get(timeout=10)

            print(f"✅ Sent: {event_type} to partition {record_metadata.partition}")
            return True

        except KafkaError as e:
            print(f"❌ Failed to send event: {str(e)}")
            return False

    def close(self):
        """Close producer"""
        self.producer.flush()
        self.producer.close()

class EventConsumer:
    """Kafka event consumer"""

    def __init__(self, consumer_group: str = 'event-processors'):
        self.consumer = KafkaConsumer(
            TOPIC_NAME,
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            group_id=consumer_group,
            auto_offset_reset='earliest',
            enable_auto_commit=False,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            key_deserializer=lambda k: k.decode('utf-8') if k else None
        )

        self.event_handlers = {
            'user.created': self.handle_user_created,
            'user.updated': self.handle_user_updated,
            'user.deleted': self.handle_user_deleted,
            'purchase.completed': self.handle_purchase,
        }

    def handle_user_created(self, event: Dict):
        """Handle user creation event"""
        user_data = event['data']
        print(f"  👤 New user: {user_data['username']} ({user_data['email']})")
        # In production: Save to database, send welcome email, etc.

    def handle_user_updated(self, event: Dict):
        """Handle user update event"""
        user_data = event['data']
        print(f"  📝 Updated user: {user_data['user_id']}")
        # In production: Update database, invalidate cache, etc.

    def handle_user_deleted(self, event: Dict):
        """Handle user deletion event"""
        user_data = event['data']
        print(f"  🗑️  Deleted user: {user_data['user_id']}")
        # In production: Archive data, cleanup resources, etc.

    def handle_purchase(self, event: Dict):
        """Handle purchase event"""
        purchase_data = event['data']
        print(f"  💰 Purchase: ${purchase_data['amount']} by {purchase_data['user_id']}")
        # In production: Process payment, update inventory, etc.

    def process_event(self, event: Dict):
        """Process individual event"""
        event_type = event.get('event_type')
        handler = self.event_handlers.get(event_type)

        if handler:
            try:
                handler(event)
                return True
            except Exception as e:
                print(f"  ❌ Error processing {event_type}: {str(e)}")
                return False
        else:
            print(f"  ⚠️  No handler for event type: {event_type}")
            return True  # Consider it processed

    def consume(self, max_messages: int = None):
        """Consume and process events"""

        print(f"📡 Consuming events from topic: {TOPIC_NAME}")
        print("Press Ctrl+C to stop\n")

        message_count = 0

        try:
            for message in self.consumer:
                event = message.value

                print(f"\n📨 Received event: {event['event_type']}")
                print(f"   Partition: {message.partition}, Offset: {message.offset}")

                # Process event
                if self.process_event(event):
                    # Commit offset after successful processing
                    self.consumer.commit()
                else:
                    # In production: Send to dead letter queue
                    print("  ⚠️  Event processing failed, not committing offset")

                message_count += 1

                if max_messages and message_count >= max_messages:
                    break

        except KeyboardInterrupt:
            print("\n\n⏸️  Consumer stopped by user")
        finally:
            self.close()

    def close(self):
        """Close consumer"""
        self.consumer.close()

def generate_sample_events(producer: EventProducer, count: int = 20):
    """Generate sample events"""

    print(f"🎲 Generating {count} sample events...")
    print("=" * 60)

    event_types = [
        ('user.created', lambda: {
            'user_id': f"user-{random.randint(1000, 9999)}",
            'username': f"user{random.randint(100, 999)}",
            'email': f"user{random.randint(100, 999)}@example.com"
        }),
        ('user.updated', lambda: {
            'user_id': f"user-{random.randint(1000, 9999)}",
            'updates': {'last_login': datetime.utcnow().isoformat()}
        }),
        ('purchase.completed', lambda: {
            'user_id': f"user-{random.randint(1000, 9999)}",
            'amount': round(random.uniform(10, 500), 2),
            'items': random.randint(1, 5)
        }),
    ]

    for i in range(count):
        event_type, data_generator = random.choice(event_types)
        data = data_generator()

        producer.send_event(event_type, data)
        time.sleep(0.1)  # Small delay between events

    print("\n✅ Sample events generated")

def demo_producer():
    """Demo event production"""

    print("📤 Event Producer Demo")
    print("=" * 60)

    producer = EventProducer()

    try:
        # Generate sample events
        generate_sample_events(producer, count=20)

        print("\n💤 Waiting for events to be sent...")
        time.sleep(2)

    finally:
        producer.close()
        print("\n✅ Producer closed")

def demo_consumer():
    """Demo event consumption"""

    print("📥 Event Consumer Demo")
    print("=" * 60)

    consumer = EventConsumer(consumer_group='demo-consumers')

    # Consume events
    consumer.consume(max_messages=20)

def main():
    """Run complete Kafka demo"""

    print("🔄 Kafka Event Streaming Demo")
    print("=" * 60)
    print()

    import sys

    if len(sys.argv) > 1:
        mode = sys.argv[1]

        if mode == 'produce':
            demo_producer()
        elif mode == 'consume':
            demo_consumer()
        else:
            print(f"Unknown mode: {mode}")
            print("Usage: python kafka_events.py [produce|consume]")
    else:
        # Run both producer and consumer in sequence
        print("Running producer first...")
        demo_producer()

        print("\n\nNow running consumer...")
        time.sleep(2)
        demo_consumer()

if __name__ == "__main__":
    # Install: pip install kafka-python
    # Run producer: python kafka_events.py produce
    # Run consumer: python kafka_events.py consume
    main()
