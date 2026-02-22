from fastapi import APIRouter
from backend.database.mongo import get_database
from bson import ObjectId

router = APIRouter(prefix="/schemes", tags=["Schemes"])


# ADD SCHEME
@router.post("/")
def add_scheme():
    db = get_database()

    scheme = {
        "scheme_name": "PMAY",
        "rules": [
            {"field": "income", "op": "<", "value": 300000},
            {"field": "owns_house", "op": "==", "value": False}
        ],
        "required_documents": [
            "aadhaar",
            "income_certificate"
        ]
    }

    result = db.schemes.insert_one(scheme)

    return {"id": str(result.inserted_id)}


# GET ALL SCHEMES
@router.get("/")
def get_schemes():
    db = get_database()

    schemes = []
    for s in db.schemes.find():
        s["_id"] = str(s["_id"])
        schemes.append(s)

    return schemes


# GET ONE SCHEME
@router.get("/{scheme_id}")
def get_scheme(scheme_id: str):
    db = get_database()

    scheme = db.schemes.find_one({"_id": ObjectId(scheme_id)})

    if scheme:
        scheme["_id"] = str(scheme["_id"])
        return scheme

    return {"error": "Scheme not found"}