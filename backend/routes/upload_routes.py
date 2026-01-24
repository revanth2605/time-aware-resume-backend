from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from data.skill_data import get_or_create_skill
from services.evidence_handler import process_certificate, process_code

upload_bp = Blueprint("upload", __name__)


@upload_bp.route("/upload/certificate", methods=["POST"])
@jwt_required()
def upload_certificate():
    identity = get_jwt_identity()
    user_id = identity["user_id"]

    data = request.json
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
    identity = get_jwt_identity()
    user_id = identity["user_id"]

    data = request.json
    skill_name = data.get("skill_name", "Python")

    skill = get_or_create_skill(user_id, skill_name)
    skill = process_code(skill)

    return {
        "message": "Code uploaded",
        "skill": skill
    }
