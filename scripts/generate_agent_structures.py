#!/usr/bin/env python3
"""
generate_agent_structures.py
Generates .agent/ directory with domain-specific agent definition files
for every *Ops folder in PickOps.

Files created per folder:
  .agent/
    agent.md          – Agent identity, persona, role
    skills.md         – Domain-specific skills
    capabilities.md   – Concrete capabilities / actions
    intents.md        – Supported user intents
    tools.md          – Tools & integrations
    workflows.md      – Agent workflow patterns
    config.yaml       – Machine-readable agent config
    prompts/
      system.md       – System prompt for this domain agent
      examples.md     – Few-shot prompt examples
"""

import os
import textwrap
from pathlib import Path

ROOT = Path(__file__).parent.parent

# ─────────────────────────────────────────────────────────────────────────────
# Domain metadata: (full_name, emoji, description, skills[], capabilities[],
#                   intents[], tools[], workflows[])
# ─────────────────────────────────────────────────────────────────────────────
DOMAINS = {
    "AgentOps": {
        "name": "AI Agent Operations",
        "emoji": "🤖",
        "desc": "Orchestrate, monitor, and govern autonomous AI agents across multi-agent systems.",
        "skills": ["Agent orchestration", "Multi-agent coordination", "Tool-use design", "Agent evaluation", "Memory management", "Prompt engineering"],
        "capabilities": ["Spawn and terminate agents", "Route tasks between agents", "Monitor agent traces", "Evaluate agent quality", "Manage agent memory stores", "Debug agent reasoning chains"],
        "intents": ["Deploy a new agent", "Monitor agent performance", "Debug a failing agent", "Chain agents together", "Evaluate agent output quality", "Add a new tool to an agent"],
        "tools": ["LangGraph", "CrewAI", "AutoGen", "LangSmith", "Ollama", "OpenAI API", "Redis", "PostgreSQL", "Temporal"],
        "workflows": ["supervisor-subagent", "sequential-chain", "parallel-fan-out", "human-in-the-loop", "reflection-loop"],
    },
    "AgriOps": {
        "name": "Agricultural Operations",
        "emoji": "🌾",
        "desc": "Automate and optimize crop management, irrigation, soil monitoring, and harvest planning.",
        "skills": ["Crop lifecycle management", "Precision irrigation", "Soil analysis", "Pest detection", "Yield forecasting", "Supply chain coordination"],
        "capabilities": ["Monitor soil sensors", "Schedule irrigation cycles", "Detect crop disease via image analysis", "Forecast yield from weather data", "Optimize fertilizer dosing", "Coordinate with logistics for harvest"],
        "intents": ["Check soil moisture levels", "Plan irrigation schedule", "Detect disease in crop images", "Forecast this season's yield", "Optimize fertilizer application", "Track farm equipment"],
        "tools": ["MQTT", "InfluxDB", "Grafana", "TensorFlow Lite", "OpenWeatherMap API", "AgroMonitoring API", "PostgreSQL", "MinIO"],
        "workflows": ["sensor-ingest-alert", "image-classification-pipeline", "yield-forecast-report", "automated-irrigation-control"],
    },
    "AIOps": {
        "name": "AI for IT Operations",
        "emoji": "🧠",
        "desc": "Apply machine learning to automate IT event correlation, anomaly detection, and root-cause analysis.",
        "skills": ["Anomaly detection", "Log analysis", "Event correlation", "Predictive alerting", "ITSM automation", "Capacity forecasting"],
        "capabilities": ["Detect infrastructure anomalies in real time", "Correlate alerts across systems", "Predict incidents before they occur", "Auto-remediate known failure patterns", "Generate RCA reports", "Forecast capacity needs"],
        "intents": ["Why is there a spike in errors?", "Predict next week's capacity needs", "Correlate alerts from multiple sources", "Auto-remediate high CPU", "Generate an incident RCA", "Reduce alert noise"],
        "tools": ["Prometheus", "Grafana", "Elasticsearch", "Kafka", "Scikit-learn", "Prophet", "PagerDuty API", "Temporal"],
        "workflows": ["anomaly-detection-pipeline", "alert-correlation-engine", "auto-remediation-loop", "capacity-forecast-report"],
    },
    "AirOps": {
        "name": "Aviation Operations",
        "emoji": "✈️",
        "desc": "Manage flight operations, maintenance scheduling, crew planning, and safety compliance.",
        "skills": ["Flight scheduling", "MRO planning", "Crew rostering", "Safety compliance", "Fuel optimization", "ATC communication"],
        "capabilities": ["Schedule flights and crew", "Track aircraft maintenance windows", "Monitor safety compliance checklists", "Optimize fuel loads", "Parse NOTAMs", "Generate flight briefing documents"],
        "intents": ["Schedule crew for next week", "Check aircraft maintenance status", "Parse incoming NOTAM", "Calculate optimal fuel load", "Generate pre-flight safety checklist", "Report a safety incident"],
        "tools": ["PostgreSQL", "Redis", "Celery", "FastAPI", "Aviation Weather API", "ACARS integration", "PDF generator"],
        "workflows": ["crew-scheduling-optimization", "maintenance-tracking", "notam-parsing-alert", "safety-audit-pipeline"],
    },
    "ALMOps": {
        "name": "Application Lifecycle Management Operations",
        "emoji": "🔄",
        "desc": "Govern the full application lifecycle from requirements through retirement.",
        "skills": ["Requirements traceability", "Release governance", "Change management", "Portfolio planning", "Technical debt tracking", "Compliance reporting"],
        "capabilities": ["Track requirements to code", "Manage release gates", "Enforce change advisory boards", "Generate compliance reports", "Measure technical debt", "Plan portfolio roadmaps"],
        "intents": ["Trace requirement to test", "Approve a change request", "Generate release notes", "Measure technical debt", "Plan next quarter roadmap", "Audit compliance status"],
        "tools": ["Jira API", "GitLab API", "SonarQube", "Confluence API", "PostgreSQL", "Grafana"],
        "workflows": ["change-request-approval", "release-gate-pipeline", "compliance-audit-report", "debt-measurement-sprint"],
    },
    "AnimOps": {
        "name": "Animation & Media Operations",
        "emoji": "🎬",
        "desc": "Automate render pipelines, asset management, and production scheduling for animation studios.",
        "skills": ["Render farm management", "Asset pipeline automation", "Scene versioning", "Resource scheduling", "Quality review automation", "Deadline integration"],
        "capabilities": ["Submit and monitor render jobs", "Version and store 3D assets", "Schedule artist workloads", "Auto-QA rendered frames", "Integrate with Deadline/Tractor", "Notify team of render completion"],
        "intents": ["Submit render job", "Check render status", "Find latest version of asset", "Schedule artist tasks", "Flag frame quality issues", "Generate production report"],
        "tools": ["AWS Thinkbox Deadline", "MinIO", "PostgreSQL", "Redis", "FFmpeg", "Pillow", "Slack API", "FastAPI"],
        "workflows": ["render-job-submission", "asset-version-pipeline", "qa-frame-review", "production-daily-report"],
    },
    "AppOps": {
        "name": "Application Operations",
        "emoji": "📱",
        "desc": "Operate, monitor, and release web and mobile applications with SRE best practices.",
        "skills": ["Deployment automation", "Feature flag management", "Error tracking", "Performance monitoring", "A/B testing", "Rollback orchestration"],
        "capabilities": ["Deploy applications with zero downtime", "Manage feature flags", "Aggregate and triage errors", "Monitor Core Web Vitals", "Run A/B experiments", "Roll back bad deployments"],
        "intents": ["Deploy new version", "Toggle feature flag", "Investigate error spike", "Check app performance", "Set up A/B test", "Roll back last deployment"],
        "tools": ["LaunchDarkly", "Sentry", "Datadog", "Vercel API", "GitHub Actions API", "PostHog", "Redis"],
        "workflows": ["blue-green-deploy", "canary-release", "error-triage-loop", "ab-experiment-lifecycle"],
    },
    "ArchaOps": {
        "name": "Archaeological Operations",
        "emoji": "🏺",
        "desc": "Digitize, classify, and manage archaeological finds, excavation data, and heritage records.",
        "skills": ["Artifact classification", "Excavation data management", "GIS mapping", "Heritage compliance", "3D scanning pipeline", "Research publication workflow"],
        "capabilities": ["Classify artifacts using computer vision", "Log excavation data with GPS coordinates", "Generate GIS maps of sites", "Track heritage compliance", "Process 3D scan files", "Export research datasets"],
        "intents": ["Log new artifact find", "Map excavation site", "Classify artifact by image", "Check heritage compliance", "Export site data", "Generate excavation report"],
        "tools": ["PostgreSQL + PostGIS", "QGIS API", "MinIO", "TensorFlow", "OpenCV", "FastAPI", "Leaflet.js"],
        "workflows": ["artifact-ingest-classify", "site-mapping-pipeline", "heritage-compliance-check", "research-export"],
    },
    "ArchiOps": {
        "name": "Architecture & Design Operations",
        "emoji": "🏛️",
        "desc": "Manage architectural design workflows, BIM models, project coordination, and compliance review.",
        "skills": ["BIM management", "Drawing versioning", "Regulatory compliance", "Project coordination", "Cost estimation", "Sustainability analysis"],
        "capabilities": ["Version and store BIM models", "Review regulatory compliance", "Coordinate multi-discipline projects", "Generate cost estimates", "Analyse building energy performance", "Produce drawing packages"],
        "intents": ["Upload new BIM model", "Check planning compliance", "Coordinate with structural team", "Estimate project cost", "Review energy performance", "Produce drawing set"],
        "tools": ["MinIO", "PostgreSQL", "IFC.js", "Autodesk Forge API", "FastAPI", "React", "PDF generator"],
        "workflows": ["bim-version-review", "compliance-check-pipeline", "multi-discipline-coordination", "drawing-package-export"],
    },
    "AutoOps": {
        "name": "Automotive Operations",
        "emoji": "🚗",
        "desc": "Automate vehicle fleet management, predictive maintenance, telematics, and EV charging operations.",
        "skills": ["Fleet telematics", "Predictive maintenance", "EV charging management", "Route optimization", "OTA update management", "Warranty analytics"],
        "capabilities": ["Track vehicle location and health", "Predict component failures", "Manage EV charging schedules", "Optimize delivery routes", "Push OTA firmware updates", "Analyse warranty claims"],
        "intents": ["Check fleet status", "Predict next maintenance", "Schedule EV charging", "Optimize delivery route", "Push software update", "Analyse warranty claims"],
        "tools": ["MQTT", "InfluxDB", "PostgreSQL", "Grafana", "HERE API", "FastAPI", "Kafka", "Redis"],
        "workflows": ["telematics-ingest-pipeline", "predictive-maintenance-model", "ota-update-rollout", "route-optimization-job"],
    },
    "AviOps": {
        "name": "Avionics Operations",
        "emoji": "🛩️",
        "desc": "Manage avionics software updates, testing, certification, and real-time monitoring.",
        "skills": ["DO-178C compliance", "Avionics software testing", "Firmware OTA management", "Safety-critical CI/CD", "ARINC 429 parsing", "Fault isolation"],
        "capabilities": ["Run avionics software tests", "Enforce DO-178C traceability", "Push certified firmware updates", "Parse ARINC 429 data", "Detect avionics faults", "Generate certification artifacts"],
        "intents": ["Run avionics test suite", "Check DO-178C compliance", "Push firmware update", "Parse ARINC data stream", "Isolate avionics fault", "Generate certification report"],
        "tools": ["LDRA", "PostgreSQL", "MinIO", "Kafka", "FastAPI", "Python", "DO-178C toolchain"],
        "workflows": ["certification-pipeline", "firmware-ota-rollout", "fault-isolation-loop", "compliance-traceability-report"],
    },
    "AWSOps": {
        "name": "AWS Cloud Operations",
        "emoji": "☁️",
        "desc": "Automate AWS infrastructure provisioning, cost optimization, security, and incident response.",
        "skills": ["AWS infrastructure automation", "Cost optimization", "Security posture management", "Multi-account governance", "Disaster recovery", "FinOps"],
        "capabilities": ["Provision resources via CloudFormation/CDK", "Identify cost anomalies", "Enforce AWS security policies", "Manage multi-account organizations", "Execute DR runbooks", "Generate cost reports"],
        "intents": ["Provision new environment", "Find cost anomalies", "Check security posture", "Manage AWS accounts", "Run DR drill", "Generate cost report"],
        "tools": ["AWS SDK (boto3)", "AWS CDK", "CloudFormation", "AWS Cost Explorer API", "Security Hub API", "Terraform", "PostgreSQL"],
        "workflows": ["infrastructure-provisioning", "cost-anomaly-detection", "security-posture-scan", "disaster-recovery-drill"],
    },
    "AzureOps": {
        "name": "Azure Cloud Operations",
        "emoji": "🔷",
        "desc": "Automate Azure resource management, governance, cost control, and security operations.",
        "skills": ["Azure Resource Manager automation", "Azure Policy enforcement", "Cost management", "Azure AD governance", "AKS operations", "Hybrid cloud management"],
        "capabilities": ["Deploy ARM/Bicep templates", "Enforce Azure Policy", "Identify budget overruns", "Manage Azure AD groups", "Operate AKS clusters", "Audit hybrid infrastructure"],
        "intents": ["Deploy Azure resource", "Enforce governance policy", "Check budget status", "Manage AD group", "Scale AKS cluster", "Audit Azure environment"],
        "tools": ["Azure SDK (azure-mgmt)", "Bicep", "Terraform", "Azure CLI", "Azure Monitor API", "PostgreSQL", "Grafana"],
        "workflows": ["arm-deployment-pipeline", "policy-compliance-scan", "cost-governance-report", "aks-operations-loop"],
    },
    "BankOps": {
        "name": "Banking Operations",
        "emoji": "🏦",
        "desc": "Automate banking workflows including payments, compliance, fraud detection, and reconciliation.",
        "skills": ["Payment processing", "Fraud detection", "AML/KYC compliance", "Reconciliation automation", "Risk management", "Regulatory reporting"],
        "capabilities": ["Process SWIFT/ACH payments", "Detect fraudulent transactions", "Run AML screening", "Reconcile ledger entries", "Generate regulatory reports", "Monitor credit risk"],
        "intents": ["Process payment", "Flag suspicious transaction", "Run KYC check", "Reconcile accounts", "Generate Basel report", "Monitor credit exposure"],
        "tools": ["PostgreSQL", "Kafka", "Redis", "SWIFT API", "TensorFlow", "FastAPI", "Vault (secrets)", "Prometheus"],
        "workflows": ["payment-processing-pipeline", "fraud-detection-model", "aml-screening-loop", "regulatory-report-generation"],
    },
    "BizOps": {
        "name": "Business Operations",
        "emoji": "💼",
        "desc": "Automate business processes, KPI tracking, cross-functional reporting, and strategic planning.",
        "skills": ["KPI dashboard automation", "OKR tracking", "Process automation", "Revenue operations", "Board reporting", "Strategic forecasting"],
        "capabilities": ["Build and update KPI dashboards", "Track OKR progress", "Automate business processes", "Analyse revenue metrics", "Generate board reports", "Forecast strategic scenarios"],
        "intents": ["Update KPI dashboard", "Check OKR status", "Automate approval workflow", "Analyse revenue trend", "Generate board report", "Forecast next quarter"],
        "tools": ["PostgreSQL", "Grafana", "Metabase", "Zapier/n8n", "Slack API", "Google Sheets API", "FastAPI"],
        "workflows": ["kpi-data-pipeline", "okr-progress-tracker", "approval-automation", "board-report-generation"],
    },
    "BlockchainOps": {
        "name": "Blockchain Operations",
        "emoji": "⛓️",
        "desc": "Operate blockchain nodes, deploy smart contracts, monitor on-chain activity, and manage wallets.",
        "skills": ["Node operations", "Smart contract deployment", "On-chain monitoring", "Wallet management", "DeFi protocol integration", "Cross-chain bridging"],
        "capabilities": ["Deploy and monitor blockchain nodes", "Deploy and verify smart contracts", "Monitor on-chain events", "Manage multi-sig wallets", "Interact with DeFi protocols", "Bridge assets cross-chain"],
        "intents": ["Deploy smart contract", "Monitor on-chain events", "Check node health", "Transfer assets", "Interact with DeFi protocol", "Bridge tokens to L2"],
        "tools": ["Web3.py", "Hardhat", "Ethers.js", "Infura/Alchemy API", "PostgreSQL", "Redis", "Prometheus", "Grafana"],
        "workflows": ["contract-deploy-verify", "on-chain-event-listener", "node-health-monitoring", "wallet-transaction-pipeline"],
    },
    "ChemiOps": {
        "name": "Chemical Operations",
        "emoji": "⚗️",
        "desc": "Manage chemical plant operations, safety monitoring, inventory, and regulatory compliance.",
        "skills": ["Process control", "Safety monitoring", "Chemical inventory management", "Environmental compliance", "Lab data management", "Incident reporting"],
        "capabilities": ["Monitor process parameters", "Alert on safety threshold breaches", "Track chemical inventory", "Generate environmental reports", "Manage MSDS documents", "Log safety incidents"],
        "intents": ["Check process parameters", "Alert on safety breach", "Check chemical stock", "Generate EPA report", "Find MSDS for chemical", "Log safety incident"],
        "tools": ["MQTT", "InfluxDB", "Grafana", "PostgreSQL", "FastAPI", "MinIO", "PagerDuty"],
        "workflows": ["process-monitoring-alert", "inventory-reorder-trigger", "safety-incident-pipeline", "environmental-compliance-report"],
    },
    "CivilOps": {
        "name": "Civil Engineering Operations",
        "emoji": "🏗️",
        "desc": "Manage civil infrastructure projects, structural monitoring, asset maintenance, and compliance.",
        "skills": ["Structural health monitoring", "Project scheduling", "Asset lifecycle management", "GIS-based planning", "Environmental impact assessment", "Regulatory compliance"],
        "capabilities": ["Monitor structural sensors", "Schedule project milestones", "Track infrastructure assets", "Generate GIS-based reports", "Assess environmental impact", "Audit regulatory compliance"],
        "intents": ["Check bridge sensor data", "Update project schedule", "Track road asset condition", "Generate GIS map", "Assess environmental impact", "Audit compliance status"],
        "tools": ["PostgreSQL + PostGIS", "MQTT", "InfluxDB", "QGIS API", "FastAPI", "Grafana", "MinIO"],
        "workflows": ["structural-monitoring-alert", "project-milestone-tracker", "asset-condition-report", "compliance-audit-pipeline"],
    },
    "CodeOps": {
        "name": "Code Operations",
        "emoji": "💻",
        "desc": "Automate code quality, static analysis, dependency management, and developer productivity.",
        "skills": ["Static code analysis", "Dependency vulnerability scanning", "Code review automation", "Test coverage enforcement", "Technical debt measurement", "Developer metrics"],
        "capabilities": ["Run static analysis on PRs", "Scan dependencies for CVEs", "Auto-comment on code quality issues", "Enforce test coverage thresholds", "Measure technical debt", "Track DORA metrics"],
        "intents": ["Analyse code quality", "Scan for vulnerable dependencies", "Review PR automatically", "Check test coverage", "Measure tech debt", "Track deployment frequency"],
        "tools": ["SonarQube API", "Snyk API", "GitHub API", "GitLab API", "Codecov API", "PostgreSQL", "Grafana"],
        "workflows": ["pr-quality-gate", "dependency-scan-pipeline", "dora-metrics-dashboard", "debt-remediation-sprint"],
    },
    "CommOps": {
        "name": "Communications Operations",
        "emoji": "📡",
        "desc": "Operate communication platforms, manage messaging pipelines, monitor uptime, and support compliance.",
        "skills": ["Messaging platform operations", "SIP/VoIP management", "Email deliverability", "Push notification routing", "Compliance archiving", "Uptime monitoring"],
        "capabilities": ["Manage messaging queues", "Monitor SIP trunk health", "Track email deliverability", "Route push notifications", "Archive communications for compliance", "Alert on channel outages"],
        "intents": ["Check messaging queue status", "Monitor SIP health", "Check email bounce rate", "Route notification campaign", "Archive communications", "Alert on outage"],
        "tools": ["Kafka", "Twilio API", "SendGrid API", "Firebase FCM", "Redis", "PostgreSQL", "Grafana", "Prometheus"],
        "workflows": ["message-queue-monitoring", "email-deliverability-tracking", "notification-routing-pipeline", "compliance-archive"],
    },
    "CompOps": {
        "name": "Compliance Operations",
        "emoji": "⚖️",
        "desc": "Automate compliance monitoring, policy enforcement, audit trail management, and regulatory reporting.",
        "skills": ["Policy enforcement automation", "Audit trail management", "Regulatory mapping", "Risk assessment", "Evidence collection", "Continuous compliance monitoring"],
        "capabilities": ["Monitor policy compliance continuously", "Collect and store audit evidence", "Map controls to regulations", "Assess risk posture", "Generate audit reports", "Alert on compliance drift"],
        "intents": ["Check compliance posture", "Collect audit evidence", "Map control to regulation", "Assess risk", "Generate audit report", "Alert on policy violation"],
        "tools": ["OpenPolicyAgent (OPA)", "PostgreSQL", "Vault", "Grafana", "FastAPI", "MinIO", "Kafka"],
        "workflows": ["continuous-compliance-scan", "audit-evidence-collection", "risk-assessment-pipeline", "regulatory-report-generation"],
    },
    "ConstOps": {
        "name": "Construction Operations",
        "emoji": "🔨",
        "desc": "Manage construction site operations, project scheduling, safety monitoring, and material logistics.",
        "skills": ["Project scheduling (Gantt/CPM)", "Site safety monitoring", "Material tracking", "Subcontractor management", "Cost control", "Quality inspection"],
        "capabilities": ["Track project milestones", "Monitor site safety sensors", "Manage material orders and deliveries", "Coordinate subcontractors", "Track budget vs actuals", "Log quality inspections"],
        "intents": ["Update project schedule", "Check site safety status", "Order materials", "Coordinate subcontractor", "Check budget status", "Log quality inspection"],
        "tools": ["PostgreSQL", "MQTT", "InfluxDB", "Procore API", "FastAPI", "Grafana", "Slack API"],
        "workflows": ["milestone-tracking-pipeline", "safety-alert-system", "material-logistics-automation", "budget-monitoring-report"],
    },
    "DairyOps": {
        "name": "Dairy Operations",
        "emoji": "🐄",
        "desc": "Automate dairy farm management including milking schedules, herd health, and milk quality tracking.",
        "skills": ["Herd health monitoring", "Milking automation", "Milk quality analysis", "Feed management", "Reproduction tracking", "Cold chain monitoring"],
        "capabilities": ["Monitor herd health sensors", "Schedule and log milking", "Track milk quality metrics", "Optimize feed rations", "Track reproduction cycles", "Alert on cold chain breaks"],
        "intents": ["Check herd health", "Schedule milking", "Log milk quality", "Optimize feed plan", "Track reproduction", "Alert on cold chain issue"],
        "tools": ["MQTT", "InfluxDB", "PostgreSQL", "Grafana", "FastAPI", "Precision feeding sensors", "Lab API"],
        "workflows": ["herd-health-monitoring", "milking-schedule-automation", "milk-quality-pipeline", "cold-chain-alert"],
    },
    "DataMeshOps": {
        "name": "Data Mesh Operations",
        "emoji": "🕸️",
        "desc": "Operate federated data domains, enforce data contracts, manage data products, and govern the mesh.",
        "skills": ["Data domain management", "Data contract enforcement", "Data product lifecycle", "Federated governance", "Data quality monitoring", "Mesh observability"],
        "capabilities": ["Register and publish data products", "Enforce data contracts", "Monitor data quality SLAs", "Govern access to data domains", "Track data lineage", "Alert on contract violations"],
        "intents": ["Register data product", "Enforce data contract", "Check data quality", "Manage domain access", "Track data lineage", "Alert on SLA breach"],
        "tools": ["DataHub", "Great Expectations", "dbt", "PostgreSQL", "Kafka", "OpenLineage", "Grafana"],
        "workflows": ["data-product-registration", "contract-validation-pipeline", "quality-monitoring-loop", "lineage-tracking"],
    },
    "DataOps": {
        "name": "Data Operations",
        "emoji": "📊",
        "desc": "Automate data pipelines, data quality, catalog management, and analytics delivery.",
        "skills": ["Pipeline orchestration", "Data quality automation", "Data catalog management", "ETL/ELT automation", "Data lineage tracking", "Analytics delivery"],
        "capabilities": ["Build and schedule data pipelines", "Validate data quality automatically", "Maintain data catalog", "Run ETL/ELT jobs", "Track data lineage", "Deliver analytics to stakeholders"],
        "intents": ["Build data pipeline", "Validate data quality", "Update data catalog", "Run ETL job", "Track lineage", "Deliver analytics report"],
        "tools": ["Apache Airflow", "dbt", "Great Expectations", "Apache Spark", "PostgreSQL", "DataHub", "Grafana", "MinIO"],
        "workflows": ["pipeline-orchestration", "quality-gate-validation", "catalog-sync-pipeline", "lineage-capture"],
    },
    "DDDOps": {
        "name": "Domain-Driven Design Operations",
        "emoji": "🗺️",
        "desc": "Support DDD practices including bounded context management, event storming, and domain model evolution.",
        "skills": ["Bounded context mapping", "Event storming facilitation", "Aggregate design", "Domain model versioning", "Context map visualization", "Ubiquitous language management"],
        "capabilities": ["Map bounded contexts", "Facilitate event storming sessions", "Version domain models", "Visualize context maps", "Enforce ubiquitous language", "Detect context boundary violations"],
        "intents": ["Map bounded context", "Run event storming", "Version domain model", "Visualize context map", "Enforce language consistency", "Detect boundary violation"],
        "tools": ["Miro API", "PlantUML", "EventStorming tools", "PostgreSQL", "FastAPI", "Confluence API"],
        "workflows": ["context-mapping-session", "event-storming-facilitation", "model-versioning-pipeline", "language-consistency-check"],
    },
    "DefOps": {
        "name": "Defence Operations",
        "emoji": "🛡️",
        "desc": "Manage defence systems operations, secure communications, mission planning, and logistics.",
        "skills": ["Secure communications", "Mission planning automation", "Supply chain logistics", "Cyber defence", "Intelligence data processing", "Compliance with ITAR/NIST"],
        "capabilities": ["Manage secure communication channels", "Automate mission planning workflows", "Track defence supply chains", "Monitor cyber threats", "Process intelligence data", "Enforce ITAR/NIST compliance"],
        "intents": ["Secure communication channel", "Plan mission workflow", "Track supply chain", "Monitor cyber threats", "Process intelligence", "Audit ITAR compliance"],
        "tools": ["HashiCorp Vault", "PostgreSQL", "Kafka", "FastAPI", "MQTT", "OpenPolicyAgent", "Grafana"],
        "workflows": ["secure-comms-pipeline", "mission-planning-automation", "cyber-threat-monitoring", "compliance-audit"],
    },
    "DevOps": {
        "name": "Development Operations",
        "emoji": "🔧",
        "desc": "Automate CI/CD pipelines, infrastructure as code, release management, and developer experience.",
        "skills": ["CI/CD pipeline automation", "Infrastructure as Code", "Release management", "Container orchestration", "Monitoring and observability", "Developer experience"],
        "capabilities": ["Build and deploy CI/CD pipelines", "Provision infrastructure with IaC", "Manage release gates", "Orchestrate containers with Kubernetes", "Monitor with LGTM stack", "Improve developer experience"],
        "intents": ["Set up CI/CD pipeline", "Provision infrastructure", "Create release gate", "Deploy to Kubernetes", "Set up monitoring", "Improve build times"],
        "tools": ["GitHub Actions", "GitLab CI", "Terraform", "Kubernetes", "Helm", "Prometheus", "Grafana", "Loki", "Docker"],
        "workflows": ["ci-cd-pipeline", "iac-provisioning", "release-gate-approval", "k8s-deployment-rollout"],
    },
    "DevSecOps": {
        "name": "Development Security Operations",
        "emoji": "🔒",
        "desc": "Embed security into CI/CD pipelines, automate vulnerability management, and enforce security policies.",
        "skills": ["SAST/DAST automation", "Container image scanning", "Secrets detection", "SBOM generation", "Security policy enforcement", "Vulnerability management"],
        "capabilities": ["Run SAST in CI pipelines", "Scan container images for CVEs", "Detect committed secrets", "Generate SBOMs", "Enforce security policies as code", "Manage vulnerability backlog"],
        "intents": ["Scan code for vulnerabilities", "Check container image CVEs", "Detect secrets in repo", "Generate SBOM", "Enforce security policy", "Manage vulnerability backlog"],
        "tools": ["Semgrep", "Trivy", "Gitleaks", "Syft", "OpenPolicyAgent", "Snyk", "GitHub API", "PostgreSQL"],
        "workflows": ["sast-pipeline", "container-scan-gate", "secrets-detection-alert", "vulnerability-triage"],
    },
    "DrugOps": {
        "name": "Pharmaceutical Drug Operations",
        "emoji": "💊",
        "desc": "Manage drug manufacturing, clinical trial data, regulatory submissions, and pharmacovigilance.",
        "skills": ["GMP compliance", "Clinical data management", "Regulatory submission", "Pharmacovigilance", "Cold chain management", "Batch record automation"],
        "capabilities": ["Track GMP compliance", "Manage clinical trial data", "Prepare regulatory submissions", "Monitor adverse drug reactions", "Track cold chain integrity", "Generate batch records"],
        "intents": ["Check GMP compliance", "Manage clinical data", "Prepare FDA submission", "Monitor adverse events", "Track cold chain", "Generate batch record"],
        "tools": ["PostgreSQL", "MinIO", "FastAPI", "HL7 FHIR API", "Vault", "Kafka", "Grafana"],
        "workflows": ["gmp-compliance-pipeline", "clinical-data-management", "regulatory-submission", "pharmacovigilance-monitoring"],
    },
    "EduOps": {
        "name": "Education Operations",
        "emoji": "🎓",
        "desc": "Automate learning management, student analytics, curriculum planning, and institutional reporting.",
        "skills": ["LMS administration", "Student performance analytics", "Curriculum planning", "Adaptive learning", "Accreditation compliance", "Institutional reporting"],
        "capabilities": ["Manage LMS content and users", "Analyse student performance", "Plan curriculum workflows", "Deliver adaptive learning paths", "Track accreditation compliance", "Generate institutional reports"],
        "intents": ["Update LMS course", "Analyse student performance", "Plan curriculum", "Set up adaptive learning", "Check accreditation status", "Generate institutional report"],
        "tools": ["Moodle API", "PostgreSQL", "Grafana", "Kafka", "FastAPI", "Canvas API", "MinIO"],
        "workflows": ["student-analytics-pipeline", "adaptive-learning-engine", "curriculum-planning-workflow", "accreditation-audit"],
    },
    "ElderOps": {
        "name": "Elder Care Operations",
        "emoji": "👴",
        "desc": "Support elder care facilities with health monitoring, medication management, and family communication.",
        "skills": ["Health monitoring automation", "Medication scheduling", "Fall detection", "Family communication", "Care plan management", "Regulatory compliance"],
        "capabilities": ["Monitor resident health sensors", "Schedule and track medications", "Detect falls via sensor/vision", "Notify family members automatically", "Manage care plans", "Audit care compliance"],
        "intents": ["Monitor resident health", "Schedule medication", "Detect fall event", "Notify family", "Update care plan", "Audit compliance"],
        "tools": ["MQTT", "InfluxDB", "PostgreSQL", "Twilio API", "FastAPI", "Grafana", "OpenCV"],
        "workflows": ["health-monitoring-alert", "medication-scheduling", "fall-detection-pipeline", "family-notification-flow"],
    },
    "ElectOps": {
        "name": "Electronics Operations",
        "emoji": "⚡",
        "desc": "Manage electronics manufacturing, PCB design workflows, test automation, and supply chain.",
        "skills": ["PCB design management", "Electronics test automation", "Component lifecycle tracking", "ESD compliance", "Supply chain management", "Failure analysis"],
        "capabilities": ["Version PCB design files", "Automate electronics testing", "Track component lifecycle", "Enforce ESD procedures", "Manage component supply chain", "Analyse failure modes"],
        "intents": ["Version PCB design", "Run electronics test", "Track component status", "Check ESD compliance", "Manage component supply", "Analyse failure mode"],
        "tools": ["MinIO", "PostgreSQL", "Kafka", "FastAPI", "Grafana", "JIRA API", "Git LFS"],
        "workflows": ["pcb-design-versioning", "test-automation-pipeline", "component-tracking", "failure-analysis-report"],
    },
    "EnerOps": {
        "name": "Energy Operations",
        "emoji": "⚡",
        "desc": "Operate energy grids, renewable sources, demand forecasting, and energy trading systems.",
        "skills": ["Grid operations", "Renewable energy management", "Demand forecasting", "Energy trading", "Smart meter management", "Carbon accounting"],
        "capabilities": ["Monitor grid health in real time", "Manage renewable energy dispatch", "Forecast energy demand", "Execute energy trades", "Process smart meter data", "Track carbon emissions"],
        "intents": ["Check grid status", "Dispatch renewable energy", "Forecast demand", "Execute energy trade", "Process meter reading", "Track carbon emissions"],
        "tools": ["MQTT", "InfluxDB", "Grafana", "Kafka", "PostgreSQL", "FastAPI", "ENTSO-E API", "Prophet"],
        "workflows": ["grid-monitoring-pipeline", "renewable-dispatch-loop", "demand-forecast-model", "carbon-accounting-report"],
    },
    "EnterOps": {
        "name": "Entertainment Operations",
        "emoji": "🎭",
        "desc": "Manage content production, distribution, rights management, and audience analytics.",
        "skills": ["Content pipeline management", "Rights and licensing", "Audience analytics", "Distribution platform integration", "Live event operations", "Content moderation"],
        "capabilities": ["Manage content production pipelines", "Track rights and licenses", "Analyse audience engagement", "Integrate with streaming platforms", "Operate live events", "Moderate user content"],
        "intents": ["Track content production", "Check rights status", "Analyse audience data", "Distribute to streaming platform", "Operate live event", "Moderate content"],
        "tools": ["PostgreSQL", "Kafka", "Redis", "MinIO", "FFmpeg", "Grafana", "FastAPI", "YouTube API"],
        "workflows": ["content-production-pipeline", "rights-management-workflow", "audience-analytics-report", "live-event-operations"],
    },
    "EventOps": {
        "name": "Event Operations",
        "emoji": "📅",
        "desc": "Automate event planning, registration, ticketing, logistics, and post-event analytics.",
        "skills": ["Event planning automation", "Registration management", "Ticketing system integration", "Venue logistics", "Speaker management", "Post-event analytics"],
        "capabilities": ["Automate event registration", "Manage ticketing workflows", "Coordinate venue logistics", "Manage speakers and agendas", "Send automated communications", "Analyse post-event feedback"],
        "intents": ["Register for event", "Manage ticket allocation", "Coordinate venue", "Manage speaker schedule", "Send event communications", "Analyse event feedback"],
        "tools": ["Eventbrite API", "PostgreSQL", "Redis", "SendGrid API", "Slack API", "FastAPI", "Grafana"],
        "workflows": ["registration-automation", "ticketing-pipeline", "event-communication-flow", "post-event-analytics"],
    },
    "FarmOps": {
        "name": "Farm Operations",
        "emoji": "🚜",
        "desc": "Automate farm management including crop planning, equipment tracking, and supply chain.",
        "skills": ["Crop planning", "Equipment telematics", "Supply chain management", "Weather integration", "Labour management", "Financial reporting"],
        "capabilities": ["Plan crop rotations", "Track farm equipment", "Manage supply chain", "Integrate weather forecasts", "Schedule labour", "Generate farm financial reports"],
        "intents": ["Plan crop rotation", "Track equipment", "Manage supply chain", "Get weather forecast", "Schedule workers", "Generate financial report"],
        "tools": ["PostgreSQL", "MQTT", "InfluxDB", "OpenWeatherMap API", "FastAPI", "Grafana", "Twilio API"],
        "workflows": ["crop-planning-optimization", "equipment-tracking-pipeline", "supply-chain-management", "financial-reporting"],
    },
    "FinOps": {
        "name": "Cloud Financial Operations",
        "emoji": "💰",
        "desc": "Optimize cloud costs, enforce budget policies, allocate spend, and drive FinOps culture.",
        "skills": ["Cloud cost optimization", "Budget policy enforcement", "Chargeback and showback", "Reserved instance management", "Waste identification", "FinOps reporting"],
        "capabilities": ["Analyse cloud costs by team/service", "Enforce budget thresholds", "Generate chargeback reports", "Manage reserved instances", "Identify idle resources", "Forecast cloud spend"],
        "intents": ["Analyse cloud costs", "Set budget threshold", "Generate chargeback report", "Manage reserved instances", "Find idle resources", "Forecast cloud spend"],
        "tools": ["AWS Cost Explorer API", "Azure Cost Management API", "GCP Billing API", "PostgreSQL", "Grafana", "Metabase", "Slack API"],
        "workflows": ["cost-analysis-pipeline", "budget-enforcement-alerts", "chargeback-report-generation", "waste-identification-scan"],
    },
    "FishOps": {
        "name": "Fishery Operations",
        "emoji": "🐟",
        "desc": "Manage fishing fleet operations, stock assessment, aquaculture monitoring, and sustainability compliance.",
        "skills": ["Fleet management", "Fish stock assessment", "Aquaculture monitoring", "Catch quota management", "Cold chain tracking", "Sustainability compliance"],
        "capabilities": ["Track fishing fleet vessels", "Assess fish stock levels", "Monitor aquaculture sensors", "Manage catch quotas", "Track cold chain", "Report sustainability compliance"],
        "intents": ["Track vessel location", "Assess fish stock", "Monitor fish farm", "Check quota status", "Track cold chain", "Report sustainability"],
        "tools": ["PostgreSQL + PostGIS", "MQTT", "InfluxDB", "Grafana", "FastAPI", "AIS API", "MinIO"],
        "workflows": ["fleet-tracking-pipeline", "stock-assessment-model", "aquaculture-monitoring", "quota-compliance-report"],
    },
    "FoodOps": {
        "name": "Food Operations",
        "emoji": "🍽️",
        "desc": "Manage food production, quality control, supply chain traceability, and regulatory compliance.",
        "skills": ["Food safety (HACCP)", "Production scheduling", "Quality control automation", "Traceability management", "Supply chain visibility", "Regulatory compliance"],
        "capabilities": ["Monitor HACCP critical control points", "Schedule production runs", "Automate QC sampling", "Track food supply chain", "Manage allergen declarations", "Generate FDA/EFSA reports"],
        "intents": ["Check HACCP status", "Schedule production", "Run QC check", "Track product origin", "Check allergen info", "Generate compliance report"],
        "tools": ["PostgreSQL", "MQTT", "InfluxDB", "Kafka", "FastAPI", "Grafana", "MinIO", "Blockchain traceability"],
        "workflows": ["haccp-monitoring-pipeline", "production-scheduling", "qc-automation", "traceability-tracking"],
    },
    "ForesOps": {
        "name": "Forestry Operations",
        "emoji": "🌲",
        "desc": "Manage forest resources, logging operations, reforestation tracking, and environmental compliance.",
        "skills": ["Forest inventory management", "Sustainable logging planning", "Reforestation tracking", "Fire risk monitoring", "Carbon credit management", "Environmental compliance"],
        "capabilities": ["Manage forest inventory", "Plan sustainable logging operations", "Track reforestation progress", "Monitor fire risk sensors", "Manage carbon credits", "Report environmental compliance"],
        "intents": ["Check forest inventory", "Plan logging operation", "Track reforestation", "Monitor fire risk", "Manage carbon credits", "Report compliance"],
        "tools": ["PostgreSQL + PostGIS", "MQTT", "Grafana", "NASA FIRMS API", "FastAPI", "MinIO", "QGIS API"],
        "workflows": ["inventory-management-pipeline", "fire-risk-monitoring", "reforestation-tracker", "carbon-credit-reporting"],
    },
    "FurnOps": {
        "name": "Furniture Operations",
        "emoji": "🪑",
        "desc": "Manage furniture manufacturing, custom orders, inventory, and delivery logistics.",
        "skills": ["Manufacturing scheduling", "Custom order management", "Inventory optimization", "Quality inspection", "Delivery logistics", "Supplier management"],
        "capabilities": ["Schedule manufacturing runs", "Manage custom furniture orders", "Optimize inventory levels", "Run quality inspections", "Track delivery logistics", "Manage supplier relationships"],
        "intents": ["Schedule manufacturing", "Manage custom order", "Check inventory", "Run quality inspection", "Track delivery", "Manage supplier"],
        "tools": ["PostgreSQL", "Kafka", "Redis", "FastAPI", "Grafana", "Shopify API", "ERP integration"],
        "workflows": ["order-to-production-pipeline", "inventory-optimization", "quality-inspection-gate", "delivery-tracking"],
    },
    "GenAIOps": {
        "name": "Generative AI Operations",
        "emoji": "✨",
        "desc": "Operate, evaluate, and govern generative AI models including LLMs, image models, and multimodal systems.",
        "skills": ["LLM deployment and serving", "Prompt management", "Evaluation and benchmarking", "Safety and guardrails", "Fine-tuning pipelines", "Cost optimization"],
        "capabilities": ["Serve LLMs via API", "Manage prompt versions", "Evaluate model quality and safety", "Apply content guardrails", "Run fine-tuning pipelines", "Optimize token costs"],
        "intents": ["Deploy LLM", "Manage prompt versions", "Evaluate model quality", "Apply safety guardrails", "Fine-tune model", "Optimize LLM costs"],
        "tools": ["Ollama", "vLLM", "LiteLLM", "LangSmith", "TGI (HuggingFace)", "OpenAI API", "Prometheus", "Grafana"],
        "workflows": ["llm-serving-pipeline", "prompt-version-management", "safety-evaluation-loop", "fine-tuning-pipeline"],
    },
    "GitOps": {
        "name": "Git Operations",
        "emoji": "🔀",
        "desc": "Manage infrastructure and application deployments driven by Git as the single source of truth.",
        "skills": ["Git workflow automation", "Declarative deployment", "Drift detection", "Reconciliation loops", "Secret management", "Multi-cluster management"],
        "capabilities": ["Sync cluster state with Git", "Detect configuration drift", "Reconcile desired vs actual state", "Manage secrets via sealed secrets", "Operate multi-cluster GitOps", "Enforce PR-based deployments"],
        "intents": ["Sync cluster with Git", "Detect config drift", "Reconcile state", "Manage secrets", "Manage multi-cluster", "Enforce PR workflow"],
        "tools": ["ArgoCD", "Flux", "Helm", "Kustomize", "Kubernetes", "GitHub API", "Sealed Secrets", "External Secrets"],
        "workflows": ["git-sync-reconciliation", "drift-detection-alert", "pr-based-deployment", "multi-cluster-sync"],
    },
    "GovOps": {
        "name": "Government Operations",
        "emoji": "🏛️",
        "desc": "Automate government service delivery, citizen engagement, compliance, and inter-agency coordination.",
        "skills": ["Digital service delivery", "Citizen data management", "Policy compliance", "Inter-agency coordination", "Open data publishing", "Audit trail management"],
        "capabilities": ["Deliver digital government services", "Manage citizen data securely", "Enforce policy compliance", "Coordinate inter-agency workflows", "Publish open data sets", "Maintain audit trails"],
        "intents": ["Deliver digital service", "Manage citizen data", "Check policy compliance", "Coordinate agencies", "Publish open data", "Audit government process"],
        "tools": ["PostgreSQL", "Vault", "Kafka", "FastAPI", "OpenPolicyAgent", "MinIO", "Grafana", "LDAP"],
        "workflows": ["citizen-service-pipeline", "policy-compliance-monitoring", "inter-agency-coordination", "open-data-publishing"],
    },
    "HealthOps": {
        "name": "Healthcare Operations",
        "emoji": "🏥",
        "desc": "Automate healthcare workflows including patient management, clinical documentation, and compliance.",
        "skills": ["Patient data management", "Clinical workflow automation", "HL7 FHIR integration", "HIPAA compliance", "Medical device monitoring", "Healthcare analytics"],
        "capabilities": ["Manage patient records via FHIR", "Automate clinical documentation", "Ensure HIPAA compliance", "Monitor medical devices", "Analyse patient outcomes", "Coordinate care teams"],
        "intents": ["Access patient record", "Document clinical note", "Check HIPAA compliance", "Monitor device", "Analyse patient outcomes", "Coordinate care team"],
        "tools": ["HL7 FHIR API", "PostgreSQL", "Vault", "Kafka", "Grafana", "FastAPI", "MinIO"],
        "workflows": ["patient-record-management", "clinical-documentation-pipeline", "hipaa-compliance-monitoring", "care-coordination"],
    },
    "HomeOps": {
        "name": "Home Operations",
        "emoji": "🏠",
        "desc": "Automate smart home management, energy optimization, security monitoring, and maintenance scheduling.",
        "skills": ["Smart home automation", "Energy optimization", "Security monitoring", "Maintenance scheduling", "IoT device management", "Voice assistant integration"],
        "capabilities": ["Automate home routines", "Optimize home energy usage", "Monitor home security cameras", "Schedule maintenance tasks", "Manage IoT devices", "Integrate with voice assistants"],
        "intents": ["Automate home routine", "Optimize energy usage", "Check security feed", "Schedule maintenance", "Manage smart device", "Integrate voice assistant"],
        "tools": ["Home Assistant API", "MQTT", "InfluxDB", "Grafana", "FastAPI", "Zigbee2MQTT", "Alexa API"],
        "workflows": ["home-automation-routines", "energy-optimization-loop", "security-monitoring-alert", "maintenance-scheduler"],
    },
    "HumanOps": {
        "name": "Human Resources Operations",
        "emoji": "👥",
        "desc": "Automate HR workflows including recruitment, onboarding, performance management, and compliance.",
        "skills": ["Recruitment automation", "Onboarding workflow", "Performance management", "Payroll integration", "Compliance management", "Employee analytics"],
        "capabilities": ["Automate recruitment pipeline", "Run onboarding workflows", "Manage performance reviews", "Integrate with payroll systems", "Ensure HR compliance", "Analyse employee metrics"],
        "intents": ["Post job and screen candidates", "Onboard new employee", "Run performance review", "Process payroll", "Check HR compliance", "Analyse workforce metrics"],
        "tools": ["Workday API", "BambooHR API", "PostgreSQL", "Kafka", "SendGrid API", "Slack API", "FastAPI"],
        "workflows": ["recruitment-pipeline", "onboarding-automation", "performance-review-cycle", "hr-compliance-audit"],
    },
    "HygenOps": {
        "name": "Hygiene Operations",
        "emoji": "🧼",
        "desc": "Manage hygiene compliance, sanitation scheduling, audit tracking, and supply management for facilities.",
        "skills": ["Sanitation scheduling", "Hygiene audit management", "Compliance tracking", "Supply inventory management", "Incident reporting", "Training management"],
        "capabilities": ["Schedule sanitation tasks", "Run hygiene audits", "Track compliance scores", "Manage hygiene supplies", "Log hygiene incidents", "Track staff training completion"],
        "intents": ["Schedule sanitation task", "Run hygiene audit", "Check compliance score", "Order hygiene supplies", "Log incident", "Track training"],
        "tools": ["PostgreSQL", "FastAPI", "Grafana", "Slack API", "SendGrid API", "MinIO"],
        "workflows": ["sanitation-scheduling", "audit-pipeline", "compliance-monitoring", "supply-reorder-trigger"],
    },
    "InterOps": {
        "name": "Interoperability Operations",
        "emoji": "🔗",
        "desc": "Manage system integration, API orchestration, data translation, and cross-system workflows.",
        "skills": ["API integration management", "Data format translation", "Protocol bridging", "Integration testing", "Event-driven integration", "API governance"],
        "capabilities": ["Orchestrate cross-system workflows", "Translate between data formats", "Bridge different protocols", "Test integrations automatically", "Manage event-driven flows", "Govern API usage"],
        "intents": ["Integrate two systems", "Translate data format", "Bridge protocols", "Test integration", "Set up event flow", "Govern API"],
        "tools": ["Apache Camel", "n8n", "MuleSoft API", "Kafka", "Redis", "PostgreSQL", "FastAPI", "OpenAPI Spec"],
        "workflows": ["api-orchestration-pipeline", "format-translation-flow", "integration-test-suite", "event-driven-integration"],
    },
    "IoTOps": {
        "name": "IoT Operations",
        "emoji": "📡",
        "desc": "Manage IoT device fleets, firmware updates, telemetry pipelines, and edge-to-cloud integration.",
        "skills": ["Device fleet management", "Firmware OTA updates", "Telemetry ingestion", "Edge computing", "Device security", "Digital twin management"],
        "capabilities": ["Manage IoT device fleets", "Push OTA firmware updates", "Ingest and process telemetry", "Run workloads at the edge", "Secure IoT devices", "Create and sync digital twins"],
        "intents": ["Manage device fleet", "Push firmware update", "Ingest telemetry", "Deploy edge workload", "Secure device", "Create digital twin"],
        "tools": ["MQTT", "AWS IoT Core", "Azure IoT Hub", "InfluxDB", "Kafka", "FastAPI", "Grafana", "KubeEdge"],
        "workflows": ["telemetry-ingestion-pipeline", "ota-update-rollout", "edge-deployment-workflow", "digital-twin-sync"],
    },
    "ITOps": {
        "name": "IT Operations",
        "emoji": "🖥️",
        "desc": "Automate IT service management, infrastructure monitoring, patch management, and incident resolution.",
        "skills": ["ITSM automation", "Infrastructure monitoring", "Patch management", "Incident management", "Change management", "Asset management"],
        "capabilities": ["Automate ITSM workflows", "Monitor infrastructure health", "Manage patching cycles", "Resolve incidents automatically", "Manage changes via ITIL", "Track IT assets"],
        "intents": ["Log IT incident", "Monitor infrastructure", "Run patch cycle", "Resolve incident", "Approve change", "Track IT asset"],
        "tools": ["ServiceNow API", "Prometheus", "Grafana", "Ansible", "PostgreSQL", "Kafka", "Slack API", "PagerDuty"],
        "workflows": ["incident-management-pipeline", "patch-management-cycle", "change-approval-workflow", "asset-tracking"],
    },
    "KidsOps": {
        "name": "Kids & Family Operations",
        "emoji": "🧒",
        "desc": "Manage child-safe digital experiences, parental controls, educational content, and activity scheduling.",
        "skills": ["Content safety filtering", "Parental control management", "Activity scheduling", "Educational content curation", "Progress tracking", "Screen time management"],
        "capabilities": ["Filter unsafe content", "Manage parental controls", "Schedule children activities", "Curate educational content", "Track child learning progress", "Enforce screen time limits"],
        "intents": ["Filter unsafe content", "Set parental control", "Schedule activity", "Curate educational content", "Track progress", "Set screen time limit"],
        "tools": ["PostgreSQL", "Redis", "FastAPI", "Content moderation API", "Slack API", "Firebase", "MinIO"],
        "workflows": ["content-safety-pipeline", "parental-control-management", "activity-scheduling", "progress-tracking"],
    },
    "LambdaOps": {
        "name": "Serverless Lambda Operations",
        "emoji": "λ",
        "desc": "Operate serverless function deployments, cold start optimization, cost management, and observability.",
        "skills": ["Serverless deployment automation", "Cold start optimization", "Function observability", "Cost optimization", "Event source management", "Serverless security"],
        "capabilities": ["Deploy and version serverless functions", "Optimize cold start performance", "Monitor function invocations", "Optimize serverless costs", "Manage event sources", "Enforce function security"],
        "intents": ["Deploy serverless function", "Reduce cold starts", "Monitor function metrics", "Optimize costs", "Manage event source", "Secure function"],
        "tools": ["AWS Lambda API", "AWS SAM", "Serverless Framework", "AWS CloudWatch", "PostgreSQL", "Grafana", "Lumigo"],
        "workflows": ["function-deployment-pipeline", "cold-start-optimization", "cost-analysis-report", "security-scan-gate"],
    },
    "LandOps": {
        "name": "Land Management Operations",
        "emoji": "🗺️",
        "desc": "Manage land records, GIS mapping, zoning compliance, environmental monitoring, and permitting.",
        "skills": ["Land records management", "GIS mapping", "Zoning compliance", "Environmental monitoring", "Permitting workflow", "Title management"],
        "capabilities": ["Manage land parcel records", "Create and update GIS maps", "Check zoning compliance", "Monitor environmental conditions", "Process permit applications", "Manage property titles"],
        "intents": ["Look up land record", "Map land parcel", "Check zoning", "Monitor environment", "Process permit", "Manage title"],
        "tools": ["PostgreSQL + PostGIS", "QGIS API", "FastAPI", "MinIO", "Grafana", "Leaflet.js", "OpenLayers"],
        "workflows": ["land-record-management", "gis-mapping-pipeline", "permit-processing-workflow", "environmental-monitoring"],
    },
    "LawOps": {
        "name": "Legal Operations",
        "emoji": "⚖️",
        "desc": "Automate legal workflows including contract management, matter tracking, billing, and compliance.",
        "skills": ["Contract lifecycle management", "Legal matter management", "E-billing automation", "Compliance monitoring", "Legal research automation", "Document review"],
        "capabilities": ["Manage contract lifecycles", "Track legal matters", "Automate legal billing", "Monitor legal compliance", "Automate legal research", "Review documents with AI"],
        "intents": ["Draft contract", "Track legal matter", "Process invoice", "Check compliance", "Research legal topic", "Review document"],
        "tools": ["PostgreSQL", "MinIO", "FastAPI", "OpenAI API", "Docusign API", "Clio API", "Grafana"],
        "workflows": ["contract-lifecycle-pipeline", "matter-management-workflow", "billing-automation", "document-review-pipeline"],
    },
    "LLMOps": {
        "name": "Large Language Model Operations",
        "emoji": "🧬",
        "desc": "Operate LLM infrastructure including model serving, fine-tuning, evaluation, and cost governance.",
        "skills": ["Model serving infrastructure", "Fine-tuning pipelines", "LLM evaluation", "Prompt optimization", "Cost and latency governance", "Safety and alignment"],
        "capabilities": ["Serve and scale LLMs", "Run fine-tuning jobs", "Evaluate model quality with benchmarks", "Optimize prompts for cost/quality", "Govern LLM costs", "Apply safety filters"],
        "intents": ["Deploy LLM endpoint", "Run fine-tuning job", "Evaluate model", "Optimize prompt", "Monitor LLM costs", "Apply safety filter"],
        "tools": ["vLLM", "TGI (HuggingFace)", "Ollama", "LangSmith", "OpenAI API", "W&B", "Prometheus", "Grafana"],
        "workflows": ["model-serving-pipeline", "fine-tuning-workflow", "evaluation-benchmark", "cost-governance-report"],
    },
    "LogiOps": {
        "name": "Logistics Operations",
        "emoji": "🚚",
        "desc": "Automate logistics workflows including routing, warehouse management, tracking, and last-mile delivery.",
        "skills": ["Route optimization", "Warehouse management", "Shipment tracking", "Last-mile delivery", "Customs compliance", "Cold chain logistics"],
        "capabilities": ["Optimize delivery routes", "Manage warehouse operations", "Track shipments in real time", "Coordinate last-mile delivery", "Process customs documents", "Monitor cold chain"],
        "intents": ["Optimize delivery route", "Manage warehouse", "Track shipment", "Coordinate last-mile", "Process customs", "Monitor cold chain"],
        "tools": ["PostgreSQL + PostGIS", "Kafka", "Redis", "HERE API", "FastAPI", "Grafana", "Twilio API"],
        "workflows": ["route-optimization-engine", "warehouse-management-pipeline", "shipment-tracking", "last-mile-coordination"],
    },
    "LoveOps": {
        "name": "Relationship & Wellbeing Operations",
        "emoji": "❤️",
        "desc": "Support relationship wellbeing apps with matching, communication coaching, and mental health resources.",
        "skills": ["Matching algorithm", "Communication coaching", "Mental health resource routing", "User safety", "Privacy compliance", "Engagement analytics"],
        "capabilities": ["Run matching algorithms", "Provide communication coaching content", "Route mental health resources", "Enforce user safety policies", "Ensure GDPR compliance", "Analyse user engagement safely"],
        "intents": ["Find compatible match", "Get communication coaching", "Access mental health resource", "Report safety issue", "Check privacy settings", "Analyse engagement"],
        "tools": ["PostgreSQL", "Redis", "FastAPI", "OpenAI API", "Kafka", "SendGrid API", "MinIO"],
        "workflows": ["matching-pipeline", "coaching-content-routing", "safety-moderation-loop", "engagement-analytics"],
    },
    "MachiOps": {
        "name": "Machinery Operations",
        "emoji": "⚙️",
        "desc": "Monitor industrial machinery, automate predictive maintenance, and manage equipment lifecycle.",
        "skills": ["Condition monitoring", "Predictive maintenance", "Equipment lifecycle management", "Vibration analysis", "SCADA integration", "OEE optimization"],
        "capabilities": ["Monitor machinery sensors", "Predict equipment failures", "Manage equipment lifecycle", "Analyse vibration signatures", "Integrate with SCADA systems", "Calculate OEE metrics"],
        "intents": ["Monitor machine health", "Predict failure", "Manage equipment lifecycle", "Analyse vibration", "Integrate SCADA", "Calculate OEE"],
        "tools": ["MQTT", "InfluxDB", "Grafana", "Kafka", "PostgreSQL", "FastAPI", "TensorFlow", "OPC-UA"],
        "workflows": ["condition-monitoring-pipeline", "predictive-maintenance-model", "oee-calculation-report", "scada-integration"],
    },
    "ManuOps": {
        "name": "Manufacturing Operations",
        "emoji": "🏭",
        "desc": "Automate manufacturing execution, quality control, production planning, and supply chain integration.",
        "skills": ["MES integration", "Production planning", "Quality control automation", "Supply chain coordination", "OEE tracking", "Lean/Six Sigma automation"],
        "capabilities": ["Integrate with MES systems", "Plan production schedules", "Automate QC inspections", "Coordinate supply chain", "Track OEE metrics", "Apply lean principles"],
        "intents": ["Plan production schedule", "Automate QC", "Integrate MES", "Coordinate supply chain", "Track OEE", "Apply lean improvement"],
        "tools": ["PostgreSQL", "Kafka", "MQTT", "InfluxDB", "Grafana", "SAP API", "FastAPI", "TensorFlow"],
        "workflows": ["production-planning-pipeline", "qc-automation-gate", "mes-integration-workflow", "oee-monitoring-report"],
    },
    "MariOps": {
        "name": "Maritime Operations",
        "emoji": "⚓",
        "desc": "Manage vessel tracking, port operations, cargo management, and maritime compliance.",
        "skills": ["Vessel tracking (AIS)", "Port operations management", "Cargo management", "Maritime compliance", "Crew management", "Weather routing"],
        "capabilities": ["Track vessels via AIS", "Manage port operations", "Track cargo manifests", "Ensure maritime compliance", "Manage crew documents", "Optimize weather routing"],
        "intents": ["Track vessel", "Manage port operations", "Check cargo manifest", "Ensure compliance", "Manage crew docs", "Optimize route"],
        "tools": ["PostgreSQL + PostGIS", "AIS API", "Kafka", "FastAPI", "Grafana", "MinIO", "OpenWeatherMap API"],
        "workflows": ["vessel-tracking-pipeline", "port-operations-management", "cargo-tracking", "compliance-audit"],
    },
    "MediOps": {
        "name": "Media Operations",
        "emoji": "📰",
        "desc": "Manage media production, publishing pipelines, digital asset management, and audience analytics.",
        "skills": ["Content production pipeline", "Digital asset management", "Publishing automation", "SEO optimization", "Audience analytics", "Rights management"],
        "capabilities": ["Manage content production workflows", "Store and retrieve digital assets", "Automate publishing pipelines", "Optimize content for SEO", "Analyse audience metrics", "Manage content rights"],
        "intents": ["Manage content production", "Store digital asset", "Publish content", "Optimize for SEO", "Analyse audience", "Manage rights"],
        "tools": ["WordPress API", "MinIO", "PostgreSQL", "Kafka", "FastAPI", "Grafana", "Cloudinary API"],
        "workflows": ["content-production-pipeline", "asset-management-workflow", "publishing-automation", "audience-analytics"],
    },
    "MicroservicesOps": {
        "name": "Microservices Operations",
        "emoji": "🔬",
        "desc": "Operate microservices architectures with service mesh, distributed tracing, and chaos engineering.",
        "skills": ["Service mesh management", "Distributed tracing", "Chaos engineering", "API gateway operations", "Service discovery", "Circuit breaker management"],
        "capabilities": ["Manage service mesh (Istio/Linkerd)", "Trace requests across services", "Run chaos experiments", "Operate API gateways", "Manage service discovery", "Configure circuit breakers"],
        "intents": ["Set up service mesh", "Trace request flow", "Run chaos experiment", "Configure API gateway", "Manage service discovery", "Set circuit breaker"],
        "tools": ["Istio", "Linkerd", "Jaeger", "Zipkin", "Kong", "Consul", "Prometheus", "Grafana", "Chaos Monkey"],
        "workflows": ["service-mesh-deployment", "distributed-tracing-pipeline", "chaos-experiment-runner", "api-gateway-config"],
    },
    "MLOps": {
        "name": "Machine Learning Operations",
        "emoji": "🤖",
        "desc": "Automate ML model training, deployment, monitoring, and lifecycle management.",
        "skills": ["Model training pipelines", "Model registry management", "Model serving", "Drift detection", "Feature store management", "Experiment tracking"],
        "capabilities": ["Build and run training pipelines", "Register and version models", "Serve models via API", "Detect model drift", "Manage feature stores", "Track experiments"],
        "intents": ["Train ML model", "Register model version", "Deploy model endpoint", "Detect model drift", "Manage features", "Track experiment"],
        "tools": ["MLflow", "Kubeflow", "DVC", "Feast", "Seldon Core", "Prometheus", "Grafana", "MinIO", "PostgreSQL"],
        "workflows": ["training-pipeline", "model-registration-workflow", "serving-deployment", "drift-detection-monitor"],
    },
    "MoneyOps": {
        "name": "Money Operations",
        "emoji": "💵",
        "desc": "Automate personal and business money management, budgeting, forecasting, and payment processing.",
        "skills": ["Budget automation", "Expense tracking", "Cash flow forecasting", "Payment processing", "Tax preparation", "Investment tracking"],
        "capabilities": ["Automate budgeting", "Track and categorize expenses", "Forecast cash flow", "Process payments", "Prepare tax documents", "Track investment portfolio"],
        "intents": ["Set budget", "Track expense", "Forecast cash flow", "Process payment", "Prepare tax docs", "Track investments"],
        "tools": ["PostgreSQL", "Plaid API", "Stripe API", "FastAPI", "Grafana", "Redis", "SendGrid API"],
        "workflows": ["budget-automation-pipeline", "expense-categorization", "cash-flow-forecast", "tax-preparation-workflow"],
    },
    "MuniOps": {
        "name": "Municipal Operations",
        "emoji": "🏙️",
        "desc": "Automate municipal services including waste management, utilities, permits, and citizen services.",
        "skills": ["Waste management routing", "Utility billing automation", "Permit processing", "Citizen service automation", "Asset management", "Emergency response coordination"],
        "capabilities": ["Optimize waste collection routes", "Automate utility billing", "Process permit applications", "Deliver citizen self-service", "Track municipal assets", "Coordinate emergency response"],
        "intents": ["Optimize waste route", "Process utility bill", "Apply for permit", "Access citizen service", "Track municipal asset", "Coordinate emergency"],
        "tools": ["PostgreSQL + PostGIS", "Kafka", "FastAPI", "HERE API", "Grafana", "Twilio API", "MinIO"],
        "workflows": ["waste-routing-optimization", "utility-billing-pipeline", "permit-processing-workflow", "citizen-service-portal"],
    },
    "MusicOps": {
        "name": "Music Operations",
        "emoji": "🎵",
        "desc": "Manage music production, distribution, rights management, and artist analytics.",
        "skills": ["Music production pipeline", "Distribution automation", "Rights and royalty management", "Artist analytics", "Metadata management", "Playlist optimization"],
        "capabilities": ["Manage music production workflows", "Distribute to streaming platforms", "Track rights and royalties", "Analyse artist performance", "Manage track metadata", "Optimize playlists"],
        "intents": ["Submit music for distribution", "Track royalties", "Analyse streaming performance", "Manage track metadata", "Optimize playlist", "Register rights"],
        "tools": ["PostgreSQL", "MinIO", "Kafka", "FastAPI", "Spotify API", "Apple Music API", "Grafana"],
        "workflows": ["music-distribution-pipeline", "royalty-tracking-workflow", "artist-analytics-report", "metadata-management"],
    },
    "NationOps": {
        "name": "National Operations",
        "emoji": "🌐",
        "desc": "Support national-scale digital transformation, cross-ministry data sharing, and e-government services.",
        "skills": ["Digital identity management", "Cross-ministry integration", "National data platform", "Cybersecurity governance", "Policy automation", "Open government data"],
        "capabilities": ["Manage national digital identities", "Integrate cross-ministry data", "Operate national data platforms", "Govern national cybersecurity", "Automate policy implementation", "Publish open government data"],
        "intents": ["Manage digital identity", "Share data across ministries", "Operate data platform", "Govern cybersecurity", "Implement policy", "Publish open data"],
        "tools": ["Keycloak", "PostgreSQL", "Kafka", "OpenPolicyAgent", "FastAPI", "MinIO", "Grafana", "Vault"],
        "workflows": ["digital-identity-pipeline", "cross-ministry-integration", "cybersecurity-governance", "open-data-publishing"],
    },
    "PetOps": {
        "name": "Pet Care Operations",
        "emoji": "🐾",
        "desc": "Manage pet care services including veterinary records, appointment scheduling, and health monitoring.",
        "skills": ["Veterinary record management", "Appointment scheduling", "Pet health monitoring", "Medication reminders", "Pet insurance processing", "Breeder management"],
        "capabilities": ["Manage pet health records", "Schedule vet appointments", "Monitor pet health wearables", "Send medication reminders", "Process pet insurance claims", "Manage breeder registrations"],
        "intents": ["Access pet health record", "Schedule vet appointment", "Monitor pet health", "Set medication reminder", "Process insurance claim", "Manage breeder info"],
        "tools": ["PostgreSQL", "FastAPI", "Redis", "Twilio API", "MQTT", "InfluxDB", "SendGrid API"],
        "workflows": ["health-record-management", "appointment-scheduling", "health-monitoring-alert", "insurance-claim-processing"],
    },
    "PoliOps": {
        "name": "Political Operations",
        "emoji": "🗳️",
        "desc": "Manage political campaign operations, voter outreach, donation tracking, and compliance reporting.",
        "skills": ["Voter outreach automation", "Donation management", "Campaign analytics", "Compliance reporting", "Social media management", "Canvassing coordination"],
        "capabilities": ["Automate voter outreach", "Track campaign donations", "Analyse campaign performance", "Generate compliance reports", "Manage social media", "Coordinate canvassing"],
        "intents": ["Automate voter outreach", "Track donation", "Analyse campaign", "Generate compliance report", "Manage social media", "Coordinate canvassing"],
        "tools": ["PostgreSQL", "Kafka", "Redis", "Twilio API", "FastAPI", "Grafana", "SendGrid API", "Twitter API"],
        "workflows": ["voter-outreach-pipeline", "donation-tracking-workflow", "campaign-analytics-report", "compliance-reporting"],
    },
    "PoultryOps": {
        "name": "Poultry Operations",
        "emoji": "🐔",
        "desc": "Manage poultry farm operations including flock health, feed management, and biosecurity.",
        "skills": ["Flock health monitoring", "Feed management", "Biosecurity protocols", "Egg production tracking", "Environmental control", "Slaughter scheduling"],
        "capabilities": ["Monitor flock health sensors", "Manage feed schedules", "Enforce biosecurity protocols", "Track egg production", "Control barn environment", "Schedule slaughter operations"],
        "intents": ["Monitor flock health", "Manage feed", "Enforce biosecurity", "Track egg production", "Control environment", "Schedule slaughter"],
        "tools": ["MQTT", "InfluxDB", "PostgreSQL", "Grafana", "FastAPI", "Twilio API"],
        "workflows": ["flock-health-monitoring", "feed-management-automation", "biosecurity-compliance", "production-tracking"],
    },
    "PsychOps": {
        "name": "Psychology & Mental Health Operations",
        "emoji": "🧠",
        "desc": "Support mental health services with clinical workflows, patient monitoring, and telehealth operations.",
        "skills": ["Clinical workflow automation", "Patient progress monitoring", "Telehealth platform operations", "Crisis intervention routing", "Treatment plan management", "HIPAA compliance"],
        "capabilities": ["Automate clinical workflows", "Monitor patient progress", "Operate telehealth sessions", "Route crisis interventions", "Manage treatment plans", "Ensure HIPAA compliance"],
        "intents": ["Automate clinical workflow", "Monitor patient progress", "Start telehealth session", "Route crisis call", "Manage treatment plan", "Check HIPAA compliance"],
        "tools": ["PostgreSQL", "HL7 FHIR API", "Vault", "FastAPI", "Twilio API", "Redis", "Grafana"],
        "workflows": ["clinical-workflow-automation", "patient-monitoring-pipeline", "crisis-intervention-routing", "telehealth-operations"],
    },
    "PubOps": {
        "name": "Publishing Operations",
        "emoji": "📚",
        "desc": "Automate publishing workflows including manuscript management, editorial, production, and distribution.",
        "skills": ["Manuscript management", "Editorial workflow", "Production pipeline", "Distribution management", "Rights and licensing", "Metadata management"],
        "capabilities": ["Manage manuscript submissions", "Automate editorial workflows", "Run production pipelines", "Manage distribution channels", "Track rights and licenses", "Publish metadata to catalogs"],
        "intents": ["Submit manuscript", "Run editorial review", "Manage production", "Distribute publication", "Track rights", "Manage metadata"],
        "tools": ["PostgreSQL", "MinIO", "FastAPI", "Kafka", "Grafana", "ISBN API", "SendGrid API"],
        "workflows": ["manuscript-submission-pipeline", "editorial-workflow", "production-pipeline", "distribution-management"],
    },
    "QualiOps": {
        "name": "Quality Operations",
        "emoji": "✅",
        "desc": "Automate quality management including inspection, non-conformance, corrective action, and auditing.",
        "skills": ["Quality inspection automation", "Non-conformance management", "Corrective action workflows", "Statistical process control", "Supplier quality management", "Audit management"],
        "capabilities": ["Automate quality inspections", "Manage non-conformances", "Run corrective action workflows", "Apply SPC analysis", "Manage supplier quality", "Conduct and track audits"],
        "intents": ["Run quality inspection", "Log non-conformance", "Initiate corrective action", "Apply SPC analysis", "Manage supplier quality", "Conduct audit"],
        "tools": ["PostgreSQL", "Grafana", "Kafka", "FastAPI", "MinIO", "Prometheus", "Slack API"],
        "workflows": ["inspection-automation-pipeline", "non-conformance-management", "corrective-action-workflow", "audit-management"],
    },
    "RAGOps": {
        "name": "Retrieval-Augmented Generation Operations",
        "emoji": "📚",
        "desc": "Operate RAG pipelines including document ingestion, vector store management, retrieval optimization, and quality evaluation.",
        "skills": ["Document ingestion pipelines", "Vector store management", "Retrieval optimization", "RAG evaluation", "Embedding model management", "Chunking strategy optimization"],
        "capabilities": ["Ingest and chunk documents", "Manage vector databases", "Optimize retrieval quality", "Evaluate RAG pipeline quality", "Manage embedding models", "Tune chunking strategies"],
        "intents": ["Ingest documents", "Query vector store", "Evaluate retrieval quality", "Optimize chunking", "Manage embeddings", "Monitor RAG pipeline"],
        "tools": ["Qdrant", "Weaviate", "Chroma", "LangChain", "LlamaIndex", "Ollama", "MinIO", "PostgreSQL", "LangSmith"],
        "workflows": ["document-ingestion-pipeline", "vector-store-management", "retrieval-evaluation", "embedding-model-update"],
    },
    "RealOps": {
        "name": "Real Estate Operations",
        "emoji": "🏘️",
        "desc": "Automate property management, listing management, tenant workflows, and investment analytics.",
        "skills": ["Property management automation", "Listing management", "Tenant workflow automation", "Lease management", "Investment analytics", "Maintenance scheduling"],
        "capabilities": ["Manage property portfolios", "Automate listing workflows", "Handle tenant requests", "Manage lease lifecycles", "Analyse investment returns", "Schedule property maintenance"],
        "intents": ["Manage property portfolio", "Create listing", "Handle tenant request", "Manage lease", "Analyse investment", "Schedule maintenance"],
        "tools": ["PostgreSQL + PostGIS", "FastAPI", "Redis", "Kafka", "Grafana", "Docusign API", "Twilio API"],
        "workflows": ["listing-management-pipeline", "tenant-workflow-automation", "lease-lifecycle-management", "investment-analytics"],
    },
    "ReliOps": {
        "name": "Reliability Operations",
        "emoji": "🔋",
        "desc": "Manage SRE practices including SLO management, error budgets, reliability testing, and chaos engineering.",
        "skills": ["SLO/SLA management", "Error budget tracking", "Reliability testing", "Chaos engineering", "Toil automation", "Incident management"],
        "capabilities": ["Define and track SLOs", "Monitor error budgets", "Run reliability tests", "Execute chaos experiments", "Automate toil reduction", "Manage incident lifecycle"],
        "intents": ["Define SLO", "Check error budget", "Run reliability test", "Execute chaos experiment", "Reduce toil", "Manage incident"],
        "tools": ["Prometheus", "Grafana", "Chaos Monkey", "LitmusChaos", "PagerDuty", "Blameless", "PostgreSQL"],
        "workflows": ["slo-monitoring-pipeline", "error-budget-tracking", "chaos-experiment-runner", "incident-management-loop"],
    },
    "ResearOps": {
        "name": "Research Operations",
        "emoji": "🔬",
        "desc": "Automate research workflows including data collection, analysis pipelines, publication, and collaboration.",
        "skills": ["Research data management", "Analysis pipeline automation", "Literature review automation", "Publication workflow", "Research collaboration", "Grant management"],
        "capabilities": ["Manage research datasets", "Build analysis pipelines", "Automate literature reviews", "Manage publication submissions", "Coordinate research teams", "Track grant milestones"],
        "intents": ["Manage research data", "Build analysis pipeline", "Review literature", "Submit publication", "Coordinate team", "Track grant"],
        "tools": ["PostgreSQL", "MinIO", "Jupyter", "Apache Spark", "FastAPI", "Semantic Scholar API", "Grafana"],
        "workflows": ["data-collection-pipeline", "analysis-automation", "literature-review-workflow", "publication-submission"],
    },
    "RetaiOps": {
        "name": "Retail Operations",
        "emoji": "🛍️",
        "desc": "Automate retail operations including inventory, pricing, customer experience, and supply chain.",
        "skills": ["Inventory optimization", "Dynamic pricing", "Customer experience automation", "Supply chain management", "Omnichannel operations", "Returns management"],
        "capabilities": ["Optimize inventory levels", "Apply dynamic pricing", "Personalize customer experience", "Manage supply chain", "Coordinate omnichannel operations", "Automate returns processing"],
        "intents": ["Optimize inventory", "Set pricing", "Personalize experience", "Manage supply chain", "Coordinate omnichannel", "Process return"],
        "tools": ["PostgreSQL", "Redis", "Kafka", "FastAPI", "Grafana", "Shopify API", "Stripe API"],
        "workflows": ["inventory-optimization-pipeline", "dynamic-pricing-engine", "customer-personalization", "supply-chain-coordination"],
    },
    "SagaOps": {
        "name": "Saga Pattern Operations",
        "emoji": "📖",
        "desc": "Implement and operate distributed saga patterns for managing long-running transactions across microservices.",
        "skills": ["Saga orchestration", "Saga choreography", "Compensating transactions", "Distributed state management", "Event sourcing", "Idempotency management"],
        "capabilities": ["Orchestrate distributed sagas", "Manage compensating transactions", "Implement choreography-based sagas", "Track distributed state", "Implement event sourcing", "Ensure idempotency"],
        "intents": ["Implement saga pattern", "Manage compensation", "Choreograph saga", "Track state", "Implement event sourcing", "Ensure idempotency"],
        "tools": ["Temporal", "Kafka", "PostgreSQL (event store)", "Redis", "FastAPI", "Grafana", "Jaeger"],
        "workflows": ["saga-orchestration-pipeline", "compensation-management", "event-sourcing-pipeline", "distributed-state-tracking"],
    },
    "SciOps": {
        "name": "Scientific Operations",
        "emoji": "🔭",
        "desc": "Automate scientific computing workflows, experiment tracking, data management, and publication.",
        "skills": ["Scientific workflow automation", "HPC management", "Experiment tracking", "Scientific data management", "Simulation pipeline", "Publication workflow"],
        "capabilities": ["Automate scientific workflows", "Manage HPC job scheduling", "Track experiments and results", "Store and retrieve scientific data", "Run simulation pipelines", "Manage publication submissions"],
        "intents": ["Run scientific workflow", "Submit HPC job", "Track experiment", "Store scientific data", "Run simulation", "Submit publication"],
        "tools": ["Slurm API", "Apache Airflow", "MLflow", "MinIO", "PostgreSQL", "Jupyter", "FastAPI"],
        "workflows": ["scientific-workflow-automation", "hpc-job-scheduling", "experiment-tracking", "simulation-pipeline"],
    },
    "SecOps": {
        "name": "Security Operations",
        "emoji": "🔐",
        "desc": "Automate security monitoring, threat detection, incident response, and vulnerability management.",
        "skills": ["SIEM operations", "Threat detection", "Incident response automation", "Vulnerability management", "Threat intelligence", "Security orchestration (SOAR)"],
        "capabilities": ["Monitor security events via SIEM", "Detect threats automatically", "Automate incident response playbooks", "Manage vulnerability lifecycle", "Process threat intelligence feeds", "Orchestrate security tools via SOAR"],
        "intents": ["Monitor security events", "Detect threat", "Respond to incident", "Manage vulnerability", "Process threat intel", "Orchestrate security tools"],
        "tools": ["Wazuh", "Elastic SIEM", "TheHive", "Cortex", "OpenCTI", "Shuffle SOAR", "Prometheus", "Grafana"],
        "workflows": ["threat-detection-pipeline", "incident-response-playbook", "vulnerability-management-cycle", "threat-intel-processing"],
    },
    "ServiceMeshOps": {
        "name": "Service Mesh Operations",
        "emoji": "🕸️",
        "desc": "Operate service mesh infrastructure including traffic management, mTLS, observability, and policy enforcement.",
        "skills": ["Traffic management", "mTLS enforcement", "Service mesh observability", "Policy enforcement", "Canary routing", "Multi-cluster mesh"],
        "capabilities": ["Manage traffic routing rules", "Enforce mTLS between services", "Observe service-to-service traffic", "Enforce mesh policies", "Configure canary deployments", "Operate multi-cluster mesh"],
        "intents": ["Configure traffic routing", "Enforce mTLS", "Observe service traffic", "Enforce policy", "Set up canary route", "Manage multi-cluster mesh"],
        "tools": ["Istio", "Linkerd", "Envoy", "Kiali", "Jaeger", "Prometheus", "Grafana", "Kubernetes"],
        "workflows": ["traffic-management-pipeline", "mtls-enforcement", "mesh-observability", "canary-routing-setup"],
    },
    "ServOps": {
        "name": "Service Operations",
        "emoji": "🎯",
        "desc": "Automate service delivery, SLA management, customer success, and support operations.",
        "skills": ["Service catalogue management", "SLA monitoring", "Customer success automation", "Support ticket automation", "Knowledge base management", "CSAT measurement"],
        "capabilities": ["Manage service catalogue", "Monitor SLAs in real time", "Automate customer success workflows", "Route and resolve support tickets", "Maintain knowledge base", "Measure customer satisfaction"],
        "intents": ["Manage service catalogue", "Monitor SLA", "Automate customer success", "Route support ticket", "Update knowledge base", "Measure CSAT"],
        "tools": ["Zendesk API", "ServiceNow API", "PostgreSQL", "Kafka", "Redis", "Grafana", "Slack API"],
        "workflows": ["sla-monitoring-pipeline", "ticket-routing-automation", "customer-success-workflow", "csat-measurement"],
    },
    "SocioOps": {
        "name": "Social Operations",
        "emoji": "🌍",
        "desc": "Automate social impact operations including community management, grant tracking, and impact measurement.",
        "skills": ["Community management", "Grant lifecycle management", "Impact measurement", "Volunteer coordination", "Social media management", "Reporting automation"],
        "capabilities": ["Manage community workflows", "Track grant applications and lifecycle", "Measure social impact metrics", "Coordinate volunteers", "Manage social media presence", "Generate impact reports"],
        "intents": ["Manage community", "Track grant", "Measure impact", "Coordinate volunteers", "Manage social media", "Generate impact report"],
        "tools": ["PostgreSQL", "Kafka", "FastAPI", "SendGrid API", "Slack API", "Grafana", "Salesforce API"],
        "workflows": ["community-management-pipeline", "grant-lifecycle-tracking", "impact-measurement-report", "volunteer-coordination"],
    },
    "SpaceOps": {
        "name": "Space Operations",
        "emoji": "🚀",
        "desc": "Manage space mission operations including telemetry processing, satellite management, and ground systems.",
        "skills": ["Telemetry processing", "Satellite constellation management", "Ground station operations", "Mission planning", "Orbital mechanics automation", "Space weather monitoring"],
        "capabilities": ["Process satellite telemetry", "Manage satellite constellations", "Operate ground stations", "Plan and schedule missions", "Calculate orbital maneuvers", "Monitor space weather"],
        "intents": ["Process telemetry", "Manage satellite", "Operate ground station", "Plan mission", "Calculate maneuver", "Monitor space weather"],
        "tools": ["Kafka", "InfluxDB", "PostgreSQL", "Grafana", "FastAPI", "NASA APIs", "STK integration"],
        "workflows": ["telemetry-processing-pipeline", "satellite-health-monitoring", "mission-planning-workflow", "ground-station-ops"],
    },
    "SporOps": {
        "name": "Sports Operations",
        "emoji": "⚽",
        "desc": "Automate sports team management, performance analytics, fan engagement, and venue operations.",
        "skills": ["Athlete performance analytics", "Team management automation", "Fan engagement", "Venue operations", "Broadcasting coordination", "Sports betting compliance"],
        "capabilities": ["Analyse athlete performance", "Manage team schedules", "Engage fans with personalization", "Operate venue systems", "Coordinate broadcasting", "Ensure betting compliance"],
        "intents": ["Analyse athlete performance", "Manage team schedule", "Engage fans", "Operate venue", "Coordinate broadcast", "Check betting compliance"],
        "tools": ["PostgreSQL", "Kafka", "Redis", "FastAPI", "Grafana", "Wearable sensor APIs", "Stripe API"],
        "workflows": ["performance-analytics-pipeline", "team-management-workflow", "fan-engagement-automation", "venue-operations"],
    },
    "TaxOps": {
        "name": "Tax Operations",
        "emoji": "🧾",
        "desc": "Automate tax compliance, filing, international tax management, and audit support.",
        "skills": ["Tax compliance automation", "Multi-jurisdiction tax", "Tax filing automation", "Transfer pricing", "Audit trail management", "Indirect tax management"],
        "capabilities": ["Automate tax compliance checks", "Manage multi-jurisdiction taxes", "Automate tax filings", "Manage transfer pricing documentation", "Maintain audit trails", "Calculate and report VAT/GST"],
        "intents": ["Check tax compliance", "File tax return", "Manage international tax", "Document transfer pricing", "Prepare audit trail", "Calculate VAT/GST"],
        "tools": ["PostgreSQL", "Vertex API", "Avalara API", "FastAPI", "MinIO", "Grafana", "Kafka"],
        "workflows": ["tax-compliance-pipeline", "multi-jurisdiction-calculation", "filing-automation", "audit-trail-management"],
    },
    "TechnoOps": {
        "name": "Technology Operations",
        "emoji": "🔬",
        "desc": "Manage technology R&D operations, patent management, innovation pipelines, and tech transfer.",
        "skills": ["R&D project management", "Patent lifecycle management", "Innovation pipeline", "Technology transfer", "IP compliance", "Tech scouting"],
        "capabilities": ["Manage R&D projects", "Track patent lifecycles", "Manage innovation pipeline", "Facilitate technology transfer", "Ensure IP compliance", "Scout emerging technologies"],
        "intents": ["Manage R&D project", "Track patent", "Manage innovation pipeline", "Transfer technology", "Check IP compliance", "Scout technology"],
        "tools": ["PostgreSQL", "FastAPI", "MinIO", "Grafana", "Semantic Scholar API", "Kafka", "Jira API"],
        "workflows": ["rd-project-management", "patent-lifecycle-tracking", "innovation-pipeline", "technology-transfer-workflow"],
    },
    "TradeOps": {
        "name": "Trade Operations",
        "emoji": "🌏",
        "desc": "Automate international trade operations including customs, trade finance, sanctions screening, and logistics.",
        "skills": ["Customs compliance", "Trade finance automation", "Sanctions screening", "Trade document management", "Tariff management", "Supply chain visibility"],
        "capabilities": ["Automate customs declarations", "Process trade finance documents", "Screen against sanctions lists", "Manage trade documents", "Calculate and apply tariffs", "Provide supply chain visibility"],
        "intents": ["Process customs declaration", "Manage trade finance", "Screen for sanctions", "Manage trade documents", "Calculate tariff", "Track supply chain"],
        "tools": ["PostgreSQL", "Kafka", "FastAPI", "Vault", "MinIO", "Grafana", "OFAC/UN sanctions APIs"],
        "workflows": ["customs-automation-pipeline", "trade-finance-workflow", "sanctions-screening-loop", "tariff-calculation"],
    },
    "TransOps": {
        "name": "Transportation Operations",
        "emoji": "🚆",
        "desc": "Manage transportation networks, scheduling, real-time tracking, and passenger experience.",
        "skills": ["Transport network management", "Schedule optimization", "Real-time tracking", "Passenger experience", "Fleet maintenance", "Revenue management"],
        "capabilities": ["Manage transport networks", "Optimize schedules", "Track vehicles in real time", "Enhance passenger experience", "Schedule fleet maintenance", "Optimize revenue management"],
        "intents": ["Manage transport network", "Optimize schedule", "Track vehicle", "Enhance passenger experience", "Schedule maintenance", "Optimize revenue"],
        "tools": ["PostgreSQL + PostGIS", "Kafka", "Redis", "FastAPI", "Grafana", "HERE API", "Twilio API"],
        "workflows": ["schedule-optimization-pipeline", "real-time-tracking", "passenger-experience-automation", "revenue-management"],
    },
    "WASMOps": {
        "name": "WebAssembly Operations",
        "emoji": "🕸️",
        "desc": "Operate WebAssembly workloads including edge deployment, module management, and performance optimization.",
        "skills": ["WASM module management", "Edge deployment", "WASI runtime operations", "Performance profiling", "Security sandboxing", "Component model management"],
        "capabilities": ["Deploy WASM modules to edge", "Manage WASM module registry", "Operate WASI runtimes", "Profile WASM performance", "Enforce security sandboxing", "Manage WASM component model"],
        "intents": ["Deploy WASM module", "Manage module registry", "Operate WASI runtime", "Profile performance", "Enforce sandbox", "Manage component model"],
        "tools": ["Wasmtime", "WasmEdge", "Wasm registry", "Spin (Fermyon)", "Fastly Compute@Edge", "Prometheus", "Grafana"],
        "workflows": ["module-deployment-pipeline", "edge-deployment-workflow", "performance-profiling", "security-sandbox-enforcement"],
    },
    "WastOps": {
        "name": "Waste Management Operations",
        "emoji": "♻️",
        "desc": "Automate waste collection routing, recycling tracking, environmental compliance, and circular economy workflows.",
        "skills": ["Collection route optimization", "Recycling stream management", "Environmental compliance", "Waste analytics", "Circular economy workflows", "Smart bin monitoring"],
        "capabilities": ["Optimize waste collection routes", "Track recycling streams", "Monitor environmental compliance", "Analyse waste data", "Support circular economy workflows", "Monitor smart bins"],
        "intents": ["Optimize collection route", "Track recycling", "Check compliance", "Analyse waste data", "Support circular economy", "Monitor smart bins"],
        "tools": ["PostgreSQL + PostGIS", "MQTT", "InfluxDB", "Grafana", "HERE API", "FastAPI", "Kafka"],
        "workflows": ["route-optimization-pipeline", "recycling-tracking", "compliance-monitoring", "smart-bin-telemetry"],
    },
    "WaterOps": {
        "name": "Water Operations",
        "emoji": "💧",
        "desc": "Automate water utility operations including network monitoring, quality management, and demand forecasting.",
        "skills": ["Water network monitoring", "Quality management", "Demand forecasting", "Leak detection", "Treatment automation", "Regulatory compliance"],
        "capabilities": ["Monitor water network sensors", "Manage water quality parameters", "Forecast water demand", "Detect and locate leaks", "Automate water treatment", "Ensure regulatory compliance"],
        "intents": ["Monitor water network", "Manage water quality", "Forecast demand", "Detect leak", "Automate treatment", "Check compliance"],
        "tools": ["MQTT", "InfluxDB", "PostgreSQL", "Grafana", "FastAPI", "Prophet", "SCADA integration"],
        "workflows": ["network-monitoring-pipeline", "quality-management-workflow", "demand-forecast-model", "leak-detection-alert"],
    },
    "WearOps": {
        "name": "Wearable Technology Operations",
        "emoji": "⌚",
        "desc": "Manage wearable device fleets, health data pipelines, firmware updates, and user privacy compliance.",
        "skills": ["Wearable device management", "Health data pipeline", "OTA firmware updates", "Privacy compliance", "Health analytics", "Alert management"],
        "capabilities": ["Manage wearable device fleets", "Process health data streams", "Push OTA firmware updates", "Ensure HIPAA/GDPR compliance", "Analyse health metrics", "Alert on health anomalies"],
        "intents": ["Manage wearable fleet", "Process health data", "Push firmware update", "Check privacy compliance", "Analyse health metrics", "Set health alert"],
        "tools": ["MQTT", "InfluxDB", "PostgreSQL", "Kafka", "FastAPI", "Grafana", "Vault"],
        "workflows": ["health-data-pipeline", "ota-update-rollout", "privacy-compliance-check", "health-anomaly-detection"],
    },
    "Web3Ops": {
        "name": "Web3 Operations",
        "emoji": "🌐",
        "desc": "Operate Web3 infrastructure including DeFi protocols, NFT platforms, DAO governance, and node management.",
        "skills": ["DeFi protocol operations", "NFT platform management", "DAO governance", "Node management", "Smart contract monitoring", "Cross-chain operations"],
        "capabilities": ["Operate DeFi protocols", "Manage NFT platforms", "Run DAO governance workflows", "Manage blockchain nodes", "Monitor smart contracts", "Bridge assets cross-chain"],
        "intents": ["Operate DeFi protocol", "Manage NFT platform", "Run DAO governance", "Manage node", "Monitor smart contract", "Bridge cross-chain"],
        "tools": ["Web3.py", "Hardhat", "The Graph", "OpenZeppelin", "IPFS", "PostgreSQL", "Prometheus", "Grafana"],
        "workflows": ["defi-protocol-operations", "nft-platform-management", "dao-governance-workflow", "node-health-monitoring"],
    },
    "WebOps": {
        "name": "Web Operations",
        "emoji": "🌐",
        "desc": "Operate web infrastructure including CDN management, performance optimization, security, and deployments.",
        "skills": ["CDN management", "Web performance optimization", "Web security", "Edge deployment", "SEO operations", "Accessibility compliance"],
        "capabilities": ["Manage CDN configuration", "Optimize Core Web Vitals", "Enforce web security headers", "Deploy to edge networks", "Monitor SEO health", "Audit accessibility compliance"],
        "intents": ["Manage CDN", "Optimize performance", "Enforce security", "Deploy to edge", "Monitor SEO", "Audit accessibility"],
        "tools": ["Cloudflare API", "Fastly API", "Lighthouse CI", "WebPageTest API", "Prometheus", "Grafana", "NextJS"],
        "workflows": ["cdn-management-pipeline", "performance-optimization", "security-header-enforcement", "edge-deployment"],
    },
    "WomenOps": {
        "name": "Women in Tech & DEI Operations",
        "emoji": "👩‍💻",
        "desc": "Support DEI initiatives, mentorship programs, pay equity analysis, and inclusive hiring workflows.",
        "skills": ["Pay equity analysis", "Inclusive hiring workflow", "Mentorship program management", "DEI metrics tracking", "ERG management", "Bias detection"],
        "capabilities": ["Analyse pay equity across roles", "Run inclusive hiring workflows", "Manage mentorship programs", "Track DEI metrics", "Coordinate ERG activities", "Detect bias in processes"],
        "intents": ["Analyse pay equity", "Run inclusive hiring", "Manage mentorship", "Track DEI metrics", "Coordinate ERG", "Detect bias"],
        "tools": ["PostgreSQL", "FastAPI", "Grafana", "Slack API", "SendGrid API", "HR system APIs"],
        "workflows": ["pay-equity-analysis", "inclusive-hiring-pipeline", "mentorship-management", "dei-metrics-reporting"],
    },
    "WorkOps": {
        "name": "Workplace Operations",
        "emoji": "🏢",
        "desc": "Automate workplace management including space booking, facilities, visitor management, and employee experience.",
        "skills": ["Space booking management", "Facilities management", "Visitor management", "Employee experience", "Hybrid work coordination", "Asset management"],
        "capabilities": ["Manage desk and room bookings", "Coordinate facilities management", "Handle visitor check-in/out", "Enhance employee experience", "Coordinate hybrid work schedules", "Track workplace assets"],
        "intents": ["Book desk/room", "Manage facilities", "Check in visitor", "Enhance employee experience", "Coordinate hybrid work", "Track asset"],
        "tools": ["PostgreSQL", "Redis", "FastAPI", "Slack API", "Twilio API", "Grafana", "Calendar API"],
        "workflows": ["space-booking-automation", "facilities-management", "visitor-management-flow", "hybrid-work-coordination"],
    },
}


