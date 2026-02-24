def classify_document(text: str) -> str:
    """
    Simple document classifier based on keywords.
    Later we can replace with LLM classification.
    """

    text_lower = text.lower()

    # Aadhaar detection
    if "aadhaar" in text_lower or "uidai" in text_lower:
        return "aadhaar"

    # Bonafide certificate
    if "bonafide" in text_lower or "certificate" in text_lower:
        return "bonafide"

    # Income certificate
    if "income certificate" in text_lower or "annual income" in text_lower:
        return "income_certificate"

    # College marksheet
    if "marksheet" in text_lower or "semester" in text_lower:
        return "marksheet"

    return "unknown"