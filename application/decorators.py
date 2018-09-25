import os
from functools import wraps
from flask import request
import requests

from .settings import settings

def is_authenticated(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if settings[os.environ['ENVIRONMENT']] \
        ['boon_token_validation_url'] != 'standalone':
            token = request.headers['Token']
            headers = {'Authorization': 'Bearer ' + token}
            resp = requests.get(
                settings[os.environ['ENVIRONMENT']] \
                ['boon_token_validation_url'],
                headers=headers)
            if resp.status_code != 200:
                return {'Error' : 'Token invalid.'}, 401
        return f(*args, **kwargs)
    return decorated_function