def slugify(text: str) -> str:
    return text.lower().replace(" ", "-").replace("/", "-").replace("&", "and")


def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"  ✓ {path.relative_to(ROOT)}")


def generate_agent_md(folder: str, d: dict) -> str:
    return f"""# {d['emoji']} {d['name']} Agent

## Identity

| Field | Value |
|-------|-------|
| **Name** | `{folder.lower()}-agent` |
| **Domain** | {d['name']} |
| **Version** | 1.0.0 |
| **Framework** | Multi-framework (CrewAI · LangGraph · AutoGen · AgentScope) |
| **Persona** | Expert autonomous agent for {d['desc'].split('.')[0].lower()} |

## Description

{d['desc']}

## Role

This agent acts as an intelligent operations assistant for **{d['name']}**, capable of
understanding natural language instructions, invoking domain-specific tools, and
coordinating with other agents to complete complex multi-step tasks.

## Invocation

```python
from agents import create_agent

agent = create_agent("{folder.lower()}")
result = agent.run("Your {d['name']} task here")
```

## Related Files

| File | Purpose |
|------|---------|
| `skills.md` | Domain skills this agent possesses |
| `capabilities.md` | Concrete actions this agent can perform |
| `intents.md` | User intents and example prompts |
| `tools.md` | Tools and integrations available |
| `workflows.md` | Agent workflow patterns |
| `config.yaml` | Machine-readable configuration |
| `prompts/system.md` | System prompt definition |
| `prompts/examples.md` | Few-shot prompt examples |
"""


