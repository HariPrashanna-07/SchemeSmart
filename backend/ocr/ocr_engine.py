from paddleocr import PaddleOCR

# load model once
ocr = PaddleOCR(use_angle_cls=True, lang="en")


def extract_text(image_path: str):
    result = ocr.ocr(image_path)

    extracted_text = []

    if result is None:
        return ""

    # handle new PaddleOCR output safely
    for block in result:
        if block is None:
            continue

        for line in block:
            try:
                text = line[1][0]
                extracted_text.append(text)
            except Exception:
                pass

    return " ".join(extracted_text)