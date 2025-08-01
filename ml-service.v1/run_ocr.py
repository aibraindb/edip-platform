from collections import defaultdict

def group_by_headers(blocks, y_threshold=20):
    """
    Groups OCR-extracted blocks into headers and content based on vertical layout.

    Args:
        blocks (List[Dict]): Output from ocr_engine.run_ocr()
        y_threshold (int): Minimum vertical gap (px) to treat as a new block

    Returns:
        dict: Header → list of child lines
    """
    # Sort blocks by Y (top), then X (left)
    blocks.sort(key=lambda b: (b["top"], b["left"]))
    grouped = defaultdict(list)
    current_header = None

    for block in blocks:
        text = block["text"]
        height = block.get("height", 0)

        # Heuristic: headers are visually distinct (e.g., taller or short/capitalized text)
        is_header = (
            height > 30 or
            text.isupper() or
            (len(text.split()) <= 3 and text.istitle())
        )

        if is_header:
            current_header = text.strip()
            if current_header not in grouped:
                grouped[current_header] = []
        elif current_header:
            grouped[current_header].append(text.strip())

    return dict(grouped)
