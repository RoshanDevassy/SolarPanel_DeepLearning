from fastapi import FastAPI, File, UploadFile, HTTPException
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import traceback
from fastapi.middleware.cors import CORSMiddleware
import os

# Set the correct path relative to the script location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ✅ Load trained models
solar_panel_model_path = os.path.join(BASE_DIR,'api/models/SpClassifyModel/ClassifyModel.keras')
fault_model_path = os.path.join(BASE_DIR,'api/models/SpFaultModel/FaultModel.keras')

if not os.path.exists(solar_panel_model_path) or not os.path.exists(fault_model_path):
    raise RuntimeError("❌ Model file(s) not found - Ensure the paths are correct!\n")

try:
    solar_panel_model = tf.keras.models.load_model(solar_panel_model_path)
    fault_model = tf.keras.models.load_model(fault_model_path)
    print("✅ Models loaded successfully!\n")
except Exception as e:
    raise RuntimeError(f"❌ Error loading models: {str(e)}\n")

# ✅ Define class names
FAULT_CLASS_NAMES = ["Bird Drop", "Clean", "Dusty", "Physical Damage", "Snow"]
old_FAULT_CLASS_NAMES = ["clean", "dusty", "bird droppings", "snow", "physical damage"]
# ✅ Initialize FastAPI app
app = FastAPI()

origins = [
    "https://frontend-solarpanel.onrender.com",  # ✅ Your deployed frontend URL
]

# ✅ Enable CORS for Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Update with deployed frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Optimized Image Preprocessing Function
def preprocess_image(image: Image.Image) -> np.ndarray:
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize((299, 299), Image.LANCZOS)  # Optimized for Xception
    image_array = np.array(image, dtype=np.float32) / 255.0  # ✅ Ensure correct dtype & normalization
    return np.expand_dims(image_array, axis=0)  # ✅ Add batch dimension

# ✅ API Endpoint for Solar Panel Detection
@app.post("/detect-panel/")
async def detect_solar_panel(file: UploadFile = File(...)):
    try:
        image = Image.open(io.BytesIO(await file.read()))
        processed_image = preprocess_image(image)
        predictions = solar_panel_model.predict(processed_image, batch_size=1, verbose=0)[0]
        panel_confidence = round(float(predictions[0]), 4)
        print(f"🔍 [Solar Panel] Raw Model Output: {predictions}")

        # ✅ Classify based on threshold (0.5 for binary classification)
        predicted_class = "Solar Panel Detected" if panel_confidence >= 0.5 else "No Solar Panel Detected"
        
        return {
            "predicted_class": predicted_class,
            "confidence": panel_confidence,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"❌ Detection error: {str(e)}\n")

# ✅ API Endpoint for Fault Detection (Only if Solar Panel is Present)
@app.post("/detect-fault/")
async def detect_fault(file: UploadFile = File(...)):
    try:
        image = Image.open(io.BytesIO(await file.read()))
        processed_image = preprocess_image(image)

        # ✅ Step 1: Detect Solar Panel (Binary Classification)
        panel_predictions = solar_panel_model.predict(processed_image, batch_size=1, verbose=0)[0]
        panel_confidence = round(float(panel_predictions[0]), 4)
        panel_detected = panel_confidence > 0.5
        
        if not panel_detected:
            return {"message": "No solar panel detected. Please upload a valid solar panel image."}

        # ✅ Step 2: Predict Fault Type (Multi-Class Classification)
        fault_predictions = fault_model.predict(processed_image, batch_size=1, verbose=0)[0]

        # 🚨 Debugging: Print raw model output to verify correctness
        print(f"🔍 [Fault Detection] Raw Model Output: {fault_predictions}")

        # ✅ Ensure predictions are a valid probability distribution
        if not np.isclose(np.sum(fault_predictions), 1.0, atol=1e-3):
            print("⚠️ Warning: Model output is not a valid softmax distribution!")

        # ✅ Extract fault class index and confidence
        fault_class_idx = int(np.argmax(fault_predictions))  # ✅ Ensure integer index
        fault_confidence = round(float(np.max(fault_predictions)), 4)
        print(fault_confidence)
        # ✅ Ensure index is within FAULT_CLASS_NAMES range
        if fault_class_idx < 0 or fault_class_idx >= len(FAULT_CLASS_NAMES):
            return {"message": "❌ Error: Invalid fault class index detected."}

        return {
            "predicted_fault": FAULT_CLASS_NAMES[fault_class_idx],
            "confidence": fault_confidence
        }
    
    except Exception as e:
        print("❌ Exception in detect-fault:", traceback.format_exc())  # ✅ Print full error details
        raise HTTPException(status_code=500, detail=f"❌ Fault detection error: {str(e)}")