def generate_skills_md(folder: str, d: dict) -> str:
    skills_list = "\n".join(f"- **{s}**" for s in d["skills"])
    return f"""# {d['emoji']} {d['name']} Agent — Skills

## Core Domain Skills

{skills_list}

## Skill Proficiency Matrix

| Skill | Level | Description |
|-------|-------|-------------|
{"".join(f'| {s} | ⭐⭐⭐⭐ | Expert-level {s.lower()} for {d["name"].lower()} |{chr(10)}' for s in d["skills"])}

## Skill Acquisition

Skills are acquired through:
1. **Domain knowledge base** — curated {d['name']} documentation
2. **Tool mastery** — deep integration with domain-specific tools
3. **Pattern library** — proven {d['name']} workflow patterns
4. **Feedback loops** — continuous improvement from outcomes

## Cross-Domain Skills

- Natural language understanding
- Multi-step reasoning and planning
- Tool orchestration
- Data analysis and summarization
- Report generation
- Stakeholder communication
"""


def generate_capabilities_md(folder: str, d: dict) -> str:
    caps_list = "\n".join(f"| {c} | ✅ | Available | Tools |" for c in d["capabilities"])
    return f"""# {d['emoji']} {d['name']} Agent — Capabilities

## Capability Overview

This agent can perform the following **{len(d["capabilities"])} core capabilities**
in the {d['name']} domain.

## Capability Matrix

| Capability | Status | Availability | Method |
|-----------|--------|--------------|--------|
{caps_list}

## Capability Details

{"".join(f"""### {cap}

