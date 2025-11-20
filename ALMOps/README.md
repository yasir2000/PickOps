# ALMOps - Application Lifecycle Management Operations

Complete Application Lifecycle Management (ALM) stack for managing software development from requirements to deployment.

## Stack Components

### Project Management & Tracking
- **Jira** (port 8080) - Issue tracking and agile project management
- **Taiga** (port 9000) - Agile project management with kanban/scrum boards
- **Redmine** (port 3000) - Flexible project management and issue tracking

### Documentation & Collaboration
- **Confluence** (port 8090) - Team collaboration and documentation

### Source Control & CI/CD
- **GitLab** (port 8929) - Complete DevOps platform with Git, CI/CD, and registry
- **Jenkins** (port 8085) - Extensible automation server

### Artifact Management
- **Nexus Repository** (port 8081) - Universal artifact repository manager
  - Maven/Gradle repositories
  - Docker registry (port 8082)
  - npm, PyPI, NuGet support

### Monitoring & Metrics
- **Prometheus** (port 9090) - Metrics collection and alerting
- **Grafana** (port 3001) - Metrics visualization and dashboards

## Quick Start

```bash
# Start the entire ALM stack
docker-compose up -d

# Start specific services
docker-compose up -d jira gitlab nexus

# View logs
docker-compose logs -f

# Stop all services
docker-compose down
```

## Service Access

| Service | URL | Default Credentials |
|---------|-----|---------------------|
| Jira | http://localhost:8080 | Setup wizard |
| Confluence | http://localhost:8090 | Setup wizard |
| GitLab | http://localhost:8929 | root / changeme123 |
| Nexus | http://localhost:8081 | admin / check logs |
| Taiga | http://localhost:9000 | Setup wizard |
| Jenkins | http://localhost:8085/jenkins | admin / check logs |
| Redmine | http://localhost:3000 | admin / admin |
| Prometheus | http://localhost:9090 | - |
| Grafana | http://localhost:3001 | admin / admin |

## Use Cases

### Complete ALM Workflow
1. **Requirements**: Capture in Jira/Taiga
2. **Documentation**: Write specs in Confluence
3. **Development**: Code in GitLab repos
4. **Build**: Automate with Jenkins CI/CD
5. **Artifacts**: Store in Nexus Repository
6. **Testing**: Track test cases in Jira
7. **Release**: Deploy via Jenkins pipelines
8. **Monitor**: Track metrics in Grafana

### Agile Teams
- Sprint planning in Jira/Taiga
- User story tracking
- Burndown charts
- Retrospectives in Confluence

### Enterprise ALM
- Multi-project management
- Cross-team collaboration
- Compliance tracking
- Release management

## Configuration

### Jira Setup
```bash
# Access setup wizard at http://localhost:8080
# Choose evaluation license or enter license key
# Configure database and admin user
```

### GitLab Integration
```bash
# Get initial root password
docker exec almops-gitlab grep 'Password:' /etc/gitlab/initial_root_password

# Configure GitLab CI/CD with Nexus
# Settings > CI/CD > Variables
MAVEN_REPO_URL=http://nexus:8081/repository/maven-releases/
```

### Nexus Docker Registry
```bash
# Login to Nexus Docker registry
docker login localhost:8082

# Tag and push images
docker tag myimage:latest localhost:8082/myimage:latest
docker push localhost:8082/myimage:latest
```

### Jenkins Pipeline Integration
```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }
        stage('Deploy to Nexus') {
            steps {
                sh 'mvn deploy'
            }
        }
    }
}
```

## Resource Requirements

### Minimum
- CPU: 8 cores
- RAM: 16 GB
- Disk: 50 GB

### Recommended
- CPU: 12+ cores
- RAM: 32 GB
- Disk: 100+ GB SSD

## Environment Variables

See `.env.example` for all configuration options.

## Integration Patterns

### Jira + GitLab
```bash
# Link commits to Jira issues
git commit -m "PROJ-123: Implement feature"
# Automatically updates Jira ticket
```

### Jenkins + Nexus
```xml
<!-- pom.xml -->
<distributionManagement>
    <repository>
        <id>nexus</id>
        <url>http://nexus:8081/repository/maven-releases/</url>
    </repository>
</distributionManagement>
```

### Monitoring Everything
```yaml
# prometheus.yml
scrape_configs:
  - job_name: 'jenkins'
    static_configs:
      - targets: ['jenkins:8080']
  - job_name: 'gitlab'
    static_configs:
      - targets: ['gitlab:80']
```

## Backup Strategy

```bash
# Backup all volumes
docker-compose down
docker run --rm -v almops_jira_data:/data -v $(pwd)/backups:/backup alpine tar czf /backup/jira.tar.gz /data

# Restore
docker run --rm -v almops_jira_data:/data -v $(pwd)/backups:/backup alpine tar xzf /backup/jira.tar.gz -C /
```

## Troubleshooting

### Jira/Confluence Won't Start
```bash
# Increase memory limits in .env
JIRA_MAX_MEMORY=6g
CONFLUENCE_MAX_MEMORY=6g
```

### GitLab 502 Error
```bash
# Wait for initialization (can take 5-10 minutes)
docker-compose logs -f gitlab

# Check status
docker exec almops-gitlab gitlab-ctl status
```

### Nexus Admin Password
```bash
# Get initial admin password
docker exec almops-nexus cat /nexus-data/admin.password
```

## Best Practices

1. **Use a reverse proxy** (Nginx/Traefik) for production
2. **Configure SSL/TLS** for all services
3. **Set up regular backups** of all data volumes
4. **Monitor resource usage** with Prometheus/Grafana
5. **Implement SSO** (LDAP/SAML) for enterprise deployments
6. **Configure email** notifications for all tools
7. **Set up disaster recovery** procedures

## License

Components have different licenses:
- Jira/Confluence: Commercial (evaluation/licensed)
- GitLab CE: MIT License
- Nexus: EPL 1.0
- Taiga: AGPL 3.0
- Jenkins: MIT License
- Redmine: GPL v2

Check individual project licenses before production use.
