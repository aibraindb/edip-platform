def extract_fields(ocr_result, model="none"):
    if model == "donut":
        return {"message": "Donut model stub"}
    elif model == "layoutlmv3":
        return {"message": "LayoutLMv3 model stub"}
    else:
        return {"raw_text": ocr_result}
