# Security Policy

## Supported Versions

We release patches for security vulnerabilities in the following versions:

| Version | Supported          |
| ------- | ------------------ |
| Latest  | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability within PickOps, please send an email to security@pickops.dev. All security vulnerabilities will be promptly addressed.

**Please do not report security vulnerabilities through public GitHub issues.**

### What to Include

- Type of issue (e.g., buffer overflow, SQL injection, cross-site scripting)
- Full paths of source file(s) related to the issue
- Location of the affected source code (tag/branch/commit)
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue

## Security Best Practices

### Credentials

- **Never commit secrets** to version control
- Use strong, unique passwords for all services
- Rotate credentials regularly
- Use `.env` files for sensitive configuration

### Docker Security

- Run containers as non-root users where possible
- Keep base images updated
- Scan images for vulnerabilities using Trivy or similar tools
- Limit container capabilities and resources

### Network Security

- Use TLS/SSL in production environments
- Implement network segmentation
- Configure firewalls appropriately
- Use VPNs for remote access

### Production Deployments

1. **Change all default passwords immediately**
2. **Enable authentication** on all services
3. **Configure TLS/SSL** for external access
4. **Implement backup strategies**
5. **Monitor logs** for suspicious activity
6. **Keep systems updated**

### Stack-Specific Security

#### LLMOps / GenAIOps
- Validate and sanitize all user inputs
- Implement rate limiting
- Monitor for prompt injection attacks

#### SecOps / DevSecOps
- Follow principle of least privilege
- Implement multi-factor authentication
- Regular security audits

#### BlockchainOps / Web3Ops
- Secure private keys using HSM or secure enclaves
- Implement multi-signature wallets
- Regular smart contract audits

#### Cloud Ops (AWS/Azure)
- Use IAM roles and policies correctly
- Enable CloudTrail/Activity logs
- Implement resource tagging

## Security Scanning

We recommend scanning your deployments regularly:

```bash
# Scan Docker images
trivy image <image-name>

# Scan infrastructure
terrascan scan

# Scan for secrets
gitleaks detect --source .
```

## Vulnerability Disclosure Timeline

- **Day 0:** Vulnerability reported
- **Day 1:** Acknowledgment sent to reporter
- **Day 7:** Initial assessment and priority assignment
- **Day 30:** Fix developed and tested
- **Day 45:** Security patch released
- **Day 60:** Public disclosure (if applicable)

## Contact

For security-related questions: security@pickops.dev

For general issues: https://github.com/yasir2000/PickOps/issues
