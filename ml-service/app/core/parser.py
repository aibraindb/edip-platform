import pdfplumber
from pdf2image import convert_from_bytes
import pytesseract
import io
from PIL import Image

def extract_text_plain(pdf_bytes: bytes):
    pages = []
    with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
        for page in pdf.pages:
            pages.append(page.extract_text() or "")
    return pages

def extract_text_ocr(pdf_bytes: bytes):
    ocr_pages = []
    images = convert_from_bytes(pdf_bytes)
    for img in images:
        gray = img.convert("L")
        ocr_pages.append(pytesseract.image_to_string(gray))
    return ocr_pages

def pages_as_images(pdf_bytes: bytes):
    return convert_from_bytes(pdf_bytes)
