from flask import Flask, request
from flask_restful import Resource, Api, reqparse, fields, marshal
#from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
api = Api(app)
#auth = HTTPBasicAuth()

# @auth.get_password
# def get_password(username):
#     if username == 'miguel':
#         return 'python'
#     return None


# @auth.error_handler
# def unauthorized():
#     # return 403 instead of 401 to prevent browsers from displaying the default
#     # auth dialog
#     return make_response(jsonify({'message': 'Unauthorized access'}), 403)

data_s = [
    {
        'id': 1,
        'question': u'Hum?',
        'answer': u'K m9',
        'done': False
    }
]

data_fields = {
    'id': fields.Integer,
    'question': fields.String,
    'answer': fields.String,
    'done': fields.Boolean,
    'uri': fields.Url('data')
}


class MainPage(Resource):
    def get(self):
        return {'hello': 'world'}

class ShowJSON(Resource):
    #decorators = [auth.login_required]
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id', type = int, default = 0, location = 'json')
        self.reqparse.add_argument('question', type = str, required = True, help = 'No task title provided', location = 'json')
        self.reqparse.add_argument('answer', type = str, default = "", location = 'json')
        super(ShowJSON, self).__init__()
    def get(self):
        return {'data_s': [marshal(data_s, data_fields) for task in data_s]}
    def post(self):
        args = self.reqparse.parse_args()
        data = {
            'id': data_s[-1]['id'] + 1,
            'question': args['question'],
            'answer': args['answer'],
            'done': False
        }
        data_s.append(data)
        return {'task': marshal(data, data_fields)}, 201

class GetData(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id', type=int, location='json')
        self.reqparse.add_argument('question', type = str, location = 'json')
        self.reqparse.add_argument('answer', type = str, location = 'json')
        self.reqparse.add_argument('done', type = bool, location = 'json')
        super(GetData, self).__init__()


api.add_resource(MainPage, '/')
api.add_resource(ShowJSON, '/json', endpoint='json')
api.add_resource(GetData, '/<string:data_id>')


if __name__ == '__main__':
    app.run(debug=True)