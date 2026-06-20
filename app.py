import streamlit as st
from PIL import Image
import time
import onnxruntime as ort
import numpy as np
from datetime import datetime

st.set_page_config(page_title="Offline Waste AI", layout="centered")

st.title("🗑️ Offline Edge AI Waste Classifier (ADTC 2026)")
st.caption("Runs fully offline on 8GB CPU laptops")

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    return ort.InferenceSession("model/waste_model.onnx")

model = load_model()

labels = ["plastic", "paper", "metal", "organic"]

# ---------------- IMAGE PREPROCESS ----------------
def preprocess(image):
    image = image.resize((128, 128))
    img = np.array(image).astype("float32") / 255.0
    img = np.expand_dims(img, axis=0)
    return img

# ---------------- UPLOAD ----------------
uploaded = st.file_uploader("Upload waste image", type=["jpg", "png", "jpeg"])

if uploaded:
    image = Image.open(uploaded)
    st.image(image, caption="Input Image", use_container_width=True)

    # ---------------- INFERENCE ----------------
    input_data = preprocess(image)

    start = time.time()
    outputs = model.run(None, {"input": input_data})[0]
    end = time.time()

    prediction = labels[np.argmax(outputs)]
    confidence = float(np.max(outputs))

    # ---------------- OUTPUT ----------------
    st.success(f"Prediction: {prediction}")
    st.info(f"Confidence: {confidence:.2f}")
    st.write(f"⏱ Inference time: {(end-start)*1000:.2f} ms")
    st.write("✔ Fully offline ONNX execution")

# ---------------- REPORT ----------------
if uploaded:
    report = f"""
ADTC 2026 Waste Classification Report
Date: {datetime.now()}
Prediction: {prediction}
Confidence: {confidence}
Offline: YES
"""

    st.download_button(
        "Download Report",
        report,
        file_name="waste_report.txt"
    )