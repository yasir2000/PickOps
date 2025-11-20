#!/bin/bash
# Wazuh Security Alerts Analysis
# Demonstrates: Alert monitoring, analysis, reporting

WAZUH_API="http://localhost:55000"
WAZUH_USER="wazuh"
WAZUH_PASS="wazuh"
ES_URL="http://localhost:9200"

echo "🛡️  Wazuh Security Alerts Analysis"
echo "======================================"

# Get authentication token
echo -e "\n🔐 Authenticating..."
TOKEN=$(curl -s -u $WAZUH_USER:$WAZUH_PASS -X GET "$WAZUH_API/security/user/authenticate" | jq -r '.data.token')

if [ -z "$TOKEN" ]; then
    echo "❌ Authentication failed"
    exit 1
fi

echo "✅ Authenticated"

# Function to query alerts
query_alerts() {
    local severity=$1
    local time_range=$2

    echo -e "\n📊 Querying $severity severity alerts (last $time_range)..."

    curl -s -X GET "$WAZUH_API/security/alerts?severity=$severity&time_range=$time_range" \
        -H "Authorization: Bearer $TOKEN" | jq '.data.affected_items'
}

# Check agent status
echo -e "\n📡 Checking agent status..."
curl -s -X GET "$WAZUH_API/agents?select=status,name,ip" \
    -H "Authorization: Bearer $TOKEN" | jq -r '.data.affected_items[] | "\(.name) (\(.ip)) - \(.status)"'

# Get high severity alerts
echo -e "\n🚨 High Severity Alerts (Last 24h)"
echo "======================================"

ALERTS=$(curl -s -X GET "${ES_URL}/wazuh-alerts-*/_search" \
    -H 'Content-Type: application/json' \
    -d '{
        "query": {
            "bool": {
                "must": [
                    {"range": {"@timestamp": {"gte": "now-24h"}}},
                    {"range": {"rule.level": {"gte": 10}}}
                ]
            }
        },
        "size": 10,
        "sort": [{"@timestamp": {"order": "desc"}}]
    }')

echo "$ALERTS" | jq -r '.hits.hits[] | .
._source | "[\(@timestamp)] \(rule.description) - Agent: \(agent.name)"'

# Alert statistics
echo -e "\n📈 Alert Statistics (Last 7 days)"
echo "======================================"

STATS=$(curl -s -X GET "${ES_URL}/wazuh-alerts-*/_search" \
    -H 'Content-Type: application/json' \
    -d '{
        "query": {
            "range": {"@timestamp": {"gte": "now-7d"}}
        },
        "aggs": {
            "by_severity": {
                "terms": {"field": "rule.level"}
            },
            "by_rule": {
                "terms": {"field": "rule.description.keyword", "size": 5}
            }
        },
        "size": 0
    }')

echo -e "\n🎯 Top Rules:"
echo "$STATS" | jq -r '.aggregations.by_rule.buckets[] | "  \(.doc_count) - \(.key)"'

echo -e "\n⚠️  By Severity:"
echo "$STATS" | jq -r '.aggregations.by_severity.buckets[] | "  Level \(.key): \(.doc_count) alerts"'

# Failed authentication attempts
echo -e "\n🔒 Failed Authentication Attempts"
echo "======================================"

AUTH_FAILS=$(curl -s -X GET "${ES_URL}/wazuh-alerts-*/_search" \
    -H 'Content-Type: application/json' \
    -d '{
        "query": {
            "bool": {
                "must": [
                    {"range": {"@timestamp": {"gte": "now-24h"}}},
                    {"match": {"rule.groups": "authentication_failed"}}
                ]
            }
        },
        "aggs": {
            "by_user": {
                "terms": {"field": "data.srcuser.keyword"}
            },
            "by_ip": {
                "terms": {"field": "data.srcip.keyword"}
            }
        },
        "size": 0
    }')

echo -e "\n👤 By User:"
echo "$AUTH_FAILS" | jq -r '.aggregations.by_user.buckets[] | "  \(.key): \(.doc_count) attempts"'

echo -e "\n🌐 By IP:"
echo "$AUTH_FAILS" | jq -r '.aggregations.by_ip.buckets[] | "  \(.key): \(.doc_count) attempts"'

# File integrity monitoring alerts
echo -e "\n📁 File Integrity Monitoring Alerts"
echo "======================================"

FIM_ALERTS=$(curl -s -X GET "${ES_URL}/wazuh-alerts-*/_search" \
    -H 'Content-Type: application/json' \
    -d '{
        "query": {
            "bool": {
                "must": [
                    {"range": {"@timestamp": {"gte": "now-24h"}}},
                    {"match": {"rule.groups": "syscheck"}}
                ]
            }
        },
        "size": 10
    }')

echo "$FIM_ALERTS" | jq -r '.hits.hits[] | ._source | "[\(@timestamp)] \(syscheck.path) - \(syscheck.event)"'

# Vulnerability detection
echo -e "\n🔍 Vulnerability Alerts"
echo "======================================"

VULN_ALERTS=$(curl -s -X GET "${ES_URL}/wazuh-alerts-*/_search" \
    -H 'Content-Type: application/json' \
    -d '{
        "query": {
            "bool": {
                "must": [
                    {"range": {"@timestamp": {"gte": "now-7d"}}},
                    {"match": {"rule.groups": "vulnerability-detector"}}
                ]
            }
        },
        "aggs": {
            "by_cve": {
                "terms": {"field": "data.vulnerability.cve.keyword", "size": 10}
            }
        },
        "size": 0
    }')

echo -e "\n🚨 Top CVEs:"
echo "$VULN_ALERTS" | jq -r '.aggregations.by_cve.buckets[] | "  \(.key): \(.doc_count) occurrences"'

# Generate HTML report
echo -e "\n📄 Generating HTML report..."

cat > alert_report.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>Wazuh Security Report</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1 { color: #333; }
        table { border-collapse: collapse; width: 100%; margin: 20px 0; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #4CAF50; color: white; }
        .high { color: red; font-weight: bold; }
        .medium { color: orange; }
        .low { color: green; }
    </style>
</head>
<body>
    <h1>🛡️ Wazuh Security Report</h1>
    <p>Generated: $(date)</p>

    <h2>Summary</h2>
    <p>Report covering last 24 hours of security events</p>

    <h2>High Severity Alerts</h2>
    <!-- Alert data would be inserted here -->

    <h2>Failed Authentication Attempts</h2>
    <!-- Auth data would be inserted here -->

    <h2>File Integrity Alerts</h2>
    <!-- FIM data would be inserted here -->
</body>
</html>
EOF

echo "✅ Report saved: alert_report.html"

echo -e "\n======================================"
echo "✨ Analysis complete!"
echo "======================================"
