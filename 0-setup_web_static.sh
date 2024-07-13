#!/usr/bin/env bash
# setup a static web site
apt-get -y update
apt-get -y upgrade
apt-get -y install nginx
mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "This is a test" | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data/
sed -i "/server_name _;/a \ \tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tindex index.html;\n\t}" /etc/nginx/sites-enabled/default
service nginx start
