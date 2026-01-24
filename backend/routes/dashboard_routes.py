from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from data.skill_data import get_skill

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard/get", methods=["GET"])
@jwt_required()
def get_dashboard():
    identity = get_jwt_identity()
    user_id = identity["user_id"]

    skill = get_skill(user_id, "Python")

    if not skill:
        return {"message": "No skill data yet"}

    return {
        "user_id": user_id,
        "skill": skill
    }
