#!/usr/bin/python3
from fabric.api import run, env
env.hosts = ['54.158.79.193', '52.204.95.113']


def do_deploy(archive_path):
    """ deploys my websites """
    try:
        archive_name_tgz = archive_path.split('/')[1]
        archive_name = archive_name_tgz.split('.')[0]
        put(archive_path, f'/tmp/{archive_name_tgz}')
        run(f'mkdir -p /data/web_static/releases/{archive_name}')
        run(f'tar -xzf /tmp/{archive_name_tgz} -C /data/web_static/releases/{archive_name}/')
        run(f'rm /tmp/{archive_name_tgz}')
        run(f'mv /data/web_static/releases/{archive_name}/web_static/* /data/web_static/releases/{archive_name}/')
        run(f'rm -rf /data/web_static/releases/{archive_name}/web_static')
        run('rm -f /data/web_static/current')
        run(f'ln -s /data/web_static/releases/{archive_name}/ /data/web_static/current')
        print('New version deployed!')
        return (True)
    except Exception as e:
        return (False)
