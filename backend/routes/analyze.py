from fastapi import APIRouter, UploadFile, File
import shutil
from backend.ai.explainer import generate_explanation
from backend.database.users import get_user_profile, update_user_profile
from backend.ocr.ocr_engine import extract_text
from backend.ai.entity_extractor import extract_entities
from backend.ai.eligibility_engine import check_eligibility
from backend.database.mongo import get_database

router = APIRouter(prefix="/analyze", tags=["Analyze"])


@router.post("/")
async def analyze_document(
    user_id: str,
    file: UploadFile = File(...)
):


    # save file
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # OCR
    text = extract_text(file_path)

    # Entity extraction
    entities = extract_entities(text)
    # update profile
    update_user_profile(user_id, entities)

    # fetch merged profile
    profile = get_user_profile(user_id)

    # Eligibility
    db = get_database()
    schemes = list(db.schemes.find())

    eligible = []

    for scheme in schemes:
        if check_eligibility(profile, scheme):
            eligible.append(scheme["scheme_name"])

    explanation = generate_explanation(entities, eligible)

    return {
        "user_profile": profile,
        "eligible_schemes": eligible,
        "explanation": explanation
    }