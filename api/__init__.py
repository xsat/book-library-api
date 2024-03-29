from flask import Flask
from os import makedirs

from .exeptions import ApiError
from .json import ModelJSONProvider
from .blueprint_controllers.auth_controller import auth_controller
from .blueprint_controllers.authors_controller import authors_controller
from .blueprint_controllers.books_controller import books_controller
from .blueprint_controllers.user_controller import user_controller


def create_app() -> Flask:
    app: Flask = Flask(__name__, instance_relative_config=True)
    app.json = ModelJSONProvider(app)
    app.register_blueprint(auth_controller)
    app.register_blueprint(authors_controller)
    app.register_blueprint(books_controller)
    app.register_blueprint(user_controller)

    @app.errorhandler(ApiError)
    def api_error_handler(error: ApiError) -> tuple[dict, int]:
        return {"error": error}, error.code

    try:
        makedirs(app.instance_path)
    except OSError:
        pass

    return app

