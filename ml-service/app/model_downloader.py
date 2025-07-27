import argparse
from transformers import AutoTokenizer, AutoModel

def download_model(model_name: str, save_dir: str):
    print(f"Downloading model '{model_name}' to '{save_dir}'")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    tokenizer.save_pretrained(save_dir)
    model.save_pretrained(save_dir)
    print("Download complete")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True, help="HuggingFace model name")
    parser.add_argument("--dest", default="./models", help="Destination folder")
    args = parser.parse_args()
    download_model(args.model, f"{args.dest}/{args.model.split('/')[-1]}")
