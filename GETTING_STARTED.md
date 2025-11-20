# PickOps - Getting Started Guide

Welcome to PickOps! This guide will help you quickly get started with any of the 18 operational stacks.

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Quick Start](#quick-start)
3. [Stack Selection](#stack-selection)
4. [Configuration](#configuration)
5. [Common Operations](#common-operations)
6. [Troubleshooting](#troubleshooting)

## Prerequisites

### Required Software

- **Docker Engine 24.0+**
  ```bash
  docker --version
  ```

- **Docker Compose 2.20+**
  ```bash
  docker-compose --version
  ```

### System Requirements

- **Minimum:**
  - 4 CPU cores
  - 8GB RAM
  - 50GB disk space

- **Recommended:**
  - 8+ CPU cores
  - 16GB+ RAM
  - 100GB+ SSD storage

- **For GPU-accelerated stacks (LLMOps, GenAIOps):**
  - NVIDIA GPU with 8GB+ VRAM
  - NVIDIA Docker runtime

### Install Docker

**Linux:**
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
```

**Windows:**
- Install [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop)
- Enable WSL2 backend

**macOS:**
- Install [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop)

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yasir2000/PickOps.git
cd PickOps
```

### 2. Choose Your Stack

```bash
# View all available stacks
ls -d */

# Or use the interactive setup
./scripts/setup-all.sh
```

### 3. Configure and Start

#### Option A: Using Individual Stack Scripts

```bash
# Navigate to your chosen stack
cd LLMOps

# Copy environment template
cp .env.example .env

# Edit configuration (IMPORTANT!)
nano .env  # or vim, code, etc.

# Start the stack
./scripts/start.sh

# Check health
./scripts/health-check.sh
```

#### Option B: Using Central Management Script

```bash
# Start any stack
./manage.sh llmops start

# View logs
./manage.sh llmops logs

# Stop the stack
./manage.sh llmops stop
```

## Stack Selection

### Choose by Use Case

**AI/ML Development:**
- `LLMOps` - Large Language Models
- `GenAIOps` - Generative AI (Images, Audio)
- `MLOps` - Traditional ML workflows
- `RAGOps` - Retrieval-Augmented Generation
- `AgentOps` - AI Agent orchestration

**Software Development:**
- `DevOps` - CI/CD pipelines
- `DevSecOps` - Secure development
- `LambdaOps` - Serverless functions

**Data & Analytics:**
- `DataOps` - Data pipelines
- `AIOps` - AI-driven IT operations

**Security:**
- `SecOps` - Security monitoring
- `DevSecOps` - Application security

**Infrastructure:**
- `ITOps` - Traditional IT management
- `IoTOps` - IoT device management
- `AWSOps` - AWS-specific tools
- `AzureOps` - Azure-specific tools

**Blockchain/Web3:**
- `BlockchainOps` - Blockchain nodes
- `Web3Ops` - Web3 infrastructure

**Financial:**
- `FinOps` - Cloud cost optimization

## Configuration

### Environment Variables

Each stack has an `.env.example` file. Copy it to `.env` and customize:

```bash
# Essential variables to configure:

# Database credentials
POSTGRES_PASSWORD=your_secure_password
MYSQL_ROOT_PASSWORD=your_secure_password

# Admin credentials
GRAFANA_PASSWORD=your_admin_password
ADMIN_PASSWORD=your_admin_password

# API keys (stack-specific)
HUGGINGFACE_TOKEN=your_token          # LLMOps
AWS_ACCESS_KEY_ID=your_key            # AWSOps
AZURE_SUBSCRIPTION_ID=your_sub_id     # AzureOps
```

### Resource Limits

Edit `docker-compose.yml` to adjust resource limits:

```yaml
deploy:
  resources:
    limits:
      cpus: '2.0'
      memory: 4G
    reservations:
      cpus: '1.0'
      memory: 2G
```

## Common Operations

### Start a Stack

```bash
cd <StackName>
./scripts/start.sh

# Or using manage script
./manage.sh <stackname> start
```

### Stop a Stack

```bash
./scripts/stop.sh

# Or
./manage.sh <stackname> stop
```

### View Logs

```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f <service-name>

# Using manage script
./manage.sh <stackname> logs <service-name>
```

### Check Status

```bash
./scripts/health-check.sh

# Or
docker-compose ps
```

### Update Stack

```bash
# Pull latest images
docker-compose pull

# Restart with new images
docker-compose up -d

# Or
./manage.sh <stackname> update
```

### Backup Data

```bash
./scripts/backup.sh

# Creates: backups/backup_YYYYMMDD_HHMMSS.tar.gz
```

### Restore Data

```bash
./scripts/restore.sh backups/backup_20240101_120000.tar.gz
```

### Clean Up

```bash
# Stop and remove containers
docker-compose down

# Also remove volumes (DELETES DATA!)
docker-compose down -v

# Using manage script
./manage.sh <stackname> clean
```

## Accessing Services

### Common Ports

Most stacks use these standard ports:

- **Grafana:** http://localhost:3000
- **Prometheus:** http://localhost:9090
- **Kibana:** http://localhost:5601
- **PostgreSQL:** localhost:5432
- **Redis:** localhost:6379

Check each stack's README.md for specific access points.

### Default Credentials

⚠️ **Change these immediately in production!**

- Grafana: `admin / admin`
- Harbor: `admin / Harbor12345`
- Nexus: `admin / admin123`
- SonarQube: `admin / admin`

## Troubleshooting

### Services Won't Start

```bash
# Check Docker is running
docker info

# Check logs
docker-compose logs

# Check disk space
df -h

# Check ports aren't in use
netstat -tulpn | grep <port>
```

### Out of Memory

```bash
# Check memory usage
docker stats

# Reduce number of services or resource limits
# Edit docker-compose.yml
```

### GPU Not Detected

```bash
# Check NVIDIA driver
nvidia-smi

# Check Docker GPU support
docker run --rm --gpus all nvidia/cuda:12.1.0-base-ubuntu22.04 nvidia-smi

# Restart Docker daemon
sudo systemctl restart docker
```

### Permission Denied

```bash
# Add user to docker group
sudo usermod -aG docker $USER

# Log out and back in
```

### Port Already in Use

```bash
# Find process using port
lsof -i :8080

# Kill process or change port in docker-compose.yml
```

## Advanced Usage

### Production Deployment

1. **Use production compose file:**
   ```bash
   docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
   ```

2. **Enable TLS:**
   - Configure SSL certificates in `configs/ssl/`
   - Update nginx configuration

3. **Set up monitoring:**
   - Configure Prometheus scraping
   - Set up Grafana dashboards
   - Configure alerting

4. **Implement backups:**
   - Set up automated backup cron jobs
   - Store backups off-site

### Multi-Stack Deployment

```bash
# Start multiple stacks
./manage.sh all start

# Or selectively
cd LLMOps && ./scripts/start.sh &
cd ../MLOps && ./scripts/start.sh &
cd ../DataOps && ./scripts/start.sh &
wait
```

### Custom Networking

```bash
# Create external network
docker network create pickops-shared

# Update docker-compose.yml to use external network
networks:
  default:
    external:
      name: pickops-shared
```

## Next Steps

1. **Explore the stack:** Access the web UIs and familiarize yourself with the tools
2. **Run examples:** Check `examples/` directory in each stack
3. **Customize:** Modify configurations for your use case
4. **Monitor:** Set up dashboards and alerts
5. **Scale:** Add more workers or replicas as needed

## Getting Help

- **Documentation:** Check each stack's `README.md` and `docs/` folder
- **Issues:** [GitHub Issues](https://github.com/yasir2000/PickOps/issues)
- **Discussions:** [GitHub Discussions](https://github.com/yasir2000/PickOps/discussions)
- **Logs:** Always check `docker-compose logs` first

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines on:
- Adding new stacks
- Improving existing ones
- Reporting bugs
- Suggesting features

---

**Happy deploying! 🚀**
