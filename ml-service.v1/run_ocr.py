from PIL import Image
import pytesseract
from collections import defaultdict
import numpy as np

def run_ocr(image_path):
    """
    Extracts and groups text from an architecture diagram image without hardcoding.
    Uses Tesseract's bounding box metadata to infer section headers and structure.

    Args:
        image_path (str): Path to the image file

    Returns:
        dict: A dictionary with headers as keys and list of items as values
    """
    # Load image
    img = Image.open(image_path).convert("RGB")
    np_img = np.array(img)

    # Extract word-level box data
    ocr_data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)

    # Collect all text boxes
    blocks = []
    for i in range(len(ocr_data["text"])):
        text = ocr_data["text"][i].strip()
        if not text:
            continue
        blocks.append({
            "text": text,
            "left": ocr_data["left"][i],
            "top": ocr_data["top"][i],
            "width": ocr_data["width"][i],
            "height": ocr_data["height"][i],
            "line_num": ocr_data["line_num"][i],
            "block_num": ocr_data["block_num"][i],
            "par_num": ocr_data["par_num"][i],
        })

    # Sort top-to-bottom, left-to-right
    blocks.sort(key=lambda b: (b["top"], b["left"]))

    # Group under headers
    grouped = defaultdict(list)
    current_header = None

    for block in blocks:
        text = block["text"]
        height = block["height"]

        is_header = (
            height > 30 or
            text.isupper() or
            (len(text.split()) <= 3 and text.istitle())
        )

        if is_header:
            current_header = text
            if current_header not in grouped:
                grouped[current_header] = []
        elif current_header:
            grouped[current_header].append(text)

    return dict(grouped)
