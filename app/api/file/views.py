from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource
from .schemas import data_schema
from .service import DataFile, get_file_list
from ..users.schemas import msg_out_schema

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}

api = Namespace('Файл', authorizations=authorizations)

api.models[data_schema.name] = data_schema

@api.route('/')
class Infos(Resource):
    method_decorators = [jwt_required()]
    @api.doc(security="apikey")
    @api.marshal_list_with(data_schema)
    def get(self):
        """Список всех файлов"""
        result = get_file_list()
        return {'list_files': result}, 200

    # @api.expect(data_schema)
    @api.marshal_with(msg_out_schema)
    def post(self):
        """Добавить файл"""
        current_request = request
        date_file = DataFile(current_request)
        date_file.save_file()

        # return {'message': file.filename, 'list_files': list_files}, 200
        return {'message': 'ok'}, 200
        # payload = api.payload
        # info.append(payload)
        # return {'message': 'ok'}, 200


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