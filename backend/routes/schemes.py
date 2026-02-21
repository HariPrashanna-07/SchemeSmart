from fastapi import APIRouter
from backend.database.mongo import get_database

router = APIRouter()

@router.post("/add-scheme")
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

    return {"inserted_id": str(result.inserted_id)}