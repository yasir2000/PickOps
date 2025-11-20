# Temporal Saga Workflow Example

Distributed transaction management using the saga pattern with Temporal.

## What it does

Implements an e-commerce order saga with:
- Payment processing
- Inventory reservation
- Order shipping
- Customer notification
- Automatic compensation on failure

## Features

- **Distributed Transaction**: Coordinates multiple services
- **Compensation Logic**: Automatic rollback on failures
- **Retry Policies**: Configurable retry strategies
- **Event Tracking**: Full audit trail of saga execution
- **Error Handling**: Graceful failure recovery

## Saga Steps

1. **Process Payment** → Compensate: Refund
2. **Reserve Inventory** → Compensate: Release reservation
3. **Ship Order** → Compensate: Cancel shipment
4. **Send Confirmation** → No compensation needed

## Usage

```bash
# Install dependencies
pip install temporalio

# Start Temporal server (in docker-compose)
cd ../..
docker-compose up -d

# Run the saga workflow
python order_saga.py

# The script will:
# - Start Temporal worker
# - Execute 3 sample orders
# - Show saga progression
# - Handle failures with compensation
```

## Example Output

```
🔄 Temporal Saga Workflow Demo
=============================================================

🔧 Starting Temporal worker...

=============================================================
Executing Saga Workflows
=============================================================

🛍️  Processing order ORD-001...
-------------------------------------------------------------
💳 Processing payment for order ORD-001, amount: $99.99
📦 Reserving inventory for order ORD-001
🚚 Shipping order ORD-001
📧 Sending confirmation for order ORD-001 to user user-123
✅ Order processed successfully

📊 Summary
=============================================================
Total orders: 3
Successful: 2
Failed (compensated): 1
```

## Failure Scenarios

The demo simulates:
- Payment failures (10% rate)
- Inventory shortages (15% rate)
- Automatic compensation when failures occur

## Architecture

```
┌─────────────┐
│   Temporal  │
│   Server    │
└──────┬──────┘
       │
┌──────▼──────────────────────────────┐
│     Order Saga Workflow             │
├─────────────────────────────────────┤
│  ┌──────────────────────────────┐  │
│  │ 1. Process Payment           │  │
│  │    Compensate: Refund        │  │
│  └───────────┬──────────────────┘  │
│              ▼                      │
│  ┌──────────────────────────────┐  │
│  │ 2. Reserve Inventory         │  │
│  │    Compensate: Release       │  │
│  └───────────┬──────────────────┘  │
│              ▼                      │
│  ┌──────────────────────────────┐  │
│  │ 3. Ship Order                │  │
│  └───────────┬──────────────────┘  │
│              ▼                      │
│  ┌──────────────────────────────┐  │
│  │ 4. Send Confirmation         │  │
│  └──────────────────────────────┘  │
└─────────────────────────────────────┘
```
