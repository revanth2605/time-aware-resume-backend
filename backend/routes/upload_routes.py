from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from data.skill_data import get_or_create_skill
from services.evidence_handler import process_certificate, process_code

upload_bp = Blueprint("upload", __name__)


@upload_bp.route("/upload/certificate", methods=["POST"])
@jwt_required()
def upload_certificate():
    user_id = get_jwt_identity()  # ✅ identity is already a string

    data = request.get_json(silent=True)
    if not data:
        return {"error": "JSON body required"}, 400

    skill_name = data.get("skill_name", "Python")

    skill = get_or_create_skill(user_id, skill_name)
    skill = process_certificate(skill)

    return {
        "message": "Certificate uploaded",
        "skill": skill
    }


@upload_bp.route("/upload/code", methods=["POST"])
@jwt_required()
def upload_code():
    user_id = get_jwt_identity()  # ✅ FIXED

    data = request.get_json(silent=True)
    if not data:
        return {"error": "JSON body required"}, 400

    skill_name = data.get("skill_name", "Python")

    skill = get_or_create_skill(user_id, skill_name)
    skill = process_code(skill)

    return {
        "message": "Code uploaded",
        "skill": skill
    }
