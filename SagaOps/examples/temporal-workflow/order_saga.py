"""
Temporal Saga Workflow Example
Demonstrates: Distributed transaction, compensation, retry logic, saga pattern
"""

from datetime import timedelta
from temporalio import workflow, activity
from temporalio.client import Client
from temporalio.worker import Worker
import asyncio
from dataclasses import dataclass
from enum import Enum

# Data models
@dataclass
class OrderRequest:
    order_id: str
    user_id: str
    amount: float
    items: list

@dataclass
class PaymentResult:
    transaction_id: str
    success: bool
    message: str

@dataclass
class InventoryResult:
    reservation_id: str
    success: bool
    message: str

class OrderStatus(Enum):
    PENDING = "pending"
    PAYMENT_PROCESSING = "payment_processing"
    INVENTORY_RESERVED = "inventory_reserved"
    COMPLETED = "completed"
    FAILED = "failed"
    COMPENSATED = "compensated"

# Activities (simulating external service calls)
@activity.defn
async def process_payment(order: OrderRequest) -> PaymentResult:
    """Process payment with payment gateway"""
    print(f"💳 Processing payment for order {order.order_id}, amount: ${order.amount}")

    # Simulate payment processing
    await asyncio.sleep(1)

    # Simulate occasional failures
    import random
    if random.random() < 0.1:  # 10% failure rate
        return PaymentResult(
            transaction_id="",
            success=False,
            message="Payment declined"
        )

    return PaymentResult(
        transaction_id=f"TXN-{order.order_id}",
        success=True,
        message="Payment successful"
    )

@activity.defn
async def reserve_inventory(order: OrderRequest) -> InventoryResult:
    """Reserve inventory for order items"""
    print(f"📦 Reserving inventory for order {order.order_id}")

    await asyncio.sleep(1)

    # Simulate occasional stock issues
    import random
    if random.random() < 0.15:  # 15% failure rate
        return InventoryResult(
            reservation_id="",
            success=False,
            message="Insufficient stock"
        )

    return InventoryResult(
        reservation_id=f"RES-{order.order_id}",
        success=True,
        message="Inventory reserved"
    )

@activity.defn
async def ship_order(order: OrderRequest) -> bool:
    """Initiate order shipping"""
    print(f"🚚 Shipping order {order.order_id}")
    await asyncio.sleep(1)
    return True

@activity.defn
async def send_confirmation(order: OrderRequest) -> bool:
    """Send order confirmation to customer"""
    print(f"📧 Sending confirmation for order {order.order_id} to user {order.user_id}")
    await asyncio.sleep(0.5)
    return True

# Compensation activities (rollback operations)
@activity.defn
async def refund_payment(transaction_id: str, amount: float) -> bool:
    """Refund payment (compensation)"""
    print(f"↩️  Refunding payment {transaction_id}, amount: ${amount}")
    await asyncio.sleep(1)
    return True

@activity.defn
async def release_inventory(reservation_id: str) -> bool:
    """Release inventory reservation (compensation)"""
    print(f"↩️  Releasing inventory reservation {reservation_id}")
    await asyncio.sleep(1)
    return True

@activity.defn
async def notify_failure(order_id: str, reason: str) -> bool:
    """Notify customer of order failure"""
    print(f"📧 Notifying failure for order {order_id}: {reason}")
    await asyncio.sleep(0.5)
    return True

