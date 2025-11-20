"""
IT Service Management Automation
Demonstrates: Ticket creation, incident management, service monitoring
"""

import requests
import json
from datetime import datetime
from typing import Dict, List, Any
from enum import Enum

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

class TicketStatus(Enum):
    NEW = "new"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"

class ITServiceManager:
    """IT Service Management operations"""

    def __init__(self, api_url: str = "http://localhost:8080/api"):
        self.api_url = api_url
        self.session = requests.Session()

    def create_ticket(self, title: str, description: str, priority: Priority, category: str) -> Dict:
        """Create IT service ticket"""

        ticket = {
            'ticket_id': f"INC-{int(datetime.now().timestamp())}",
            'title': title,
            'description': description,
            'priority': priority.name,
            'category': category,
            'status': TicketStatus.NEW.value,
            'created_at': datetime.now().isoformat(),
            'assigned_to': None,
            'resolution': None
        }

        print(f"📝 Creating ticket: {ticket['ticket_id']}")
        print(f"   Title: {title}")
        print(f"   Priority: {priority.name}")

        # In production, would POST to API
        # response = self.session.post(f"{self.api_url}/tickets", json=ticket)

        return ticket

    def update_ticket(self, ticket_id: str, updates: Dict) -> Dict:
        """Update ticket"""

        print(f"🔄 Updating ticket: {ticket_id}")
        for key, value in updates.items():
            print(f"   {key}: {value}")

        # In production, would PATCH to API
        # response = self.session.patch(f"{self.api_url}/tickets/{ticket_id}", json=updates)

        return updates

    def assign_ticket(self, ticket_id: str, assignee: str):
        """Assign ticket to engineer"""

        print(f"👤 Assigning {ticket_id} to {assignee}")

        return self.update_ticket(ticket_id, {
            'assigned_to': assignee,
            'status': TicketStatus.IN_PROGRESS.value
        })

    def resolve_ticket(self, ticket_id: str, resolution: str):
        """Resolve ticket"""

        print(f"✅ Resolving ticket: {ticket_id}")
        print(f"   Resolution: {resolution}")

        return self.update_ticket(ticket_id, {
            'status': TicketStatus.RESOLVED.value,
            'resolution': resolution,
            'resolved_at': datetime.now().isoformat()
        })

    def monitor_services(self) -> List[Dict]:
        """Monitor IT services health"""

        print("\n🔍 Monitoring services...")
        print("=" * 60)

        services = [
            {
                'name': 'Email Server',
                'status': 'healthy',
                'uptime': '99.9%',
                'response_time': '45ms'
            },
            {
                'name': 'File Server',
                'status': 'healthy',
                'uptime': '99.7%',
                'response_time': '12ms'
            },
            {
                'name': 'VPN Gateway',
                'status': 'degraded',
                'uptime': '98.5%',
                'response_time': '230ms'
            },
            {
                'name': 'Database',
                'status': 'healthy',
                'uptime': '99.95%',
                'response_time': '8ms'
            },
        ]

        for service in services:
            status_icon = '✅' if service['status'] == 'healthy' else '⚠️'
            print(f"{status_icon} {service['name']:20} | "
                  f"Uptime: {service['uptime']:6} | "
                  f"Response: {service['response_time']:6}")

        return services

    def create_incident_report(self, services: List[Dict]) -> Dict:
        """Create incident report for degraded services"""

        degraded = [s for s in services if s['status'] != 'healthy']

        if not degraded:
            print("\n✅ All services healthy - no incidents")
            return None

        print(f"\n⚠️  Found {len(degraded)} degraded services")

        report = {
            'report_id': f"RPT-{int(datetime.now().timestamp())}",
            'created_at': datetime.now().isoformat(),
            'total_services': len(services),
            'degraded_services': len(degraded),
            'incidents': []
        }

        for service in degraded:
            incident = {
                'service': service['name'],
                'status': service['status'],
                'impact': 'Medium',
                'action': f"Investigating {service['name']} performance"
            }
            report['incidents'].append(incident)

            # Auto-create ticket
            ticket = self.create_ticket(
                title=f"{service['name']} Performance Degradation",
                description=f"Service showing degraded performance. Response time: {service['response_time']}",
                priority=Priority.HIGH,
                category="Performance"
            )
            incident['ticket_id'] = ticket['ticket_id']

        return report

def demo_change_management():
    """Demo change management workflow"""

    print("\n📋 Change Management Workflow")
    print("=" * 60)

    sm = ITServiceManager()

    # Create change request
    change = {
        'change_id': f"CHG-{int(datetime.now().timestamp())}",
        'title': 'Upgrade database to v14',
        'requestor': 'john.doe@company.com',
        'impact': 'Medium',
        'risk': 'Low',
        'scheduled_date': '2024-01-15T02:00:00Z',
        'estimated_duration': '2 hours',
        'rollback_plan': 'Restore from snapshot',
        'approval_status': 'pending'
    }

    print(f"📝 Change Request: {change['change_id']}")
    print(f"   Title: {change['title']}")
    print(f"   Impact: {change['impact']}")
    print(f"   Risk: {change['risk']}")
    print(f"   Scheduled: {change['scheduled_date']}")

    # Approval workflow
    print(f"\n✅ Change approved by CAB")
    change['approval_status'] = 'approved'

    # Implementation
    print(f"🔧 Implementing change...")
    print(f"   Taking database snapshot...")
    print(f"   Upgrading database...")
    print(f"   Running tests...")
    print(f"   ✅ Change successful!")

    change['status'] = 'completed'
    change['completed_at'] = datetime.now().isoformat()

    return change

def main():
    """Run ITSM automation demo"""

    print("🎫 IT Service Management Automation")
    print("=" * 60)

    sm = ITServiceManager()

    # 1. Monitor services
    services = sm.monitor_services()

    # 2. Create incident report
    report = sm.create_incident_report(services)

    if report:
        print("\n📊 Incident Report:")
        print(f"   Report ID: {report['report_id']}")
        print(f"   Degraded Services: {report['degraded_services']}/{report['total_services']}")

        for incident in report['incidents']:
            print(f"\n   - {incident['service']}")
            print(f"     Ticket: {incident['ticket_id']}")
            print(f"     Action: {incident['action']}")

    # 3. Manual ticket workflow
    print("\n" + "=" * 60)
    print("Ticket Workflow Demo")
    print("=" * 60)

    # Create ticket
    ticket = sm.create_ticket(
        title="User cannot access email",
        description="User reports unable to login to email since this morning",
        priority=Priority.MEDIUM,
        category="Email"
    )

    # Assign ticket
    sm.assign_ticket(ticket['ticket_id'], "support@company.com")

    # Resolve ticket
    sm.resolve_ticket(
        ticket['ticket_id'],
        "Password reset required. User credentials updated and email access restored."
    )

    # 4. Change management
    change = demo_change_management()

    # Summary
    print("\n" + "=" * 60)
    print("📊 Summary")
    print("=" * 60)

    if report:
        print(f"\nIncidents created: {len(report['incidents'])}")
        for inc in report['incidents']:
            print(f"  - {inc['ticket_id']}: {inc['service']}")

    print(f"\nChange {change['change_id']}: {change['status']}")
    print(f"\n✅ ITSM automation complete!")

if __name__ == "__main__":
    # Install: pip install requests
    main()
