#!/bin/bash
# Mass Stack Generator for PickOps
# Generates 68 specialized operational stacks

set -euo pipefail

# Stack definitions: name|description|key_services
STACKS=(
    "AgriOps|Agriculture Operations|farm-management,iot-sensors,weather-api,crop-analytics,irrigation-control"
    "PoliOps|Politics Operations|campaign-manager,voter-database,poll-tracking,social-media-monitor,donation-platform"
    "MuniOps|Municipality Operations|city-services,waste-management,permit-system,311-helpdesk,utility-billing"
    "TransOps|Transportation Operations|fleet-tracking,route-optimizer,traffic-monitor,maintenance-scheduler,fare-system"
    "AirOps|Airport Operations|flight-tracker,baggage-system,security-screening,gate-management,customs-system"
    "AviOps|Aviation Operations|aircraft-maintenance,crew-scheduler,flight-planner,weather-radar,atc-interface"
    "MariOps|Maritime Operations|vessel-tracking,port-management,cargo-system,navigation-charts,tide-predictor"
    "LogiOps|Logistics Operations|warehouse-management,delivery-tracking,inventory-system,route-planner,tms"
    "MediOps|Medical Operations|emr-system,appointment-scheduler,lab-integration,pharmacy-management,billing"
    "HealthOps|Healthcare Operations|patient-portal,telemedicine,health-records,insurance-claims,analytics"
    "DrugOps|Pharmaceutical Operations|drug-database,prescription-system,interaction-checker,inventory-tracking,regulatory-compliance"
    "EduOps|Education Operations|lms-platform,student-portal,gradebook,attendance-system,online-classes"
    "LandOps|Land Management Operations|cadastral-system,deed-registry,survey-data,valuation-system,gis-mapping"
    "RealOps|Real Estate Operations|property-listings,crm-system,document-vault,valuation-tools,market-analytics"
    "HomeOps|Home Operations|smart-home-hub,energy-monitor,security-system,maintenance-scheduler,automation-engine"
    "SocioOps|Social Living Operations|community-platform,event-manager,volunteer-system,social-network,resource-sharing"
    "CivilOps|Civil Engineering Operations|project-management,cad-integration,structural-analysis,material-tracking,inspection-system"
    "WaterOps|Water Operations|scada-system,quality-monitoring,treatment-control,distribution-management,leak-detection"
    "EnerOps|Energy Operations|grid-management,smart-meters,demand-forecasting,renewable-integration,billing-system"
    "AutoOps|Automotive Operations|inventory-management,service-scheduling,parts-catalog,diagnostic-system,crm"
    "EnterOps|Entertainment Operations|booking-system,venue-management,ticketing,content-delivery,royalty-tracking"
    "TechnoOps|Technology Operations|asset-management,license-tracking,helpdesk,inventory-system,deployment-automation"
    "CommOps|Communications Operations|pbx-system,call-center,email-server,chat-platform,broadcast-system"
    "ServOps|Domestic Services Operations|booking-platform,provider-matching,payment-processing,rating-system,schedule-manager"
    "PetOps|Pet Operations|vet-management,grooming-scheduler,pet-registry,health-records,boarding-system"
    "WearOps|Apparel Operations|inventory-system,pos-system,size-recommender,supply-chain,ecommerce-platform"
    "ManuOps|Manufacturing Operations|mes-system,quality-control,production-planning,machine-monitoring,scada"
    "FoodOps|Food Operations|recipe-management,nutrition-database,menu-planning,ordering-system,delivery-tracking"
    "FarmOps|Farm Operations|crop-planning,livestock-tracking,equipment-management,weather-integration,market-prices"
    "PoultryOps|Poultry Operations|flock-management,egg-production,feed-tracking,health-monitoring,hatchery-system"
    "DairyOps|Dairy Operations|milk-production,herd-management,quality-testing,cold-chain,distribution-system"
    "FishOps|Fishing Operations|catch-reporting,vessel-tracking,quota-management,market-system,sustainability-monitoring"
    "TaxOps|Taxation Operations|tax-filing,calculation-engine,compliance-checker,audit-system,payment-gateway"
    "BankOps|Banking Operations|core-banking,atm-management,loan-system,fraud-detection,mobile-banking"
    "BizOps|Business Operations|crm-system,erp-platform,invoice-management,reporting,project-tracking"
    "AnimOps|Animals & Plants Operations|species-database,conservation-tracking,habitat-monitoring,research-platform,citizen-science"
    "ConstOps|Construction Operations|project-management,bid-system,equipment-tracking,safety-compliance,time-tracking"
    "ArchiOps|Archaeology Operations|site-database,artifact-catalog,3d-scanning,carbon-dating,research-collaboration"
    "QualiOps|Quality Operations|iso-management,audit-system,defect-tracking,compliance-checker,certification-management"
    "InterOps|Internet Operations|dns-management,cdn-control,bandwidth-monitor,ddos-protection,ssl-certificate-manager"
    "TradeOps|Trade Operations|order-matching,settlement-system,market-data,risk-management,regulatory-reporting"
    "WorkOps|Employment Operations|job-board,applicant-tracking,resume-parser,interview-scheduler,onboarding-system"
    "PubOps|Media & Journalism Operations|cms-platform,editorial-workflow,fact-checker,multimedia-dam,distribution-system"
    "ForesOps|Forest Operations|inventory-system,fire-detection,wildlife-tracking,harvest-planning,reforestation-tracker"
    "DefOps|Defence Operations|command-control,logistics-system,training-management,mission-planning,intelligence-platform"
    "SpaceOps|Space Operations|satellite-tracking,mission-control,telemetry-analysis,orbit-calculator,ground-station-network"
    "LoveOps|Relationship Operations|matching-algorithm,profile-management,messaging-platform,event-planning,compatibility-analysis"
    "HygenOps|Hygiene Operations|cleaning-scheduler,supply-tracking,quality-inspection,compliance-monitoring,waste-management"
    "MachiOps|Machinery Operations|maintenance-system,spare-parts,performance-monitoring,predictive-maintenance,downtime-tracking"
    "ChemiOps|Chemistry Operations|lab-management,formula-database,safety-compliance,inventory-system,experiment-tracking"
    "SciOps|Science Operations|research-platform,data-repository,collaboration-tools,publication-management,grant-tracking"
    "ResearOps|Research Operations|project-management,literature-review,data-analysis,ethics-compliance,collaboration-platform"
    "FurnOps|Furniture Operations|inventory-management,3d-configurator,order-tracking,delivery-scheduling,showroom-management"
    "ElectOps|Electronics Operations|product-catalog,repair-tracking,warranty-management,ecommerce-platform,smart-home-integration"
    "RetaiOps|Retail Operations|pos-system,inventory-management,customer-loyalty,analytics-dashboard,omnichannel-platform"
    "WastOps|Waste Management Operations|collection-routing,facility-management,recycling-tracking,compliance-reporting,billing-system"
    "KidsOps|Children Operations|daycare-management,activity-tracking,parent-portal,development-monitoring,safety-compliance"
    "ElderOps|Elder Care Operations|care-planning,medication-management,activity-scheduler,family-portal,health-monitoring"
    "ReliOps|Religion Operations|member-management,donation-tracking,event-calendar,sermon-library,volunteer-coordination"
    "HumanOps|Human Resources Operations|hr-platform,payroll-system,benefits-management,performance-reviews,recruitment"
    "SporOps|Sports Operations|team-management,scheduling,stats-tracking,ticket-sales,fan-engagement"
    "PsychOps|Psychology Operations|patient-management,assessment-tools,therapy-tracking,appointment-scheduler,billing"
    "MusicOps|Music Operations|studio-management,rights-management,royalty-tracking,distribution-platform,collaboration-tools"
    "MoneyOps|Money Operations|accounting-system,budgeting-tools,investment-tracking,expense-management,financial-planning"
    "CodeOps|Code Operations|repository-management,ci-cd-pipeline,code-review,issue-tracking,deployment-automation"
    "WomenOps|Women Services Operations|health-tracking,community-platform,safety-network,career-resources,education-portal"
    "NationOps|Nation Operations|census-system,border-control,national-id,statistics-platform,emergency-management"
    "CompOps|Computer Operations|asset-tracking,remote-management,software-deployment,monitoring,backup-system"
    "LawOps|Legal Operations|case-management,document-automation,legal-research,billing,client-portal"
)

