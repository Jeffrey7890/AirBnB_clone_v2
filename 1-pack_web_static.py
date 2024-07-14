#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """ generateds a .tgz archive from the web_static content """

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    achive_name = f'versions/web_static_{timestamp}.tgz'
    path = 'web_static'
    local('mkdir -p versions')
    result = local(f'tar -cvzf {achive_name} {path}')
    if result.failed:
        return (None)
    achive_size = os.path.getsize(achive_name)
    print(f"web_static packed: {achive_name} -> {achive_size}Bytes")
    return (achive_name)
