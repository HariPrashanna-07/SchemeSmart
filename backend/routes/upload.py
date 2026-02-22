from fastapi import APIRouter, UploadFile, File
import os
from backend.ocr.ocr_engine import extract_text
from backend.ai.entity_extractor import extract_entities

router = APIRouter(prefix="/upload", tags=["Upload"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/")
async def upload_document(file: UploadFile = File(...)):
    try:
        file_path = os.path.join(UPLOAD_DIR, file.filename)

        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        print("Processing OCR:", file_path)

        text = extract_text(file_path)
        entities = extract_entities(text)

        return {
            "filename": file.filename,
            "extracted_text": text,
            "entities": entities
        }

        return {
            "filename": file.filename,
            "extracted_text": text
        }

    except Exception as e:
        return {"error": str(e)}