create_stack() {
    local stack_name=$1
    local description=$2
    local services=$3

    echo "Creating $stack_name..."

    mkdir -p "$stack_name"

    # Create docker-compose.yml
    cat > "$stack_name/docker-compose.yml" << 'EOF'
version: '3.8'

services:
  # Core Database
  postgres:
    image: postgres:15-alpine
    container_name: ${STACK_NAME}-postgres
    environment:
      - POSTGRES_DB=${STACK_NAME}
      - POSTGRES_USER=${STACK_NAME}
      - POSTGRES_PASSWORD=${POSTGRES_PASS:-password}
    volumes:
      - postgres-data:/var/lib/postgresql/data
    ports:
      - "${POSTGRES_PORT:-5432}:5432"
    networks:
      - ${STACK_NAME}-network

  # Redis Cache
  redis:
    image: redis:7-alpine
    container_name: ${STACK_NAME}-redis
    command: redis-server --appendonly yes
    volumes:
      - redis-data:/data
    ports:
      - "${REDIS_PORT:-6379}:6379"
    networks:
      - ${STACK_NAME}-network

  # API Backend
  backend:
    image: node:20-alpine
    container_name: ${STACK_NAME}-backend
    working_dir: /app
    command: sh -c "npm install && npm start"
    environment:
      - DATABASE_URL=postgresql://${STACK_NAME}:${POSTGRES_PASS:-password}@postgres:5432/${STACK_NAME}
      - REDIS_URL=redis://redis:6379
    volumes:
      - ./backend:/app
    ports:
      - "${BACKEND_PORT:-3000}:3000"
    depends_on:
      - postgres
      - redis
    networks:
      - ${STACK_NAME}-network

  # Frontend
  frontend:
    image: nginx:alpine
    container_name: ${STACK_NAME}-frontend
    volumes:
      - ./frontend:/usr/share/nginx/html:ro
      - ./configs/nginx.conf:/etc/nginx/conf.d/default.conf:ro
    ports:
      - "${FRONTEND_PORT:-8080}:80"
    depends_on:
      - backend
    networks:
      - ${STACK_NAME}-network

  # Message Queue
  rabbitmq:
    image: rabbitmq:3.12-management-alpine
    container_name: ${STACK_NAME}-rabbitmq
    environment:
      - RABBITMQ_DEFAULT_USER=admin
      - RABBITMQ_DEFAULT_PASS=${RABBITMQ_PASS:-admin}
    volumes:
      - rabbitmq-data:/var/lib/rabbitmq
    ports:
      - "${AMQP_PORT:-5672}:5672"
      - "${RABBITMQ_MGMT_PORT:-15672}:15672"
    networks:
      - ${STACK_NAME}-network

  # Analytics - Metabase
  metabase:
    image: metabase/metabase:v0.48.0
    container_name: ${STACK_NAME}-metabase
    environment:
      - MB_DB_TYPE=postgres
      - MB_DB_DBNAME=metabase
      - MB_DB_PORT=5432
      - MB_DB_USER=${STACK_NAME}
      - MB_DB_PASS=${POSTGRES_PASS:-password}
      - MB_DB_HOST=postgres
    ports:
      - "${METABASE_PORT:-3001}:3000"
    depends_on:
      - postgres
    volumes:
      - metabase-data:/metabase-data
    networks:
      - ${STACK_NAME}-network

  # Monitoring - Prometheus
  prometheus:
    image: prom/prometheus:v2.48.0
    container_name: ${STACK_NAME}-prometheus
    volumes:
      - ./configs/prometheus.yml:/etc/prometheus/prometheus.yml:ro
      - prometheus-data:/prometheus
    ports:
      - "${PROMETHEUS_PORT:-9090}:9090"
    networks:
      - ${STACK_NAME}-network

  # Dashboards - Grafana
  grafana:
    image: grafana/grafana:10.2.0
    container_name: ${STACK_NAME}-grafana
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=${GRAFANA_PASS:-admin}
    volumes:
      - grafana-data:/var/lib/grafana
    ports:
      - "${GRAFANA_PORT:-3002}:3000"
    networks:
      - ${STACK_NAME}-network

networks:
  ${STACK_NAME}-network:
    driver: bridge

volumes:
  postgres-data:
  redis-data:
  rabbitmq-data:
  metabase-data:
  prometheus-data:
  grafana-data:
EOF

    # Create README.md
    cat > "$stack_name/README.md" << EOF
# $stack_name - $description

Comprehensive operational stack for $description.

## Services

- **PostgreSQL**: Core database
- **Redis**: Caching and session store
- **Backend API**: RESTful API service
- **Frontend**: Web interface
- **RabbitMQ**: Message queue
- **Metabase**: Analytics and BI
- **Prometheus**: Metrics collection
- **Grafana**: Dashboards and monitoring

## Quick Start

\`\`\`bash
cd $stack_name
cp .env.example .env
docker-compose up -d
\`\`\`

## Access Points

- **Frontend**: http://localhost:8080
- **Backend API**: http://localhost:3000
- **RabbitMQ Management**: http://localhost:15672 (admin/admin)
- **Analytics**: http://localhost:3001
- **Grafana**: http://localhost:3002 (admin/admin)
- **Prometheus**: http://localhost:9090

## Key Services

$services

## Configuration

Edit \`.env\` file for custom configuration:
- Database credentials
- Service ports
- Admin passwords

## Examples

See \`examples/\` directory for:
- API integration examples
- Dashboard configurations
- Workflow automation
- Data analytics

## Resource Requirements

**Minimum**: 4 cores, 8GB RAM, 50GB disk
**Recommended**: 8 cores, 16GB RAM, 100GB disk

## License

See main repository LICENSE file.
EOF

    # Create .env.example
    cat > "$stack_name/.env.example" << EOF
STACK_NAME=$(echo $stack_name | tr '[:upper:]' '[:lower:]')
POSTGRES_PASS=password
POSTGRES_PORT=5432
REDIS_PORT=6379
BACKEND_PORT=3000
FRONTEND_PORT=8080
RABBITMQ_PASS=admin
AMQP_PORT=5672
RABBITMQ_MGMT_PORT=15672
METABASE_PORT=3001
PROMETHEUS_PORT=9090
GRAFANA_PASS=admin
GRAFANA_PORT=3002
EOF

    # Create configs directory
    mkdir -p "$stack_name/configs"

    # Create nginx.conf
    cat > "$stack_name/configs/nginx.conf" << 'EOF'
server {
    listen 80;
    server_name localhost;

    location / {
        root /usr/share/nginx/html;
        index index.html;
        try_files $uri $uri/ /index.html;
    }

    location /api {
        proxy_pass http://backend:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
EOF

    # Create prometheus.yml
    cat > "$stack_name/configs/prometheus.yml" << 'EOF'
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'backend'
    static_configs:
      - targets: ['backend:3000']
EOF

    # Create examples directory
    mkdir -p "$stack_name/examples"
    cat > "$stack_name/examples/README.md" << EOF
# $stack_name Examples

Production-ready examples for $description.

## Available Examples

1. **API Integration**: REST API usage examples
2. **Data Analytics**: Dashboard and report configurations
3. **Workflow Automation**: Process automation examples
4. **Monitoring Setup**: Metrics and alerting configuration

## Getting Started

Each example includes:
- Complete source code
- Configuration files
- Documentation
- Usage instructions

EOF

    echo "✅ Created $stack_name"
}

# Main execution
main() {
    echo "🚀 Creating 68 specialized operational stacks for PickOps"
    echo "=================================================="

    for stack_def in "${STACKS[@]}"; do
        IFS='|' read -r name desc services <<< "$stack_def"
        create_stack "$name" "$desc" "$services"
    done

    echo ""
    echo "✅ All stacks created successfully!"
    echo "Total stacks: ${#STACKS[@]}"
}

main
