from flask_restful import Resource

from .docker_client import container_list
from .docker_client import container_move

from .decorators import is_authenticated

class AuthenticatedResource(Resource):
    method_decorators = [is_authenticated]

class ContainerList(AuthenticatedResource):
    @staticmethod
    def get():
        return container_list()

class Container(AuthenticatedResource):
    @staticmethod
    def post(cid):
        return container_move(cid)
