from flask_restx import Model, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from ...models.models import File


data_schema = Model('File', {
    'list_files': fields.List(fields.Raw, required=True, description='Имя информации'),
})

class FileOutSchema(SQLAlchemyAutoSchema):
    """Автосхема пользователя"""
    class Meta:
        """Meta."""
        model = File
        include_fk = True