# Saga Workflow
@workflow.defn
class OrderSagaWorkflow:
    """
    Saga workflow for order processing
    Steps: Payment → Inventory → Shipping → Confirmation
    With compensation if any step fails
    """

    @workflow.run
    async def run(self, order: OrderRequest) -> dict:
        status = OrderStatus.PENDING
        payment_result = None
        inventory_result = None

        try:
            # Step 1: Process Payment
            workflow.logger.info(f"Starting saga for order {order.order_id}")
            status = OrderStatus.PAYMENT_PROCESSING

            payment_result = await workflow.execute_activity(
                process_payment,
                order,
                start_to_close_timeout=timedelta(seconds=30),
                retry_policy={
                    'maximum_attempts': 3,
                    'initial_interval': timedelta(seconds=1),
                    'maximum_interval': timedelta(seconds=10),
                    'backoff_coefficient': 2.0,
                }
            )

            if not payment_result.success:
                raise Exception(f"Payment failed: {payment_result.message}")

            workflow.logger.info(f"Payment successful: {payment_result.transaction_id}")

            # Step 2: Reserve Inventory
            status = OrderStatus.INVENTORY_RESERVED

            inventory_result = await workflow.execute_activity(
                reserve_inventory,
                order,
                start_to_close_timeout=timedelta(seconds=30),
                retry_policy={'maximum_attempts': 3}
            )

            if not inventory_result.success:
                # Compensate: Refund payment
                await self.compensate_payment(payment_result.transaction_id, order.amount)
                raise Exception(f"Inventory reservation failed: {inventory_result.message}")

            workflow.logger.info(f"Inventory reserved: {inventory_result.reservation_id}")

            # Step 3: Ship Order
            shipped = await workflow.execute_activity(
                ship_order,
                order,
                start_to_close_timeout=timedelta(seconds=30)
            )

            if not shipped:
                # Compensate: Release inventory and refund payment
                await self.compensate_inventory(inventory_result.reservation_id)
                await self.compensate_payment(payment_result.transaction_id, order.amount)
                raise Exception("Shipping failed")

            # Step 4: Send Confirmation
            await workflow.execute_activity(
                send_confirmation,
                order,
                start_to_close_timeout=timedelta(seconds=10)
            )

            status = OrderStatus.COMPLETED
            workflow.logger.info(f"Order {order.order_id} completed successfully")

            return {
                'order_id': order.order_id,
                'status': status.value,
                'payment_transaction_id': payment_result.transaction_id,
                'inventory_reservation_id': inventory_result.reservation_id,
                'message': 'Order processed successfully'
            }

        except Exception as e:
            # Saga failed - run compensation
            workflow.logger.error(f"Saga failed for order {order.order_id}: {str(e)}")

            # Notify customer
            await workflow.execute_activity(
                notify_failure,
                args=[order.order_id, str(e)],
                start_to_close_timeout=timedelta(seconds=10)
            )

            status = OrderStatus.COMPENSATED

            return {
                'order_id': order.order_id,
                'status': status.value,
                'message': f'Order failed: {str(e)}',
                'error': str(e)
            }

    async def compensate_payment(self, transaction_id: str, amount: float):
        """Compensation: Refund payment"""
        await workflow.execute_activity(
            refund_payment,
            args=[transaction_id, amount],
            start_to_close_timeout=timedelta(seconds=30)
        )

    async def compensate_inventory(self, reservation_id: str):
        """Compensation: Release inventory"""
        await workflow.execute_activity(
            release_inventory,
            reservation_id,
            start_to_close_timeout=timedelta(seconds=30)
        )

async def main():
    """Run Temporal saga workflow example"""

    print("🔄 Temporal Saga Workflow Demo")
    print("=" * 60)

    # Connect to Temporal server
    client = await Client.connect("localhost:7233")

    # Create worker
    worker = Worker(
        client,
        task_queue="order-saga-queue",
        workflows=[OrderSagaWorkflow],
        activities=[
            process_payment,
            reserve_inventory,
            ship_order,
            send_confirmation,
            refund_payment,
            release_inventory,
            notify_failure
        ]
    )

    # Start worker in background
    print("\n🔧 Starting Temporal worker...")
    async with worker:
        # Example orders
        orders = [
            OrderRequest(
                order_id="ORD-001",
                user_id="user-123",
                amount=99.99,
                items=["item1", "item2"]
            ),
            OrderRequest(
                order_id="ORD-002",
                user_id="user-456",
                amount=149.99,
                items=["item3"]
            ),
            OrderRequest(
                order_id="ORD-003",
                user_id="user-789",
                amount=199.99,
                items=["item4", "item5", "item6"]
            ),
        ]

        print("\n" + "=" * 60)
        print("Executing Saga Workflows")
        print("=" * 60)

        results = []

        for order in orders:
            print(f"\n🛍️  Processing order {order.order_id}...")
            print("-" * 60)

            # Execute workflow
            result = await client.execute_workflow(
                OrderSagaWorkflow.run,
                order,
                id=f"order-saga-{order.order_id}",
                task_queue="order-saga-queue",
            )

            results.append(result)

            if result['status'] == OrderStatus.COMPLETED.value:
                print(f"✅ {result['message']}")
            else:
                print(f"❌ {result['message']}")

        # Summary
        print("\n" + "=" * 60)
        print("📊 Summary")
        print("=" * 60)

        successful = sum(1 for r in results if r['status'] == OrderStatus.COMPLETED.value)
        failed = len(results) - successful

        print(f"\nTotal orders: {len(results)}")
        print(f"Successful: {successful}")
        print(f"Failed (compensated): {failed}")

        print("\n" + "=" * 60)
        print("✨ Saga demo complete!")
        print("=" * 60)

if __name__ == "__main__":
    # Install: pip install temporalio
    asyncio.run(main())
