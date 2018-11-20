from flask import Blueprint, request
from flask_restful import Api, Resource
from .logic import hello 

class Simple(Resource):
    def get(self):
        print('calling service!')
        return hello()

def get_simple_resources():
    blueprint = Blueprint('', __name__)
    api = Api(blueprint)
    endpoints = [
        (Simple, '/simple')
    ]
    [api.add_resource(*ep) for ep in endpoints]
    return api 