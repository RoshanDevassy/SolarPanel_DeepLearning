import os
import gdown

# get absolute directory of this file (startup.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# models directory relative to this file
MODELS_DIR = os.path.join(BASE_DIR)

# Create folders if they don't exist
os.makedirs(os.path.join(MODELS_DIR, "SpClassifyModel"), exist_ok=True)
os.makedirs(os.path.join(MODELS_DIR, "SpFaultModel"), exist_ok=True)

# URLs (same as before)
SPCLASS_MODEL_URL = os.getenv("SPCLASS_MODEL_URL")
SPFAULT_MODEL_URL = os.getenv("SPFAULT_MODEL_URL")

# Define full output paths for downloads
classify_model_path = os.path.join(MODELS_DIR, "SpClassifyModel", "ClassifyModel.keras")
fault_model_path = os.path.join(MODELS_DIR, "SpFaultModel", "FaultModel.keras")

print(f"Downloading ClassifyModel to: {classify_model_path}")
print(f"Downloading FaultModel to: {fault_model_path}")

# Download if not already present
if not os.path.exists(classify_model_path):
    print("📥 Downloading classification model...")
    gdown.download(SPCLASS_MODEL_URL, classify_model_path, quiet=False)
else:
    print("✅ Classification model already exists")

if not os.path.exists(fault_model_path):
    print("📥 Downloading fault model...")
    gdown.download(SPFAULT_MODEL_URL, fault_model_path, quiet=False)
else:
    print("✅ Fault model already exists")
