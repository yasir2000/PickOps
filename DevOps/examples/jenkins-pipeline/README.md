# Jenkins Pipeline Example

Complete CI/CD pipeline demonstrating:
- Source checkout
- Build & test
- Code quality analysis (SonarQube)
- Docker build & security scan
- Registry push (Harbor)
- Automated deployment

## Setup

### 1. Start DevOps Stack

```bash
cd ../../
docker-compose up -d
```

### 2. Configure Jenkins

Access Jenkins at http://localhost:8080

```bash
# Get initial admin password
docker-compose exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

Install required plugins:
- Docker Pipeline
- SonarQube Scanner
- Git
- Pipeline
- Credentials

### 3. Configure Credentials

**Jenkins → Manage Jenkins → Credentials**

Add:
1. **harbor-credentials**: Username/Password for Harbor
2. **sonarqube-token**: Secret text from SonarQube

### 4. Configure SonarQube

Access SonarQube at http://localhost:9000 (admin/admin)

1. Create project: `myapp`
2. Generate token
3. Add token to Jenkins credentials

### 5. Create Pipeline Job

1. **New Item** → Pipeline
2. **Pipeline** section:
   - Definition: Pipeline script from SCM
   - SCM: Git
   - Repository URL: your-repo-url
   - Script Path: `Jenkinsfile`

## Sample Application Structure

```
myapp/
├── Dockerfile
├── Jenkinsfile
├── package.json
├── src/
│   └── index.js
├── test/
│   └── app.test.js
└── sonar-project.properties
```

### Dockerfile

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
EXPOSE 3000
CMD ["node", "src/index.js"]
```

### sonar-project.properties

```properties
sonar.projectKey=myapp
sonar.projectName=My Application
sonar.projectVersion=1.0
sonar.sources=src
sonar.tests=test
sonar.javascript.lcov.reportPaths=coverage/lcov.info
```

## Run the Pipeline

1. **Trigger Build**: Click "Build Now"
2. **Monitor**: Watch stage progression
3. **View Logs**: Click on stage for details
4. **Approve Production**: Manual approval required

## Pipeline Stages Explained

### 1. Checkout
Clones repository from Git

### 2. Build
Installs dependencies and builds application

### 3. Test
Runs unit tests with coverage reporting

### 4. SonarQube Analysis
Scans code for:
- Code smells
- Bugs
- Security vulnerabilities
- Technical debt

### 5. Quality Gate
Blocks pipeline if quality thresholds not met

### 6. Docker Build
Creates container image with version tag

### 7. Security Scan
Scans image for CVEs using Trivy

### 8. Push to Registry
Pushes to Harbor private registry

### 9. Deploy to Staging
Automatic deployment for testing

### 10. Integration Tests
Validates deployed application

### 11. Deploy to Production
Manual approval required (main branch only)

## View Results

### Jenkins Dashboard
- Build history
- Test results
- Coverage reports

### Harbor Registry
http://localhost:8081
- View pushed images
- Check vulnerability scans
- Manage image retention

### SonarQube
http://localhost:9000
- Code quality metrics
- Security hotspots
- Technical debt

### Grafana
http://localhost:3000
- Pipeline metrics
- Build duration trends
- Success/failure rates

## Troubleshooting

**Docker permission denied:**
```bash
# Add jenkins user to docker group
docker-compose exec jenkins usermod -aG docker jenkins
docker-compose restart jenkins
```

**SonarQube not connecting:**
```bash
# Check SonarQube is running
docker-compose ps sonarqube
# Verify URL in Jenkins configuration
```

**Harbor authentication failed:**
```bash
# Test login manually
docker login localhost:8081
```

## Next Steps

- Add [vault-secrets](../vault-secrets/) for secure credentials
- Implement [gitlab-ci-cd](../gitlab-ci-cd/) alternative
- Set up notifications and reporting
