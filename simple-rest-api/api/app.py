from flask import Flask
from .simple.resources import get_simple_resources
from .config import Config 

APP_NAME = 'simpleapi'
CONFIG_NAME = 'production'

def register_blueprints(app):
    app.register_blueprint(get_simple_resources().blueprint)

def register_error_handlers(app):
    pass

def create_app(name=APP_NAME, config=CONFIG_NAME):
    """
    A factory function used for creating apps

    Args:
        name (string): application name
        config (string): configuration name

    Returns:
        Flask app
    """
    app = Flask(name) 
    app.config.from_object(Config.factory(config))
    register_error_handlers(app)
    register_blueprints(app)

    return app