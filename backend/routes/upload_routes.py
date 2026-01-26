from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from data.skill_data import get_or_create_skill
from services.evidence_handler import process_certificate, process_code
from utils.serializers import serialize_mongo_doc

upload_bp = Blueprint("upload", __name__)


# ---------------------------------------------------
# UPLOAD CERTIFICATE
# ---------------------------------------------------

@upload_bp.route("/upload/certificate", methods=["POST"])
@jwt_required()
def upload_certificate():

    user_id = get_jwt_identity()

    data = request.get_json(silent=True)
    if not data:
        return {"error": "JSON body required"}, 400

    skill_name = data.get("skill_name", "Python")

    # Visibility: public / private
    visibility = data.get("visibility", "private")

    # Optional future metadata (url, issuer, etc)
    metadata = data.get("metadata", {})

    skill = get_or_create_skill(user_id, skill_name, visibility)

    # Pass metadata later if needed (future AI usage)
    skill = process_certificate(skill)

    return {
        "message": "Certificate uploaded",
        "skill": serialize_mongo_doc(skill)
    }


# ---------------------------------------------------
# UPLOAD CODE
# ---------------------------------------------------

@upload_bp.route("/upload/code", methods=["POST"])
@jwt_required()
def upload_code():

    user_id = get_jwt_identity()

    data = request.get_json(silent=True)
    if not data:
        return {"error": "JSON body required"}, 400

    skill_name = data.get("skill_name", "Python")

    # Visibility: public / private
    visibility = data.get("visibility", "private")

    # Optional future metadata (repo url, snippet, etc)
    metadata = data.get("metadata", {})

    skill = get_or_create_skill(user_id, skill_name, visibility)

    skill = process_code(skill)

    return {
        "message": "Code uploaded",
        "skill": serialize_mongo_doc(skill)
    }
