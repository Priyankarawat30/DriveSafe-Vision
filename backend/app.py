from fastapi import FastAPI, UploadFile, File
from backend.detector import process_image
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from PIL import Image
import numpy as np
import io


app = FastAPI()

# CORS for Streamlit frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
async def detect_drowsiness(file: UploadFile = File(...)):
    content = await file.read()
    image = Image.open(io.BytesIO(content)).convert('RGB')
    image = np.array(image)
    result = process_image(image)
    return JSONResponse(result)
