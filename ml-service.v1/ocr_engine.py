import pytesseract
from PIL import Image

# Optional: Set Tesseract binary location if needed
# pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

def run_ocr(image, method="tesseract"):
    """
    Runs OCR using the specified method and returns normalized text block list.
    Supported methods: tesseract, doctr, paddleocr
    """
    print(f"[INFO] Running OCR with method: {method}")

    if isinstance(image, str):
        image = Image.open(image)

    results = []

    if method == "tesseract":
        ocr_data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
        n = len(ocr_data["text"])
        for i in range(n):
            text = ocr_data["text"][i].strip()
            if not text:
                continue
            results.append({
                "text": text,
                "left": ocr_data["left"][i],
                "top": ocr_data["top"][i],
                "width": ocr_data["width"][i],
                "height": ocr_data["height"][i],
                "line_num": ocr_data["line_num"][i],
                "block_num": ocr_data["block_num"][i],
                "par_num": ocr_data["par_num"][i],
            })

    elif method == "doctr":
        from doctr.models import ocr_predictor
        from doctr.io import DocumentFile
        model = ocr_predictor(pretrained=True)
        doc = DocumentFile.from_images(image)
        output = model(doc)

        for page in output.pages:
            for block in page.blocks:
                for line in block.lines:
                    text = " ".join([word.value for word in line.words])
                    bbox = line.geometry[0]  # Top-left
                    results.append({
                        "text": text,
                        "left": int(bbox[0] * image.size[0]),
                        "top": int(bbox[1] * image.size[1]),
                        "width": 0,  # doctr doesn't give width
                        "height": 0,
                    })

    elif method == "paddleocr":
        from paddleocr import PaddleOCR
        ocr = PaddleOCR(use_angle_cls=True, lang='en')
        result = ocr.ocr(np.array(image))

        for line in result[0]:
            text = line[1][0]
            box = line[0]
            left = int(box[0][0])
            top = int(box[0][1])
            results.append({
                "text": text,
                "left": left,
                "top": top,
                "width": 0,
                "height": 0
            })

    else:
        raise ValueError(f"OCR method '{method}' not supported")

    return results
