from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from flask_restx import Namespace, Resource
from flask_restx.reqparse import RequestParser

from .schemas import login_in_schema, login_out_schema


authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}

api = Namespace('Аутентификация', authorizations=authorizations)

api.models[login_in_schema.name] = login_in_schema
api.models[login_out_schema.name] = login_out_schema


parser_token = RequestParser()
parser_token.add_argument('token', type=str)

@api.route('/')
class Logins(Resource):
    @jwt_required(optional=True)
    def get(self):
        """Проверить токен"""
        args = parser_token.parse_args()
        current_user = get_jwt_identity()
        if current_user:
            return {'result': True}, 200
        return {'result': False}, 200

    # @api.expect(course_input_model)
    @api.expect(login_in_schema)
    @api.marshal_with(login_out_schema)
    def post(self):
        """Получить токен"""
        payload = api.payload
        if payload.get('login') != "test" or payload.get('password') != "test":
            return {'message': "Bad username or password", 'token': None}, 401
        access_token = create_access_token(identity=payload.get('login'))
        return {'message': "Ok", 'token': str(access_token)}, 200

#
# @api.route('/<id>')
# @api.param('id', 'идентификатор информации')
# @api.response(404, 'Информация не найдена')
# class Info(Resource):
#     @api.doc('информация')
#     @api.marshal_with(data_schema)
#     def get(self, id):
#         '''Запрос одной информации'''
#         for i in info:
#             if i['id'] == id:
#                 return i
#         api.abort(500)