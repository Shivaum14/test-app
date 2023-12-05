import datetime
from flask import Blueprint, request, jsonify
from ..models import Todo, Session

todo_blueprint = Blueprint("todo_blueprint", __name__)


@todo_blueprint.route("/todo", methods=["POST"])
def add_todo():
    session = Session()
    try:
        data = request.json
        new_todo = Todo(value=data["value"], date=datetime.datetime.now())
        session.add(new_todo)
        session.commit()
        return jsonify({"message": "Todo added successfully"}), 201
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()


@todo_blueprint.route("/todos", methods=["GET"])
def get_todos():
    session = Session()
    todos = session.query(Todo).all()
    return jsonify([todo.to_dict() for todo in todos]), 200
