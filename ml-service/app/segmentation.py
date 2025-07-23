import os
import pdfplumber

def segment_pdf(doc_id: str):
    filepath = f"/tmp/{doc_id}.pdf"
    if not os.path.exists(filepath):
        print(f"[Segmentation] File not found: {filepath}")
        return

    with pdfplumber.open(filepath) as pdf:
        print(f"[Segmentation] Total pages: {len(pdf.pages)}")
        for i, page in enumerate(pdf.pages):
            text = page.extract_text() or ""
            print(f"Page {i+1} Text Sample: {text[:50]}...")
