#!/bin/bash
# Nginx Performance Optimization Example
# Demonstrates: Configuration tuning, caching, compression, SSL optimization

echo "🚀 Nginx Performance Optimization"
echo "======================================"

# Generate optimized nginx.conf
cat > nginx_optimized.conf << 'EOF'
user nginx;
worker_processes auto;
worker_rlimit_nofile 100000;
error_log /var/log/nginx/error.log warn;
pid /var/run/nginx.pid;

events {
    worker_connections 4096;
    use epoll;
    multi_accept on;
}

http {
    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    # Logging
    log_format main '$remote_addr - $remote_user [$time_local] "$request" '
                    '$status $body_bytes_sent "$http_referer" '
                    '"$http_user_agent" "$http_x_forwarded_for" '
                    'rt=$request_time uct="$upstream_connect_time" '
                    'uht="$upstream_header_time" urt="$upstream_response_time"';

    access_log /var/log/nginx/access.log main;

    # Performance optimizations
    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    keepalive_requests 100;
    reset_timedout_connection on;

    # Buffer sizes
    client_body_buffer_size 128k;
    client_max_body_size 10m;
    client_header_buffer_size 1k;
    large_client_header_buffers 4 8k;
    output_buffers 1 32k;
    postpone_output 1460;

    # Timeouts
    client_header_timeout 30s;
    client_body_timeout 30s;
    send_timeout 30s;

    # Gzip compression
    gzip on;
    gzip_vary on;
    gzip_proxied any;
    gzip_comp_level 6;
    gzip_types
        text/plain
        text/css
        text/xml
        text/javascript
        application/json
        application/javascript
        application/xml+rss
        application/rss+xml
        font/truetype
        font/opentype
        application/vnd.ms-fontobject
        image/svg+xml;
    gzip_disable "msie6";

    # Caching
    open_file_cache max=10000 inactive=30s;
    open_file_cache_valid 60s;
    open_file_cache_min_uses 2;
    open_file_cache_errors on;

    # Security headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header Referrer-Policy "no-referrer-when-downgrade" always;

    # SSL optimization
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers 'ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256';
    ssl_prefer_server_ciphers off;
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 10m;
    ssl_session_tickets off;
    ssl_stapling on;
    ssl_stapling_verify on;

    # Rate limiting
    limit_req_zone $binary_remote_addr zone=general:10m rate=10r/s;
    limit_req_zone $binary_remote_addr zone=api:10m rate=30r/s;
    limit_conn_zone $binary_remote_addr zone=addr:10m;

    # Upstream configuration
    upstream backend {
        least_conn;
        server backend1:8080 max_fails=3 fail_timeout=30s;
        server backend2:8080 max_fails=3 fail_timeout=30s;
        keepalive 32;
    }

    # Cache configuration
    proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=my_cache:10m
                     max_size=1g inactive=60m use_temp_path=off;

    server {
        listen 80;
        listen [::]:80;
        server_name example.com www.example.com;

        # Redirect to HTTPS
        return 301 https://$server_name$request_uri;
    }

    server {
        listen 443 ssl http2;
        listen [::]:443 ssl http2;
        server_name example.com www.example.com;

        # SSL certificates
        ssl_certificate /etc/nginx/ssl/cert.pem;
        ssl_certificate_key /etc/nginx/ssl/key.pem;

        # Root and index
        root /usr/share/nginx/html;
        index index.html index.htm;

        # Rate limiting
        limit_req zone=general burst=20 nodelay;
        limit_conn addr 10;

        # Static files with caching
        location ~* \.(jpg|jpeg|png|gif|ico|css|js|svg|woff|woff2|ttf|eot)$ {
            expires 1y;
            add_header Cache-Control "public, immutable";
            access_log off;
        }

        # API endpoints with caching
        location /api/ {
            limit_req zone=api burst=50 nodelay;

            proxy_pass http://backend;
            proxy_http_version 1.1;
            proxy_set_header Connection "";
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;

            # Caching
            proxy_cache my_cache;
            proxy_cache_valid 200 10m;
            proxy_cache_valid 404 1m;
            proxy_cache_use_stale error timeout updating http_500 http_502 http_503 http_504;
            proxy_cache_background_update on;
            proxy_cache_lock on;
            add_header X-Cache-Status $upstream_cache_status;
        }

        # Health check endpoint
        location /health {
            access_log off;
            return 200 "healthy\n";
            add_header Content-Type text/plain;
        }

        # Status page (restrict to localhost)
        location /nginx_status {
            stub_status on;
            access_log off;
            allow 127.0.0.1;
            deny all;
        }
    }
}
EOF

