"""
Cloud Cost Analysis and Optimization
Demonstrates: Cost tracking, budget alerts, resource optimization recommendations
"""

import boto3
from datetime import datetime, timedelta
from typing import Dict, List, Any
import json

class CloudCostAnalyzer:
    """Analyze and optimize cloud costs"""

    def __init__(self):
        self.ce_client = boto3.client('ce')  # Cost Explorer
        self.ec2_client = boto3.client('ec2')
        self.rds_client = boto3.client('rds')

    def get_cost_and_usage(self, days: int = 30) -> Dict[str, Any]:
        """Get cost and usage for the past N days"""

        print(f"💰 Analyzing costs for the past {days} days...")

        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=days)

        response = self.ce_client.get_cost_and_usage(
            TimePeriod={
                'Start': start_date.strftime('%Y-%m-%d'),
                'End': end_date.strftime('%Y-%m-%d')
            },
            Granularity='DAILY',
            Metrics=['UnblendedCost', 'UsageQuantity'],
            GroupBy=[
                {'Type': 'DIMENSION', 'Key': 'SERVICE'}
            ]
        )

        return response

    def analyze_cost_by_service(self, cost_data: Dict) -> List[Dict]:
        """Analyze costs grouped by service"""

        print("\n📊 Cost breakdown by service:")
        print("=" * 60)

        service_costs = {}

        for result in cost_data['ResultsByTime']:
            for group in result['Groups']:
                service = group['Keys'][0]
                cost = float(group['Metrics']['UnblendedCost']['Amount'])

                if service not in service_costs:
                    service_costs[service] = 0
                service_costs[service] += cost

        # Sort by cost
        sorted_services = sorted(
            service_costs.items(),
            key=lambda x: x[1],
            reverse=True
        )

        total_cost = sum(service_costs.values())

        for service, cost in sorted_services[:10]:  # Top 10
            percentage = (cost / total_cost) * 100
            print(f"  {service:30} ${cost:10.2f} ({percentage:5.1f}%)")

        print(f"\n  {'TOTAL':30} ${total_cost:10.2f}")

        return sorted_services

    def get_cost_forecast(self, days: int = 30) -> Dict:
        """Get cost forecast for next N days"""

        print(f"\n🔮 Cost forecast for next {days} days...")

        start_date = datetime.now().date()
        end_date = start_date + timedelta(days=days)

        response = self.ce_client.get_cost_forecast(
            TimePeriod={
                'Start': start_date.strftime('%Y-%m-%d'),
                'End': end_date.strftime('%Y-%m-%d')
            },
            Metric='UNBLENDED_COST',
            Granularity='MONTHLY'
        )

        forecast = float(response['Total']['Amount'])
        print(f"  Forecasted cost: ${forecast:.2f}")

        return response

    def find_idle_resources(self) -> List[Dict]:
        """Find idle/underutilized resources"""

        print("\n🔍 Scanning for idle resources...")
        print("=" * 60)

        recommendations = []

        # 1. Stopped EC2 instances
        print("\n1️⃣  Checking EC2 instances...")
        ec2_response = self.ec2_client.describe_instances()

        for reservation in ec2_response['Reservations']:
            for instance in reservation['Instances']:
                if instance['State']['Name'] == 'stopped':
                    recommendations.append({
                        'type': 'EC2',
                        'resource_id': instance['InstanceId'],
                        'issue': 'Stopped instance',
                        'recommendation': 'Terminate if no longer needed',
                        'potential_savings': '~$50/month'
                    })

        # 2. Unattached EBS volumes
        print("2️⃣  Checking EBS volumes...")
        volumes = self.ec2_client.describe_volumes()

        for volume in volumes['Volumes']:
            if volume['State'] == 'available':
                size = volume['Size']
                monthly_cost = size * 0.10  # ~$0.10 per GB-month
                recommendations.append({
                    'type': 'EBS',
                    'resource_id': volume['VolumeId'],
                    'issue': f'Unattached {size}GB volume',
                    'recommendation': 'Delete if snapshot exists',
                    'potential_savings': f'${monthly_cost:.2f}/month'
                })

        # 3. Idle RDS instances
        print("3️⃣  Checking RDS instances...")
        try:
            rds_instances = self.rds_client.describe_db_instances()

            for db in rds_instances['DBInstances']:
                # Check if instance has low CPU (would need CloudWatch)
                # For demo, flag non-production instances
                if 'dev' in db['DBInstanceIdentifier'].lower():
                    recommendations.append({
                        'type': 'RDS',
                        'resource_id': db['DBInstanceIdentifier'],
                        'issue': 'Development database running continuously',
                        'recommendation': 'Stop during non-business hours',
                        'potential_savings': '~$100/month'
                    })
        except:
            pass  # RDS permissions might not be available

        # Display recommendations
        print(f"\n📋 Found {len(recommendations)} optimization opportunities:")
        for i, rec in enumerate(recommendations, 1):
            print(f"\n  {i}. {rec['type']} - {rec['resource_id']}")
            print(f"     Issue: {rec['issue']}")
            print(f"     Recommendation: {rec['recommendation']}")
            print(f"     Potential savings: {rec['potential_savings']}")

        return recommendations

    def check_budget_alerts(self, budget_limit: float) -> Dict:
        """Check if spending is approaching budget limit"""

        print(f"\n💵 Checking budget (limit: ${budget_limit})...")

        # Get current month spending
        start_date = datetime.now().replace(day=1).date()
        end_date = datetime.now().date()

        response = self.ce_client.get_cost_and_usage(
            TimePeriod={
                'Start': start_date.strftime('%Y-%m-%d'),
                'End': end_date.strftime('%Y-%m-%d')
            },
            Granularity='MONTHLY',
            Metrics=['UnblendedCost']
        )

        current_spend = float(response['ResultsByTime'][0]['Total']['UnblendedCost']['Amount'])
        percentage = (current_spend / budget_limit) * 100

        print(f"  Current spend: ${current_spend:.2f}")
        print(f"  Budget usage: {percentage:.1f}%")

        if percentage >= 90:
            print("  🚨 ALERT: Budget usage above 90%!")
        elif percentage >= 75:
            print("  ⚠️  WARNING: Budget usage above 75%")
        else:
            print("  ✅ Budget usage healthy")

        return {
            'current_spend': current_spend,
            'budget_limit': budget_limit,
            'percentage_used': percentage
        }

    def generate_cost_report(self, output_file: str = 'cost_report.json'):
        """Generate comprehensive cost report"""

        print("\n📄 Generating cost report...")

        # Gather all data
        cost_data = self.get_cost_and_usage(30)
        service_costs = self.analyze_cost_by_service(cost_data)
        forecast = self.get_cost_forecast(30)
        recommendations = self.find_idle_resources()
        budget_status = self.check_budget_alerts(1000.0)

        # Create report
        report = {
            'generated_at': datetime.now().isoformat(),
            'period': '30 days',
            'top_services': [
                {'service': s[0], 'cost': s[1]}
                for s in service_costs[:10]
            ],
            'forecast': {
                'amount': float(forecast['Total']['Amount']),
                'period': '30 days'
            },
            'budget_status': budget_status,
            'optimization_recommendations': recommendations,
            'total_potential_savings': sum(
                float(rec['potential_savings'].replace('$', '').replace('/month', '').replace('~', ''))
                for rec in recommendations
                if '$' in rec['potential_savings']
            )
        }

        # Save report
        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)

        print(f"\n✅ Report saved to {output_file}")

        return report

def main():
    """Run cost analysis demo"""

    print("💰 Cloud Cost Analysis & Optimization")
    print("=" * 60)

    try:
        analyzer = CloudCostAnalyzer()

        # Generate comprehensive report
        report = analyzer.generate_cost_report()

        # Summary
        print("\n" + "=" * 60)
        print("📊 Summary")
        print("=" * 60)
        print(f"\nTop spending service: {report['top_services'][0]['service']}")
        print(f"Amount: ${report['top_services'][0]['cost']:.2f}")
        print(f"\n30-day forecast: ${report['forecast']['amount']:.2f}")
        print(f"Budget usage: {report['budget_status']['percentage_used']:.1f}%")
        print(f"\nOptimization opportunities: {len(report['optimization_recommendations'])}")
        print(f"Potential monthly savings: ${report['total_potential_savings']:.2f}")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("\n⚠️  Make sure AWS credentials are configured:")
        print("   aws configure")
        print("\n   And Cost Explorer API is enabled in AWS Console")

if __name__ == "__main__":
    # Install: pip install boto3
    # Configure: aws configure
    main()
