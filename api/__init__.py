from flask import Flask
from os import makedirs

from werkzeug.exceptions import BadRequestKeyError

from .json_provider import ModelJSONProvider

from .blueprint_controllers.auth_controller import auth_controller
from .blueprint_controllers.authors_controller import authors_controller
from .blueprint_controllers.books_controller import books_controller


def create_app() -> Flask:
    app: Flask = Flask(__name__, instance_relative_config=True)
    app.json = ModelJSONProvider(app)
    app.register_blueprint(auth_controller)
    app.register_blueprint(books_controller)
    app.register_blueprint(authors_controller)

    @app.errorhandler(BadRequestKeyError)
    def bad_request_key_error_handler(error: BadRequestKeyError) -> tuple[dict, int]:
        return {
            "error": {
                "message": error.name,
                "code": error.code,
            },
        }, error.code

    try:
        makedirs(app.instance_path)
    except OSError:
        pass

    return app

