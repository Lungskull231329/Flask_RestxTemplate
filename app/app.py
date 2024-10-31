import os
from flask import Flask


def internal_server_error(e):
    print(e)
    return 'Ошибка сервера {}'.format(str(e)[:500] + '...'), 500

def get_app(config) -> Flask:
    """Get flask application."""

    app = Flask(__name__)
    app.config.from_object(config)

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    UPLOAD_FOLDER = BASE_DIR + '\\uploads'

    # print(UPLOAD_FOLDER)

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    app.config['BASE_DIR'] = BASE_DIR
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!


    # Register the blueprint with the Flask app
    from . import blueprints
    for blueprint in blueprints:
        app.register_blueprint(blueprint.obj, url_prefix=blueprint.url_prefix)
    app.register_error_handler(Exception, internal_server_error)

    from . import api, jwt
    jwt.init_app(app)
    api.init_app(app)


    # ///// Раскомментировать для создания таблиц, не забыть закомментировать /////

    # from sqlalchemy import create_engine
    # from .models import Base
    # from .models.models import Data, User
    # Base.metadata.create_all(create_engine(app.config.get('DB_URI', '')))



    return app
