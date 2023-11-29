from flask import Flask
from .views.user import user_blueprint


def register_blueprints(app):
    # Register the Blueprints
    app.register_blueprint(user_blueprint)


def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    return app
