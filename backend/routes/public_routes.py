from flask import Blueprint, request
from data.users import get_user_by_username
from data.skill_data import get_public_skills

public_bp = Blueprint("public", __name__)

# -----------------------------------------
# EXISTING ROUTE (KEPT AS-IS)
# -----------------------------------------

@public_bp.route("/users/public", methods=["POST"])
def public_profile():
    data = request.json
    username = data.get("username")

    user = get_user_by_username(username)
    if not user:
        return {"error": "User not found"}, 404

    public_skills = get_public_skills(user["user_id"])

    profile = {
        "username": user["username"],
        "user_id": user["user_id"],
        "public_skills": [
            {
                "skill_name": s["skill_name"],
                "score": round(s["current_score"], 2)
            }
            for s in public_skills
        ]
    }

    return profile


# -----------------------------------------
# NEW ROUTE (FOR FRONTEND PUBLIC PROFILE)
# -----------------------------------------

@public_bp.route("/public/profile/<username>", methods=["GET"])
def public_profile_get(username):

    user = get_user_by_username(username)
    if not user:
        return {"error": "User not found"}, 404

    public_skills = get_public_skills(user["user_id"])

    return {
        "username": user["username"],
        "skills": [
            {
                "skill_name": s["skill_name"],
                "current_score": round(s["current_score"], 2)
            }
            for s in public_skills
        ]
    }
