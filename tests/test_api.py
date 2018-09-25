# pylint: disable=redefined-outer-name
import os
import json
import pytest
import requests
from application import create_app
from application.settings import settings

@pytest.fixture
def client():
    if settings[os.environ['ENVIRONMENT']]['test_token'] == '':
        headers = {'Content-Type':  'application/x-www-form-urlencoded'}
        data = dict(
            username=settings[os.environ['ENVIRONMENT']]['test_username'],
            password=settings[os.environ['ENVIRONMENT']]['test_password'],
            grant_type='password',
            client_id=settings[os.environ['ENVIRONMENT']]['test_client_id']
        )
        resp = requests.post(
            settings[os.environ['ENVIRONMENT']]['boon_get_token_url'],
            headers=headers,
            data=data
            )
        settings[os.environ['ENVIRONMENT']] \
            ['test_token'] = resp.json()['access_token']

    app = create_app()
    app.config['TESTING'] = True
    testclient = app.test_client()

    yield testclient

def test_authentication(client):
    headers = {'Token' : ''}
    resp = client.get('/', headers=headers)
    assert '401' in resp.status
    headers = {'Token' : settings[os.environ['ENVIRONMENT']]['test_token']}
    resp = client.get('/', headers=headers)
    assert '200' in resp.status

def test_post_container(client):
    headers = {'Token' : settings[os.environ['ENVIRONMENT']]['test_token']}
    rv = client.get('/', headers=headers)
    for container in json.loads(rv.data):
        rc = client.post('/' + container + '/', headers=headers)
        assert '200 OK' in rc.status
        # Return container to original state
        rc = client.post('/' + container + '/', headers=headers)
        assert '200 OK' in rc.status
        break
