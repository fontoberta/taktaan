from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from application.resources import ContainerList
from application.resources import Container

def create_app():
    app = Flask(__name__)
    CORS(app)
    api = Api(app)
    api.add_resource(ContainerList, '/')
    api.add_resource(Container, '/<string:cid>/')
    return app
