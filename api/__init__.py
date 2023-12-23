from flask import Flask
from os import makedirs


from .blueprint_controllers.authors_controller import authors_controller
from .blueprint_controllers.books_controller import books_controller
from .blueprint_controllers.auth_controller import auth_controller


def create_app() -> Flask:
    app: Flask = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(auth_controller)
    app.register_blueprint(books_controller)
    app.register_blueprint(authors_controller)

    try:
        makedirs(app.instance_path)
    except OSError:
        pass

    return app
