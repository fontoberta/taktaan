import os
import docker
from requests import exceptions
from .settings import settings

def container_list():
    client = docker.DockerClient(
        base_url=settings[os.environ['ENVIRONMENT']]['docker_unix_url'])
    try:
        clist = client.containers.list(all=True)
    except exceptions.ConnectionError: # pragma: no cover
        return {'Error' : 'No Docker information found.'}, 404

    rvalue = {}
    for l in clist:
        rvalue.update({l.name: {'id': l.short_id, 'status': l.status}})
    return rvalue

def container_move(cid):
    client = docker.DockerClient(
        base_url=settings[os.environ['ENVIRONMENT']]['docker_unix_url'])
    try:
        c = client.containers.get(cid)
    except exceptions.ConnectionError: # pragma: no cover
        return {'Error' : 'No Docker information found.'}, 404

    if c.status == 'exited':
        c.start()
        return {'id' : cid, 'status' : 'running'}
    c.stop()
    return {'id' : cid, 'status' : 'exited'}
