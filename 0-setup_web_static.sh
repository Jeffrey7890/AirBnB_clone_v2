#!/usr/bin/env bash
# setup a static web site
apt update
apt-get install -y nginx
DIRS=("/data/" "/data/web_static/" "/data/web_static/releases/" "/data/web_static/shared/" "/data/web_static/releases/test/")

for dir in "${DIRS[@]}"; do
        if [ ! -d "$dir" ]; then
                mkdir "$dir"
        fi
done

echo "<html>
        <head>
        </head>
        <body>
                Holberton School
        </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "/server_name _;/a \ \tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tindex index.html;\n\t}" /etc/nginx/sites-enabled/default
systemctl restart nginx
