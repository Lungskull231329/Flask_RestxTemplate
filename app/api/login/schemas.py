from flask_restx import Model, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from ...models.models import File

# note_schema = Model('Примечание', {
#     'id': fields.String(required=True, description='Идентификатор примечания'),
#     'note': fields.String(required=True, description='Текст примечания'),
# })

login_in_schema = Model('LoginInSchema', {
    'login': fields.String(required=True, description='Логин'),
    'password': fields.String(required=True, description='Пароль')
})

login_out_schema = Model('LoginOutSchema', {
    'message': fields.String(required=True, description='Сообщение'),
    'token': fields.String(required=True, description='Сообщение')
})


class FileOutSchema(SQLAlchemyAutoSchema):
    """Автосхема пользователя"""
    class Meta:
        """Meta."""
        model = File
        include_fk = True