""" from fastapi import FastAPI, File, UploadFile, HTTPException
import tensorflow as tf
import numpy as np
from PIL import Image
import io
from fastapi.middleware.cors import CORSMiddleware
import os

# ✅ Load trained models
solar_panel_model_path = "C:\\Users\\rosha\\OneDrive\\Desktop\\Solar_Panel_Fault_Detection\\models\\solar\\spClassifierModel\\spClassifyModel_20250207_051941.keras"
fault_model_path = "C:\\Users\\rosha\\OneDrive\\Desktop\\Solar_Panel_Fault_Detection\\models\\updatedFinalsolarpanel.keras"

if not os.path.exists(solar_panel_model_path) or not os.path.exists(fault_model_path):
    raise RuntimeError("❌ Model file(s) not found - Ensure the paths are correct!\n")

try:
    solar_panel_model = tf.keras.models.load_model(solar_panel_model_path)
    fault_model = tf.keras.models.load_model(fault_model_path)
    print("✅ Models loaded successfully!\n")
except Exception as e:
    raise RuntimeError(f"❌ Error loading models: {str(e)}\n")

# ✅ Define class names
FAULT_CLASS_NAMES = ["Bird Drop", "Clean", "Dusty", "Physical Damage", "snow"]

# ✅ Initialize FastAPI app
app = FastAPI()

# ✅ Enable CORS for Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Update with deployed frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Optimized Image Preprocessing Function
def preprocess_image(image: Image.Image) -> np.ndarray:
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize((299, 299), Image.LANCZOS)  # Optimized for Xception
    image_array = np.array(image, dtype=np.float32) / 255.0 #Normalizing
    image.close()
    return np.expand_dims(image_array, axis=0) #batch size

# ✅ API Endpoint for Solar Panel Detection
@app.post("/detect-panel/")
async def detect_solar_panel(file: UploadFile = File(...)):
    try:
        image = Image.open(io.BytesIO(await file.read()))
        processed_image = preprocess_image(image)
        
        predictions = solar_panel_model.predict(processed_image, batch_size=1, verbose=0)[0]
        panel_confidence = round(float(predictions[0]), 4)
        print(f"🔍 Raw Model Output: {predictions[0]}")

        # ✅ Fix Binary Classification Output
        predicted_class = "Solar Panel Detected" if panel_confidence > 0.5 else "No Solar Panel Detected"
        
        return {
            "predicted_class": predicted_class,
            "confidence": panel_confidence,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"❌ Detection error: {str(e)}\n")

# ✅ API Endpoint for Fault Detection (Only if Solar Panel is Present)
@app.post("/detect-fault/")
async def detect_fault(file: UploadFile = File(...)):
    try:
        image = Image.open(io.BytesIO(await file.read()))
        processed_image = preprocess_image(image)

        # ✅ Step 1: Detect Solar Panel (Binary Classification)
        panel_predictions = solar_panel_model.predict(processed_image, batch_size=1, verbose=0)[0]
        panel_confidence = round(float(panel_predictions[0]), 4)  # ✅ Confidence for solar panel detection
        panel_detected = panel_confidence > 0.5  # ✅ Fix binary classification check
        
        if not panel_detected:
            return {"message": "No solar panel detected. Please upload a valid solar panel image."}

        # ✅ Step 2: Predict Fault Type (Multi-Class Classification)
        fault_predictions = fault_model.predict(processed_image, batch_size=1, verbose=0)[0]
        fault_class_idx = np.argmax(fault_predictions)  # ✅ Use argmax for softmax output
        fault_confidence = round(float(np.max(fault_predictions)), 4)
        
        return {
            "predicted_fault": FAULT_CLASS_NAMES[fault_class_idx],
            "confidence": fault_confidence
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"❌ Fault detection error: {str(e)}")
 """

