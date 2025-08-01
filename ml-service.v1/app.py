
import streamlit as st
from PIL import Image
from ocr_engine import run_ocr
from run_ocr import group_by_headers

st.set_page_config(page_title="Document Intelligence MVP", layout="wide")
st.title("🧠 Document Intelligence MVP")

# Sidebar controls
st.sidebar.header("OCR Settings")
ocr_method = st.sidebar.selectbox("Select OCR Engine", ["tesseract", "doctr", "paddleocr"])

uploaded_file = st.file_uploader("📄 Upload a document image (PNG, JPG)", type=["jpg", "jpeg", "png"])

def extract_information(image, method="tesseract"):
    blocks = run_ocr(image, method=method)
    grouped_output = group_by_headers(blocks)
    return grouped_output

if uploaded_file is not None:
    # Convert to PIL image
    image = Image.open(uploaded_file).convert("RGB")

    # Display image
    st.image(image, caption="Uploaded Document", use_column_width=True)

    # Process and extract
    with st.spinner(f"Running OCR with {ocr_method}..."):
        result = extract_information(image, method=ocr_method)

    # Display result
    st.subheader("📋 Extracted Information")
    st.json(result)
