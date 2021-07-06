from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

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

app.run(port = 5001, debug = True)