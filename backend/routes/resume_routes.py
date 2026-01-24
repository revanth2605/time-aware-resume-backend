from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from data.skill_data import get_skills_by_user

resume_bp = Blueprint("resume", __name__)


@resume_bp.route("/resume/get", methods=["GET"])
@jwt_required()
def get_resume():
    identity = get_jwt_identity()
    user_id = identity["user_id"]

    skills = get_skills_by_user(user_id)

    resume = [
        {
            "skill_name": s["skill_name"],
            "score": round(s["current_score"], 2),
            "visibility": s["visibility"]
        }
        for s in skills
    ]

    return {
        "user_id": user_id,
        "resume": resume
    }
