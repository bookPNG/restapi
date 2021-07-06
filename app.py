from flask import Flask, request
from flask_restful import Resource, Api

appflask = Flask(__name__)
api = Api(appflask)

class Helloworld(Resource):
    def get(self):
        return "Hello World :)"

class Sum(Resource):
    def post(self):
        data = request.get_json()
        a = data['a']
        b = data['b']
        sum = a + b
        return sum

api.add_resource(Helloworld, '/hello') #http://127.0.0.1:5000/
api.add_resource(Sum, '/sum')
