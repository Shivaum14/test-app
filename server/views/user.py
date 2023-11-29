from flask import Blueprint, request, jsonify
from ..models import User, Session

user_blueprint = Blueprint("user_blueprint", __name__)


@user_blueprint.route("/user", methods=["POST"])
def add_user():
    session = Session()
    try:
        data = request.json
        new_user = User(name=data["name"], email=data["email"])
        session.add(new_user)
        session.commit()
        return jsonify({"message": "User added successfully"}), 201
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()
