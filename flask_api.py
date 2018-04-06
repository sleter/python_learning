from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

data = {}

class GetData(Resource):
    def get(self, data_id):
        return {data_id: data[data_id]}

    def put(self, data_id):
        data[data_id] = request.form['data']
        return {data_id: data[data_id]}

api.add_resource(GetData, '/<string:data_id>')

if __name__ == '__main__':
    app.run(debug=True)