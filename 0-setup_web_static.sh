#!/usr/bin/env bash
# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    apt-get update -y
    apt-get install -y nginx
fi

# Create necessary folders if they don't already exist
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
chown -R ubuntu:ubuntu /data/

# Create fake HTML file for testing
echo "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    <p>Nginx server test</p>
  </body>
</html>" | tee /data/web_static/releases/test/index.html

# Create symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Configure Nginx to serve content
sed -i '/server_name _;/a location /hbnb_static {\n\talias /data/web_static/current/;\n}\n' /etc/nginx/sites-enabled/default
service nginx restart