- **Input**: Natural language request or structured parameters
- **Output**: Structured result with status, data, and recommendations
- **Tools required**: See [tools.md](tools.md)
- **Estimated duration**: < 30 seconds for simple queries, < 5 minutes for complex workflows

""" for cap in d["capabilities"])}

## Limitations

- Cannot execute destructive actions without human approval
- Requires valid credentials and network access to external services
- Complex multi-system workflows may require human-in-the-loop confirmation
"""


def generate_intents_md(folder: str, d: dict) -> str:
    intents_section = ""
    for i, intent in enumerate(d["intents"], 1):
        slug = slugify(intent)
        intents_section += f"""### Intent {i}: {intent}

- **Trigger phrases**: "{intent}", "I need to {intent.lower()}", "Help me {intent.lower()}"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: {intent}
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

"""
    return f"""# {d['emoji']} {d['name']} Agent — Intents

## Supported Intents

This agent handles **{len(d["intents"])} primary intents** in the {d['name']} domain.

{intents_section}

## Intent Routing

Intents are classified using:
1. **Keyword matching** — domain-specific keyword extraction
2. **Semantic similarity** — embedding-based intent classification
3. **LLM reasoning** — for ambiguous or compound intents

## Fallback Behaviour

If an intent cannot be matched:
1. Agent asks for clarification
2. Suggests the most similar supported intent
3. Escalates to human operator if needed
"""


