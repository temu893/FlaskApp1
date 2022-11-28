from flask import Flask, request
from flask_restful import Resource, Api
from src.main.python.service.main import Item,Items
from src.main.resources.templetes.index import Index


app = Flask(__name__)
api = Api(app)

api.add_resource(Items, '/')
api.add_resource(Item,'/<int:pk>')
# api.add_resource(Index, '/h')