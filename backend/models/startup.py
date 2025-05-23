# backend/models/startup.py
import os
import gdown

# Set up model info
MODELS = {
    "SpClassifyModel/ClassifyModel.keras": os.getenv("SPCLASS_MODEL_URL"),
    "SpFaultModel/FaultModel.keras": os.getenv("SPFAULT_MODEL_URL"),
}

def download_model(local_path, url):
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    if not os.path.exists(local_path):
        print(f"Downloading {local_path}...")
        gdown.download(url, local_path, quiet=False)
    else:
        print(f"{local_path} already exists. Skipping download.")

for path, url in MODELS.items():
    if url:
        download_model(f"models/{path}", url)
