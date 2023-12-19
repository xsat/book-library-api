from flask import Flask
from os.path import join
from os import makedirs
from .controllers.books_controller import books_controller
from .controllers.authors_controller import authors_controller


def create_app(test_config=None) -> Flask:
    app: Flask = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(books_controller)
    app.register_blueprint(authors_controller)
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=join(app.instance_path, 'flaskr.sqlite'),
    # )

    # if test_config is None:
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     app.config.from_mapping(test_config)

    try:
        makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
