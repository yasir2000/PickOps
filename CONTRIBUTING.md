# Contributing to PickOps

Thank you for your interest in contributing to PickOps! This document provides guidelines and instructions for contributing.

## 🌟 Ways to Contribute

- 🐛 Report bugs and issues
- 💡 Suggest new features or stacks
- 📝 Improve documentation
- 🔧 Submit bug fixes
- ✨ Add new operational stacks
- 🧪 Write tests
- 📊 Add monitoring dashboards

## 🚀 Getting Started

1. **Fork the repository**
2. **Clone your fork:**
   ```bash
   git clone https://github.com/YOUR-USERNAME/PickOps.git
   cd PickOps
   ```
3. **Create a branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 📋 Stack Development Guidelines

### Structure Requirements

Each new stack must include:

```
<StackName>/
├── README.md                    # Comprehensive documentation
├── docker-compose.yml           # Base configuration
├── docker-compose.dev.yml       # Development overrides
├── docker-compose.prod.yml      # Production settings
├── .env.example                 # All environment variables
├── configs/                     # Configuration files
│   └── README.md
├── scripts/
│   ├── start.sh                 # Start script
│   ├── stop.sh                  # Stop script
│   ├── health-check.sh          # Health verification
│   ├── backup.sh                # Backup automation
│   └── restore.sh               # Restore automation
├── data/.gitkeep                # Data directory
├── logs/.gitkeep                # Logs directory
└── docs/
    ├── architecture.md          # Architecture overview
    ├── configuration.md         # Configuration guide
    └── troubleshooting.md       # Common issues
```

### Code Standards

- **Shell Scripts:**
  - Use `#!/usr/bin/env bash`
  - Include error handling (`set -euo pipefail`)
  - Add comments for complex logic
  - Make scripts executable: `chmod +x`

- **Docker Compose:**
  - Use version 3.8+
  - Include health checks
  - Define resource limits
  - Use named volumes
  - Add restart policies

- **Documentation:**
  - Clear and concise
  - Include examples
  - Document all environment variables
  - Add troubleshooting section

### Testing Requirements

Before submitting:

1. **Test locally:**
   ```bash
   cd <StackName>
   docker-compose up -d
   ./scripts/health-check.sh
   ```

2. **Verify all services start:**
   ```bash
   docker-compose ps
   ```

3. **Check logs for errors:**
   ```bash
   docker-compose logs
   ```

4. **Test cleanup:**
   ```bash
   docker-compose down -v
   ```

## 🔍 Pull Request Process

1. **Update documentation** - Ensure README.md reflects changes
2. **Test thoroughly** - All services must start and function
3. **Follow conventions** - Match existing code style
4. **Commit messages:**
   ```
   feat(LLMOps): add Ollama integration
   fix(MLOps): correct MLflow tracking URI
   docs(RAGOps): update vector database configuration
   ```

5. **Create pull request:**
   - Clear title describing the change
   - Detailed description of what and why
   - Reference any related issues
   - Include screenshots/logs if relevant

## 📝 Commit Message Format

Use conventional commits:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance

**Example:**
```
feat(AgentOps): add LangGraph orchestration

- Integrate LangGraph for agent workflows
- Add example multi-agent configuration
- Include monitoring dashboards

Closes #123
```

## 🧪 Testing Checklist

- [ ] All containers start successfully
- [ ] Health checks pass
- [ ] Services are accessible on documented ports
- [ ] Logs are clean (no critical errors)
- [ ] Data persists across restarts
- [ ] Backup/restore scripts work
- [ ] Documentation is accurate
- [ ] .env.example includes all variables
- [ ] No secrets committed

## 📚 Documentation Standards

### README.md Template

Each stack README should include:

1. **Overview** - What the stack does
2. **Architecture** - Component diagram
3. **Components** - List of services
4. **Prerequisites** - Requirements
5. **Quick Start** - Setup instructions
6. **Configuration** - Environment variables
7. **Usage** - Common operations
8. **Monitoring** - Dashboard access
9. **Troubleshooting** - Common issues
10. **References** - External documentation

## 🔒 Security Guidelines

- **Never commit secrets** - Use .env files
- **Use latest images** - Pin versions
- **Enable security scanning** - Trivy, Clair
- **Follow least privilege** - Non-root users
- **Enable TLS** - For production
- **Regular updates** - Keep dependencies current

## 🤝 Code Review Process

Maintainers will review for:

- ✅ Functionality
- ✅ Code quality
- ✅ Documentation
- ✅ Security
- ✅ Performance
- ✅ Consistency

## 💬 Getting Help

- **Questions:** Open a [Discussion](https://github.com/yasir2000/PickOps/discussions)
- **Bugs:** Open an [Issue](https://github.com/yasir2000/PickOps/issues)
- **Chat:** Join our community

## 📜 License

By contributing, you agree that your contributions will be licensed under the same license as the project.

---

Thank you for making PickOps better! 🎉
