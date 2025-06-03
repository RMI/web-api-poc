#!/bin/sh

# Default values
API_BASE_URL=${API_BASE_URL:-http://localhost:8000}
API_KEY=${API_KEY:-abc123}

# Create config.js file with environment variable values
cat > /usr/share/nginx/html/config.js << EOF
// Configuration generated at runtime
window.APP_CONFIG = {
  API_BASE_URL: "${API_BASE_URL}",
  API_KEY: "${API_KEY}"
};
EOF

echo "Generated config.js with API_BASE_URL: ${API_BASE_URL}"


# Start nginx
exec nginx -g 'daemon off;'
