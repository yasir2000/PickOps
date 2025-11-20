# WebOps - Web Operations

Modern web application deployment, performance optimization, and CDN management.

## 🎯 Overview

- Web server optimization (Nginx, Apache, Caddy)
- CDN integration (Varnish, CloudFlare Workers)
- Performance monitoring (Lighthouse CI, WebPageTest)
- SSL/TLS management (Let's Encrypt, Certbot)
- Load balancing and caching
- Static site deployment

## 📦 Components

| Service | Port | Description |
|---------|------|-------------|
| Nginx | 80/443 | Web server |
| Caddy | 2019 | Modern web server |
| Varnish | 6081 | HTTP cache |
| HAProxy | 8404 | Load balancer |
| PageSpeed | 8080 | Performance optimization |
| Certbot | - | SSL certificate management |

## 🚀 Quick Start

```bash
cd WebOps
cp .env.example .env
./scripts/start.sh
```

## Access Points

- Nginx: http://localhost:80
- Caddy Admin: http://localhost:2019
- Varnish: http://localhost:6081
- HAProxy Stats: http://localhost:8404
