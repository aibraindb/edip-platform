import os
from transformers import AutoTokenizer, AutoModel
from pathlib import Path

def load_model_offline(model_dir: str):
    os.environ["TRANSFORMERS_OFFLINE"] = "1"
    if not Path(model_dir).exists():
        raise FileNotFoundError(f"Model directory '{model_dir}' not found")
    tokenizer = AutoTokenizer.from_pretrained(model_dir, local_files_only=True)
    model = AutoModel.from_pretrained(model_dir, local_files_only=True)
    return tokenizer, model
