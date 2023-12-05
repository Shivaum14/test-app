from flask import Flask
from .views.todo import todo_blueprint


def register_blueprints(app):
    # Register the Blueprints
    app.register_blueprint(todo_blueprint)


def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    return app
