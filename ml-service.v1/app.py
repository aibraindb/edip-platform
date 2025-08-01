import streamlit as st
from PIL import Image
from config import CONFIG
from ocr_engine import run_ocr
from layout_engine import detect_layout
from extraction_engine import extract_fields

st.title("Document Intelligence MVP")

uploaded_file = st.file_uploader("Upload a document image", type=["png", "jpg", "jpeg"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Document", use_column_width=True)
    
    ocr_result = run_ocr(image, CONFIG["ocr"])
    layout_info = detect_layout(image, CONFIG["layout"])
    extracted = extract_fields(ocr_result, CONFIG["extractor"])
    
    st.subheader("Extracted Information")
    st.json(extracted)
