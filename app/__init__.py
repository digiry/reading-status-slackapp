from flask import Flask

from config import config


def create_app(config_name: str = 'dev') -> Flask:
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config[config_name])
    app.config.from_pyfile('config.py', silent=True)

    return app
