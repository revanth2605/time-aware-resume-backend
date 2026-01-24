from bson import ObjectId

def serialize_mongo_doc(doc):
    """
    Convert MongoDB document to JSON-safe dict
    WITHOUT removing any future-use fields.
    """
    if not doc:
        return doc

    serialized = {}

    for key, value in doc.items():
        if isinstance(value, ObjectId):
            serialized[key] = str(value)
        else:
            serialized[key] = value

    return serialized