echo "✅ Generated optimized nginx.conf"

# Performance testing script
cat > performance_test.sh << 'EOF'
#!/bin/bash
echo "📊 Running performance tests..."

# Install dependencies
command -v ab >/dev/null 2>&1 || {
    echo "Installing Apache Bench..."
    apt-get update && apt-get install -y apache2-utils
}

# Test 1: Simple load test
echo -e "\n🧪 Test 1: Basic load test (1000 requests, concurrency 10)"
ab -n 1000 -c 10 -g test1.tsv http://localhost/

# Test 2: High concurrency
echo -e "\n🧪 Test 2: High concurrency (5000 requests, concurrency 100)"
ab -n 5000 -c 100 -g test2.tsv http://localhost/

# Test 3: Keep-alive enabled
echo -e "\n🧪 Test 3: With keep-alive (1000 requests, concurrency 50)"
ab -n 1000 -c 50 -k -g test3.tsv http://localhost/

# Test 4: Static file performance
echo -e "\n🧪 Test 4: Static file delivery"
ab -n 2000 -c 50 -g test4.tsv http://localhost/static/test.jpg

echo -e "\n✅ Performance tests complete!"
echo "Results saved in test*.tsv files"
EOF

chmod +x performance_test.sh

# Monitoring script
cat > monitor_nginx.sh << 'EOF'
#!/bin/bash
echo "📈 Nginx Performance Monitor"
echo "=============================="

while true; do
    clear
    echo "Time: $(date)"
    echo ""

    # Active connections
    echo "🔌 Active Connections:"
    curl -s http://localhost/nginx_status | grep "Active"

    # Connection status
    echo -e "\n📊 Connection Status:"
    curl -s http://localhost/nginx_status | grep -E "Reading|Writing|Waiting"

    # Requests
    echo -e "\n📈 Total Requests:"
    curl -s http://localhost/nginx_status | grep "requests"

    # Process stats
    echo -e "\n💻 Process Stats:"
    ps aux | grep nginx | grep -v grep

    # CPU and Memory
    echo -e "\n🖥️  Resource Usage:"
    top -b -n 1 | grep nginx | head -5

    sleep 5
done
EOF

chmod +x monitor_nginx.sh

# SSL optimization check
cat > check_ssl.sh << 'EOF'
#!/bin/bash
echo "🔒 SSL Configuration Check"
echo "============================"

DOMAIN="example.com"

echo -e "\n1. Testing SSL protocols..."
for proto in ssl2 ssl3 tls1 tls1_1 tls1_2 tls1_3; do
    result=$(openssl s_client -connect $DOMAIN:443 -$proto < /dev/null 2>&1 | grep "Protocol")
    echo "  $proto: $result"
done

echo -e "\n2. Testing cipher suites..."
nmap --script ssl-enum-ciphers -p 443 $DOMAIN

echo -e "\n3. SSL Labs grade (mock)..."
echo "  Overall Rating: A+"
echo "  Certificate: Valid"
echo "  Protocol Support: TLS 1.2, TLS 1.3"
echo "  Key Exchange: Strong"
echo "  Cipher Strength: Strong"

echo -e "\n✅ SSL check complete!"
EOF

chmod +x check_ssl.sh

echo ""
echo "======================================"
echo "✨ Optimization files generated!"
echo "======================================"
echo ""
echo "📁 Files created:"
echo "  - nginx_optimized.conf"
echo "  - performance_test.sh"
echo "  - monitor_nginx.sh"
echo "  - check_ssl.sh"
echo ""
echo "🚀 Next steps:"
echo "  1. Review nginx_optimized.conf"
echo "  2. Copy to /etc/nginx/nginx.conf"
echo "  3. Test: nginx -t"
echo "  4. Reload: nginx -s reload"
echo "  5. Run performance_test.sh"
echo "  6. Monitor with monitor_nginx.sh"
echo ""
