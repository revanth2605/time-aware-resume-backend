from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity

from data.code_evidence import get_code_evidence_by_skill
from data.certificate_evidence import get_certificate_evidence_by_skill
from utils.serializers import serialize_mongo_doc

evidence_bp = Blueprint("evidence", __name__)

# -----------------------------------
# CODE HISTORY
# -----------------------------------

@evidence_bp.route("/evidence/code/<skill_name>", methods=["GET"])
@jwt_required()
def get_code_history(skill_name):

    user_id = get_jwt_identity()

    records = get_code_evidence_by_skill(user_id, skill_name)

    return {
        "records": [serialize_mongo_doc(r) for r in records]
    }


# -----------------------------------
# CERTIFICATE HISTORY
# -----------------------------------

@evidence_bp.route("/evidence/certificate/<skill_name>", methods=["GET"])
@jwt_required()
def get_certificate_history(skill_name):

    user_id = get_jwt_identity()

    records = get_certificate_evidence_by_skill(user_id, skill_name)

    return {
        "records": [serialize_mongo_doc(r) for r in records]
    }
