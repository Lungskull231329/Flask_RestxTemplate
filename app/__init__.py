"""App."""
from .app import get_app
from flask_jwt_extended import JWTManager
from flask_restx import Api

from .api.file import api as ns_file
from .api.users import api as ns_users
from .api.login import api as ns_login

from .tools.common import BlueprintContainer

from .web.views import page


api = Api(
    title='Моя программа',
    version='1.0',
    description='Описание',
    doc='/apidocs/',
    # validate=True
    # All API metadatas
)

api.add_namespace(ns_file, path='/file')
api.add_namespace(ns_users, path='/users')
api.add_namespace(ns_login, path='/login')

blueprints = []
blueprints.append(BlueprintContainer(page, '/'))


jwt = JWTManager()