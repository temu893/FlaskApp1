from flask_restful import Resource, Api
from flask import Flask, request
from src.main.resources.templetes.sampledata import in_memory_data

class Items(Resource):
    def get(self):
        return in_memory_data
    
    def post(self):
        data = request.json
        employeId=len(in_memory_data.keys())+ 1
        in_memory_data[employeId]={'name':data['name']}
        return in_memory_data
    
#getting specific employe by primery key
class Item(Resource):
    def get(self, pk):
        return in_memory_data[pk]
    
    def put(self, pk):
        data = request.json
        in_memory_data[pk]['name']= {'name':data['name']}
        return in_memory_data
    
    def delete(self, pk):
        del in_memory_data[pk]
        return in_memory_data