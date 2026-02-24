from fastapi import APIRouter
from backend.database.mongo import get_database
from backend.ai.eligibility_engine import check_eligibility

router = APIRouter(prefix="/eligibility", tags=["Eligibility"])


@router.post("/")
def evaluate_user(user_data: dict):

    db = get_database()
    schemes = list(db.schemes.find())

    eligible_schemes = []

    for scheme in schemes:
        if check_eligibility(user_data, scheme):
            eligible_schemes.append(scheme["scheme_name"])

    return {"eligible_schemes": eligible_schemes}