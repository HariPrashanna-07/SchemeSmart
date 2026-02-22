import re
import spacy

nlp = spacy.load("en_core_web_sm")


def extract_entities(text: str):

    doc = nlp(text)

    data = {
        "name": None,
        "organization": None,
        "study_year": None,
        "total_amount": None
    }

    # -------------------------
    # 1️⃣ NAME EXTRACTION (RULE BASED)
    # -------------------------
    name_match = re.search(
        r"Mr\.?\s+([A-Z\s]+)",
        text
    )

    if name_match:
        data["name"] = name_match.group(1).strip()

    # fallback NLP
    if not data["name"]:
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                data["name"] = ent.text
                break

    # -------------------------
    # 2️⃣ ORGANIZATION
    # -------------------------
    # Better organization detection
    # -------------------------
    # ORGANIZATION EXTRACTION + CLEANING
    # -------------------------
    org_match = re.search(
        r"([A-Z][A-Za-z\s]+?(College|University|Institute)[A-Za-z\s]*)",
        text
    )

    if org_match:
        org = org_match.group(1).strip()

        # remove trailing numbers or single letters from OCR noise
        org = re.sub(r"\s+[A-Z]?\d.*$", "", org)

        # remove isolated trailing letters
        org = re.sub(r"\s+[A-Z]$", "", org)

        data["organization"] = org
    # -------------------------
    # 3️⃣ STUDY YEAR
    # -------------------------
    year_match = re.search(
        r"(First|Second|Third|Fourth)\s+year",
        text,
        re.I,
    )

    mapping = {
        "First": 1,
        "Second": 2,
        "Third": 3,
        "Fourth": 4
    }

    if year_match:
        data["study_year"] = mapping[year_match.group(1).capitalize()]

    # -------------------------
    # 4️⃣ TOTAL AMOUNT (SMART)
    # -------------------------
    total_match = re.search(
        r"Total\s+(\d+)",
        text,
        re.I
    )

    if total_match:
        data["total_amount"] = int(total_match.group(1))

    return data