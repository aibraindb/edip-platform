from fastapi import APIRouter, File, UploadFile
from app.core.parser import extract_text_plain, extract_text_ocr
from app.core.loader import load_model_offline

router = APIRouter()

# Load layout-aware classifier once at startup
try:
    tokenizer, model = load_model_offline("./models/layoutlm-base-uncased")
except Exception:
    tokenizer, model = None, None

@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    pdf_bytes = await file.read()
    text_pages = extract_text_plain(pdf_bytes)
    ocr_pages = extract_text_ocr(pdf_bytes)
    doc_type = None
    if tokenizer and model:
        # placeholder classification output
        doc_type = "layout-aware-classifier"
    return {
        "doc_type": doc_type or "unknown",
        "pages": [{"page": i+1, "text": txt or ocr_pages[i]}
                  for i, txt in enumerate(text_pages)]
    }
