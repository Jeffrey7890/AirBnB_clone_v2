#!/usr/bin/python3
from fabric.api import run, env
env.hosts = ['54.158.79.193', '52.204.95.113']


def do_deploy(archive_path):
    """ deploys my websites """
    try:
        archive_name_tgz = archive_path.split('/')[1]
        archive_name = archive_name_tgz.split('.')[0]
        path_to_archive_name = f"/data/web_static/releases/{archive_name}"
        put(archive_path, f'/tmp/{archive_name_tgz}')
        run(f'mkdir -p {path_to_archive_name')
        run(f'tar -xzf /tmp/{archive_name_tgz} -C {path_to_archive_name}')
        run(f'rm /tmp/{archive_name_tgz}')
        run(f'mv {path_to_archive_name}/web_static/* {path_to_archive_name}')
        run(f'rm -rf {path_to_archive_name}/web_static')
        run('rm -f /data/web_static/current')
        run(f'ln -s {path_to_archive_name}/ /data/web_static/current')
        print('New version deployed!')
        return (True)
    except Exception as e:
        return (False)
