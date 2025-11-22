import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
import io

# -------------------------------
# Load Model
# -------------------------------
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("models/waste_classifier.h5")
    return model

model = load_model()

# Waste labels (modify based on your actual model classes)
CLASS_NAMES = ["Plastic", "Paper", "Metal", "Glass", "Organic"]

# -------------------------------
# App UI
# -------------------------------
st.set_page_config(
    page_title="AI Waste Sorter",
    page_icon="♻️",
    layout="centered"
)

st.title("♻️ AI Waste Sorter")
st.write("Upload a waste image and let AI classify it for proper recycling.")

# -------------------------------
# Image Upload
# -------------------------------
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

def preprocess_image(img):
    img = img.resize((224, 224))        # Adjust if your model uses a different size
    img = np.array(img) / 255.0         # Normalization
    img = np.expand_dims(img, axis=0)   # Add batch dimension
    return img

# -------------------------------
# Prediction
# -------------------------------
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    st.write("Classifying...")

    processed_img = preprocess_image(image)
    predictions = model.predict(processed_img)
    score = tf.nn.softmax(predictions[0])

    predicted_class = CLASS_NAMES[np.argmax(score)]
    confidence = np.max(score) * 100

    st.success(f"### 🗑 Waste Type: **{predicted_class}**")
    st.info(f"Prediction Confidence: **{confidence:.2f}%**")

    # -------------------------------
    # Recycling Tips
    # -------------------------------
    tips = {
        "Plastic": "Rinse plastic items and remove labels before recycling.",
        "Paper": "Avoid recycling wet or dirty paper.",
        "Metal": "Clean metal cans and separate aluminum from steel if possible.",
        "Glass": "Sort glass by color and remove lids.",
        "Organic": "Best used for composting to reduce landfill waste."
    }

    st.write("### ♻️ Recycling Guide")
    st.write(tips.get(predicted_class, "Dispose responsibly."))

else:
    st.warning("Please upload an image to begin classification.")
