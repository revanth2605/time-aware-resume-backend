from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from data.skill_data import (
    get_skill,
    get_skills_by_user,
    update_skill_visibility
)

from utils.serializers import serialize_mongo_doc

dashboard_bp = Blueprint("dashboard", __name__)


# -----------------------------------------
# SINGLE SKILL (keep existing behavior)
# -----------------------------------------

@dashboard_bp.route("/dashboard/get", methods=["GET"])
@jwt_required()
def get_dashboard():

    user_id = get_jwt_identity()

    skill = get_skill(user_id, "Python")

    if not skill:
        return {"message": "No skill data yet"}

    return {
        "user_id": user_id,
        "skill": serialize_mongo_doc(skill)
    }


# -----------------------------------------
# NEW: ALL USER SKILLS
# -----------------------------------------

@dashboard_bp.route("/dashboard/skills", methods=["GET"])
@jwt_required()
def get_all_skills():

    user_id = get_jwt_identity()

    skills = get_skills_by_user(user_id)

    return {
        "skills": [serialize_mongo_doc(s) for s in skills]
    }


# -----------------------------------------
# NEW: CHANGE VISIBILITY
# -----------------------------------------

@dashboard_bp.route("/dashboard/visibility", methods=["POST"])
@jwt_required()
def change_visibility():

    user_id = get_jwt_identity()
    data = request.json

    skill_name = data.get("skill_name")
    visibility = data.get("visibility")

    update_skill_visibility(user_id, skill_name, visibility)

    return {"message": "Visibility updated"}
