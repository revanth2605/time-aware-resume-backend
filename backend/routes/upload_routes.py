from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from data.skill_data import get_or_create_skill
from services.evidence_handler import process_certificate, process_code
from utils.serializers import serialize_mongo_doc

upload_bp = Blueprint("upload", __name__)


@upload_bp.route("/upload/certificate", methods=["POST"])
@jwt_required()
def upload_certificate():
    # JWT identity is a STRING (user_id)
    user_id = get_jwt_identity()

    # Safe JSON parsing
    data = request.get_json(silent=True)
    if not data:
        return {"error": "JSON body required"}, 400

    skill_name = data.get("skill_name", "Python")

    # Core logic (kept for future use)
    skill = get_or_create_skill(user_id, skill_name)
    skill = process_certificate(skill)

    # Serialize MongoDB document safely
    return {
        "message": "Certificate uploaded",
        "skill": serialize_mongo_doc(skill)
    }


@upload_bp.route("/upload/code", methods=["POST"])
@jwt_required()
def upload_code():
    # JWT identity is a STRING (user_id)
    user_id = get_jwt_identity()

    # Safe JSON parsing
    data = request.get_json(silent=True)
    if not data:
        return {"error": "JSON body required"}, 400

    skill_name = data.get("skill_name", "Python")

    # Core logic (kept for future AI / admin use)
    skill = get_or_create_skill(user_id, skill_name)
    skill = process_code(skill)

    # Serialize MongoDB document safely
    return {
        "message": "Code uploaded",
        "skill": serialize_mongo_doc(skill)
    }
