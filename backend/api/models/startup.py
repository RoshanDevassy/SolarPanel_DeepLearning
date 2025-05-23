import os
import gdown

# Set up model directories
os.makedirs("models/SpClassifyModel", exist_ok=True)
os.makedirs("models/SpFaultModel", exist_ok=True)

# Define URLs
SPCLASS_MODEL_URL = os.getenv("SPCLASS_MODEL_URL")
SPFAULT_MODEL_URL = os.getenv("SPFAULT_MODEL_URL")

# Define output paths
classify_model_path = "models/SpClassifyModel/ClassifyModel.keras"
fault_model_path = "models/SpFaultModel/FaultModel.keras"

# Download classification model
if not os.path.exists(classify_model_path):
    print("📥 Downloading classification model...")
    gdown.download(SPCLASS_MODEL_URL, classify_model_path, quiet=False)
else:
    print("✅ Classification model already exists")

# Download fault detection model
if not os.path.exists(fault_model_path):
    print("📥 Downloading fault model...")
    gdown.download(SPFAULT_MODEL_URL, fault_model_path, quiet=False)
else:
    print("✅ Fault model already exists")
