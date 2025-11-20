# Kafka Producer-Consumer Example

Event-driven messaging with Kafka for real-time data processing.

## What it does

Implements a complete Kafka event system:
- Device event producer
- Event consumer with processing
- Event handlers by type
- Error handling and retries
- Offset management

## Event Types

- `user.created` - New user registration
- `user.updated` - User profile updates
- `user.deleted` - User account deletion
- `purchase.completed` - Purchase transactions

## Usage

```bash
# Install dependencies
pip install kafka-python

# Start Kafka (in docker-compose)
cd ../..
docker-compose up -d

# Terminal 1: Start consumer
python kafka_events.py consume

# Terminal 2: Start producer
python kafka_events.py produce

# Or run both sequentially
python kafka_events.py
```

## Architecture

```
┌──────────────┐
│   Producer   │──┐
└──────────────┘  │
                  │
┌──────────────┐  │     ┌─────────────────┐
│   Producer   │──┼────▶│  Kafka Broker   │
└──────────────┘  │     │  Topic: events  │
                  │     └────────┬────────┘
┌──────────────┐  │              │
│   Producer   │──┘              │
└──────────────┘                 │
                                 │
                    ┌────────────▼─────────────┐
                    │   Consumer Group         │
                    │  ┌─────────────────────┐ │
                    │  │ Event Processor     │ │
                    │  │ - user.created      │ │
                    │  │ - user.updated      │ │
                    │  │ - purchase.*        │ │
                    │  └─────────────────────┘ │
                    └──────────────────────────┘
```

## Features

### Producer
- Automatic partitioning by user_id
- JSON serialization
- Delivery confirmation
- Error retry logic

### Consumer
- Consumer group coordination
- Manual offset commits
- Event type routing
- Error handling
- Graceful shutdown

## Example Output

```
📤 Event Producer Demo
============================================================
🎲 Generating 20 sample events...
✅ Sent: user.created to partition 2
✅ Sent: purchase.completed to partition 1
✅ Sent: user.updated to partition 0
...

📥 Event Consumer Demo
============================================================
📡 Consuming events from topic: user-events

📨 Received event: user.created
   Partition: 2, Offset: 15
  👤 New user: user456 (user456@example.com)

📨 Received event: purchase.completed
   Partition: 1, Offset: 8
  💰 Purchase: $127.45 by user-1234
```

## Configuration

Key settings:
- `acks='all'` - Wait for all replicas
- `retries=3` - Retry failed sends
- `qos=1` - At-least-once delivery
- `enable_auto_commit=False` - Manual offset control