def generate_tools_md(folder: str, d: dict) -> str:
    tools_list = "\n".join(f"| {t} | Integrated | See config.yaml |" for t in d["tools"])
    return f"""# {d['emoji']} {d['name']} Agent — Tools

## Tool Inventory

| Tool | Status | Configuration |
|------|--------|---------------|
{tools_list}

## Tool Integration Patterns

### Direct API Calls
Tools that expose REST/GraphQL APIs are called directly with authenticated clients.

### Message Queue Tools
Kafka-based tools use producer/consumer patterns for async processing.

### Database Tools
PostgreSQL and time-series databases are accessed via connection pools with
parameterized queries (no string interpolation — SQL injection safe).

### Sensor / IoT Tools
MQTT-based tools subscribe to topic hierarchies and push data to InfluxDB.

## Tool Authentication

All credentials are stored in **HashiCorp Vault** or environment variables.
Never hardcoded. Rotated on a schedule defined in `config.yaml`.

## Adding New Tools

1. Define tool in `agents/tools/` as a `BaseTool` subclass
2. Register in `config.yaml` under `tools:`
3. Add integration test in `tests/tools/`
4. Document here with status and config reference
"""


def generate_workflows_md(folder: str, d: dict) -> str:
    wf_section = ""
    for wf in d["workflows"]:
        wf_title = wf.replace("-", " ").title()
        wf_section += f"""### {wf_title}

```
trigger → {wf} → [tool calls] → result → notify
```

- **Pattern**: Sequential with conditional branching
- **Trigger**: User intent or scheduled cron
- **Steps**: Plan → Execute → Validate → Report
- **On failure**: Retry with backoff → Escalate → Human-in-the-loop

"""
    return f"""# {d['emoji']} {d['name']} Agent — Workflows

## Workflow Patterns

This agent supports **{len(d["workflows"])} primary workflow patterns**.

{wf_section}

## Workflow Design Principles

1. **Idempotency** — safe to retry without side effects
2. **Observability** — all steps emit structured logs and metrics
3. **Compensation** — failed workflows trigger rollback/cleanup
4. **Human-in-the-loop** — destructive actions require approval
5. **Timeout handling** — all steps have explicit timeouts

## Workflow Orchestration

Workflows are orchestrated via:
- **LangGraph** — for stateful, cyclic agent workflows
- **Temporal** — for long-running, durable workflows
- **Celery** — for distributed task queues
"""


