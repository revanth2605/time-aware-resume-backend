from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson import ObjectId

from data.code_evidence import get_code_evidence_by_skill
from data.certificate_evidence import get_certificate_evidence_by_skill
from data.db import code_evidence_collection, certificate_evidence_collection
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


# -----------------------------------
# DELETE CODE EVIDENCE
# -----------------------------------

@evidence_bp.route("/evidence/code/<evidence_id>", methods=["DELETE"])
@jwt_required()
def delete_code_evidence(evidence_id):

    user_id = get_jwt_identity()

    code_evidence_collection.delete_one({
        "_id": ObjectId(evidence_id),
        "user_id": user_id
    })

    return {"message": "Code evidence deleted"}


# -----------------------------------
# DELETE CERTIFICATE EVIDENCE
# -----------------------------------

@evidence_bp.route("/evidence/certificate/<evidence_id>", methods=["DELETE"])
@jwt_required()
def delete_certificate_evidence(evidence_id):

    user_id = get_jwt_identity()

    certificate_evidence_collection.delete_one({
        "_id": ObjectId(evidence_id),
        "user_id": user_id
    })

    return {"message": "Certificate evidence deleted"}
