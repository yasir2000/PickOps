#!/bin/bash
# Container Security Scanning with Trivy
# Demonstrates: Vulnerability scanning, compliance checks, SBOM generation

echo "🔒 Container Security Scanning with Trivy"
echo "=========================================="

# Install Trivy if not present
if ! command -v trivy &> /dev/null; then
    echo "📦 Installing Trivy..."
    wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | apt-key add -
    echo "deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main" | tee -a /etc/apt/sources.list.d/trivy.list
    apt-get update && apt-get install -y trivy
fi

# Example Docker image to scan
IMAGE="nginx:latest"

echo ""
echo "🐳 Scanning image: $IMAGE"
echo "=========================================="

# 1. Vulnerability scan
echo -e "\n1️⃣  Running vulnerability scan..."
trivy image \
    --severity HIGH,CRITICAL \
    --format table \
    --output scan_results.txt \
    $IMAGE

# 2. Generate JSON report
echo -e "\n2️⃣  Generating JSON report..."
trivy image \
    --format json \
    --output scan_results.json \
    $IMAGE

# 3. Generate SBOM
echo -e "\n3️⃣  Generating SBOM (Software Bill of Materials)..."
trivy image \
    --format cyclonedx \
    --output sbom.json \
    $IMAGE

# 4. Check for misconfigurations
echo -e "\n4️⃣  Checking for misconfigurations..."
trivy config ./Dockerfile --exit-code 1 || true

# 5. Secret scanning
echo -e "\n5️⃣  Scanning for secrets..."
trivy fs --scanners secret ./ || true

# Parse and display summary
echo ""
echo "=========================================="
echo "📊 Scan Summary"
echo "=========================================="

if [ -f scan_results.json ]; then
    echo ""
    echo "Vulnerabilities by severity:"
    jq -r '.Results[0].Vulnerabilities | group_by(.Severity) | map({severity: .[0].Severity, count: length}) | .[] | "\(.severity): \(.count)"' scan_results.json 2>/dev/null || echo "No vulnerabilities found"

    echo ""
    echo "Top 5 critical vulnerabilities:"
    jq -r '.Results[0].Vulnerabilities | map(select(.Severity == "CRITICAL")) | .[:5] | .[] | "  - \(.VulnerabilityID): \(.PkgName) \(.InstalledVersion) -> \(.FixedVersion // "no fix")"' scan_results.json 2>/dev/null || echo "None"
fi

echo ""
echo "✅ Files generated:"
echo "  - scan_results.txt (human-readable)"
echo "  - scan_results.json (machine-readable)"
echo "  - sbom.json (SBOM in CycloneDX format)"
echo ""
