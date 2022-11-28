from flask import Flask, request
from flask_restful import Resource, Api
from src.main.python.service.main import Item,Items

app = Flask(__name__)
api = Api(app)

api.add_resource(Items, '/')
api.add_resource(Item,'/<int:pk>')