def generate_config_yaml(folder: str, d: dict) -> str:
    tools_yaml = "\n".join(f"  - name: {t.split(' ')[0].lower().replace('(', '').replace(')', '')}\n    enabled: true" for t in d["tools"])
    workflows_yaml = "\n".join(f"  - {wf}" for wf in d["workflows"])
    return f"""# Agent Configuration — {folder}
# Auto-generated by generate_agent_structures.py

agent:
  id: {folder.lower()}-agent
  name: "{d['name']} Agent"
  version: "1.0.0"
  domain: "{folder}"
  emoji: "{d['emoji']}"
  description: >
    {d['desc']}

llm:
  provider: ollama          # Switch to: openai | anthropic | azure
  model: llama3
  base_url: http://ollama:11434
  temperature: 0.1
  max_tokens: 4096
  fallback_provider: openai
  fallback_model: gpt-4o

memory:
  enabled: true
  provider: redis
  url: redis://redis:6379
  ttl_seconds: 86400
  vector_store: qdrant

tools:
{tools_yaml}

workflows:
{workflows_yaml}

human_in_the_loop:
  enabled: true
  triggers:
    - destructive_action
    - high_cost_operation
    - compliance_critical
  approval_channel: slack
  timeout_seconds: 300

observability:
  tracing: true
  tracing_provider: langsmith
  metrics: true
  metrics_port: 9090
  log_level: INFO

security:
  secrets_provider: vault
  vault_addr: http://vault:8200
  credential_rotation_days: 90
  audit_log: true

rate_limits:
  requests_per_minute: 60
  tokens_per_minute: 100000
"""


