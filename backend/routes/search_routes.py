from flask import Blueprint, request
from data.users import get_all_users
from data.skill_data import get_public_skills

search_bp = Blueprint("search", __name__)


@search_bp.route("/users/search", methods=["POST"])
def search_users():
    data = request.json
    query = data.get("query", "").lower()

    results = []

    users = get_all_users()

    for user in users:
        if query in user["username"].lower() or query in user["user_id"].lower():
            public_skills = get_public_skills(user["user_id"])

            if public_skills:  # show only users with public data
                results.append({
                    "username": user["username"],
                    "user_id": user["user_id"],
                    "public_skills": [
                        {
                            "skill_name": s["skill_name"],
                            "score": round(s["current_score"], 2)
                        }
                        for s in public_skills
                    ]
                })

    return {"results": results}