"""
 from fastapi import FastAPI, File, UploadFile, HTTPException
import tensorflow as tf
import numpy as np
from PIL import Image
import io
from fastapi.middleware.cors import CORSMiddleware
import os

# ✅ Load trained model (Ensure it exists before serving API)
model_path = os.path.join("C:\\Users\\rosha\\OneDrive\\Desktop\\Solar_Panel_Fault_Detection\\models", "updatedfinalsolarpanel.keras")

if not os.path.exists(model_path):
    raise RuntimeError(f"❌ Model file not found at: {model_path} - Ensure the path is correct!")

try:
    model = tf.keras.models.load_model(model_path)
    print("✅ Model loaded successfully!")
except Exception as e:
    raise RuntimeError(f"❌ Error loading model: {str(e)}")

# ✅ Define class names (same order as training)
CLASS_NAMES = ["Clean","Dusty","Bird Drop","Snow","Physical Damage"]

# ✅ Initialize FastAPI app
app = FastAPI()

# ✅ Enable CORS for Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Update with deployed frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Optimized Image Preprocessing Function
def preprocess_image(image: Image.Image) -> np.ndarray:
    \"""
    Preprocess the input image:
    - Converts RGBA/Grayscale to RGB
    - Resizes to 224x224 using LANCZOS filter
    - Normalizes pixel values (0-1)
    - Adds batch dimension for model input
    \"""
    if image.mode != "RGB":  # Handle Grayscale & RGBA
        image = image.convert("RGB")

    image = image.resize((224, 224), Image.LANCZOS)  # High-quality resize
    image_array = np.array(image, dtype=np.float32) / 255.0  # Normalize pixel values
    image.close()  # ✅ Free memory after conversion
    return np.expand_dims(image_array, axis=0)  # Add batch dimension

# ✅ API Endpoint for Predictions
@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    \"""
    Handles image upload and returns the predicted class with confidence score.
    \"""
    try:
        # ✅ Read and preprocess image
        image = Image.open(io.BytesIO(await file.read()))
        processed_image = preprocess_image(image)

        # ✅ Perform Prediction
        predictions = model.predict(processed_image)[0]  # Extract batch-0 prediction
        predicted_class_idx = np.argmax(predictions)  # Get class index
        confidence = float(np.max(predictions))  # Get confidence score

        return {
            "predicted_class": CLASS_NAMES[predicted_class_idx],
            "confidence": round(confidence, 4)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"❌ Prediction error: {str(e)}") """


""" from fastapi import FastAPI, File, UploadFile, HTTPException
import tensorflow as tf
import numpy as np
from PIL import Image
import io
from fastapi.middleware.cors import CORSMiddleware
import os

# Load trained model

# Build the model path
model_path = os.path.join('C:\\Users\\rosha\\OneDrive\\Desktop\\Solar_Panel_Fault_Detection\\models', "newsolarpanel.keras")

# Check if the model file exists
if os.path.exists(model_path):
    model = tf.keras.models.load_model(model_path)
    print("Model loaded successfully!")
else:
    print("Model file not found!")

# Class names (same order as training data)
class_names = ["Bird-Drop", "Clean", "Dusty", "Electrical-Damage", "Physical-Damage", "Snow-Covered"]  # Update with your actual class names

app = FastAPI()

# Enable CORS for Next.js (Replace with your Next.js domain if hosted)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow all origins (or specify your frontend URL)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Preprocessing function
def preprocess_image(image: Image.Image):
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    image = image.resize((224, 224),Image.LANCZOS)  # Resize to match model input
    image = np.array(image) / 255.0   # Normalize pixel values
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# API endpoint for predictions
@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    try:
        # Read image file
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        
        # Preprocess image
        processed_image = preprocess_image(image)
        
        # Make prediction
        predictions = model.predict(processed_image)
        predicted_class = np.argmax(predictions)  # Get class index
        confidence = np.max(predictions)  # Get confidence score
        
        return {
            "predicted_class": class_names[predicted_class],
            "confidence": float(confidence)
        }

    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))

 """