def generate_system_prompt_md(folder: str, d: dict) -> str:
    skills_inline = ", ".join(d["skills"])
    return f"""# {d['emoji']} {d['name']} Agent — System Prompt

## System Prompt (v1.0.0)

```
You are an expert autonomous agent specializing in {d['name']}.

## Your Role
{d['desc']}

## Your Skills
You have deep expertise in: {skills_inline}.

## Your Behaviour
1. **Think step-by-step** before taking any action.
2. **Use tools** to gather information before making decisions.
3. **Validate** your understanding by checking inputs and outputs.
4. **Ask for clarification** if the request is ambiguous.
5. **Seek human approval** before executing destructive or irreversible actions.
6. **Be concise** — provide structured, actionable responses.
7. **Log everything** — emit structured observations at each step.

## Response Format
Always respond in this structure:
- **Understanding**: Restate what you were asked to do
- **Plan**: List the steps you will take
- **Actions**: Execute steps, reporting each result
- **Summary**: Summarize what was done and any follow-up needed

## Constraints
- Never hardcode credentials or secrets
- Never execute SQL with string interpolation (use parameterized queries)
- Never perform irreversible operations without explicit human confirmation
- Always validate inputs at system boundaries
- Respect rate limits of all integrated APIs
```

## Prompt Versioning

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-04-24 | Initial system prompt |
"""


def generate_examples_md(folder: str, d: dict) -> str:
    examples = ""
    for intent in d["intents"][:3]:
        cap = d["capabilities"][d["intents"].index(intent) % len(d["capabilities"])]
        examples += f"""---

### Example: {intent}

**User:**
```
{intent}
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to {intent.lower()}
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: {d['tools'][0].split(' ')[0]} → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: {intent}

Actions taken:
- Retrieved current state using {d['tools'][0].split(' ')[0]}
- Applied {d['capabilities'][0].lower()} logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

"""
    return f"""# {d['emoji']} {d['name']} Agent — Prompt Examples

## Few-Shot Examples

These examples demonstrate the agent's expected reasoning and response patterns.

{examples}
"""


# ─────────────────────────────────────────────────────────────────────────────
# Main generation loop
# ─────────────────────────────────────────────────────────────────────────────
def main():
    generated = 0
    skipped = 0

    for folder_name in sorted(ROOT.iterdir()):
        if not folder_name.is_dir():
            continue
        if folder_name.name in ("scripts", ".git", "__pycache__", "node_modules"):
            continue
        if not folder_name.name.endswith("Ops"):
            continue

        domain = DOMAINS.get(folder_name.name)
        if not domain:
            # Generate minimal generic entry for unknown domains
            domain = {
                "name": f"{folder_name.name.replace('Ops', '')} Operations",
                "emoji": "⚙️",
                "desc": f"Automate and optimize {folder_name.name.replace('Ops', '').lower()} operations with intelligent agentic workflows.",
                "skills": ["Process automation", "Data analysis", "Workflow orchestration", "Monitoring and alerting", "Report generation"],
                "capabilities": ["Automate workflows", "Monitor systems", "Generate reports", "Integrate external services", "Coordinate multi-agent tasks"],
                "intents": ["Automate a workflow", "Monitor system health", "Generate a report", "Integrate a service", "Coordinate agents"],
                "tools": ["PostgreSQL", "Redis", "Kafka", "FastAPI", "Grafana", "Prometheus"],
                "workflows": ["automation-pipeline", "monitoring-workflow", "report-generation", "integration-pipeline"],
            }
            skipped += 1

        agent_dir = folder_name / ".agent"
        print(f"\n📁 {folder_name.name}/")

        write(agent_dir / "agent.md", generate_agent_md(folder_name.name, domain))
        write(agent_dir / "skills.md", generate_skills_md(folder_name.name, domain))
        write(agent_dir / "capabilities.md", generate_capabilities_md(folder_name.name, domain))
        write(agent_dir / "intents.md", generate_intents_md(folder_name.name, domain))
        write(agent_dir / "tools.md", generate_tools_md(folder_name.name, domain))
        write(agent_dir / "workflows.md", generate_workflows_md(folder_name.name, domain))
        write(agent_dir / "config.yaml", generate_config_yaml(folder_name.name, domain))
        write(agent_dir / "prompts" / "system.md", generate_system_prompt_md(folder_name.name, domain))
        write(agent_dir / "prompts" / "examples.md", generate_examples_md(folder_name.name, domain))

        generated += 1

    print(f"\nDone. Generated .agent/ structures for {generated} ops folders")
    if skipped:
        print(f"Note: {skipped} folders used fallback generic metadata (add to DOMAINS dict)")


if __name__ == "__main__":
    main()
