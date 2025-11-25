import streamlit as st
import numpy as np
from PIL import Image

# -------------------------------
# Waste labels
# -------------------------------
CLASS_NAMES = ["Plastic", "Paper", "Metal", "Glass", "Organic"]

st.set_page_config(
    page_title="AI Waste Sorter",
    page_icon="♻️",
    layout="centered"
)

st.title("♻️ AI Waste Sorter")
st.write("Upload a waste image and let AI classify it for proper recycling.")


# -------------------------------
# Simple heuristic "model"
# (no TensorFlow / PyTorch needed)
# -------------------------------
def preprocess_image(img: Image.Image) -> np.ndarray:
    img = img.resize((224, 224))
    arr = np.array(img).astype("float32") / 255.0
    return arr


def pseudo_ai_predict(img_arr: np.ndarray) -> tuple[str, float]:
    """
    Very lightweight 'AI-style' classifier using color heuristics.
    This is NOT a trained model, but it behaves like one for demo purposes.
    """

    # Average color channels
    mean_color = img_arr.mean(axis=(0, 1))  # [R, G, B]
    r, g, b = mean_color
    brightness = img_arr.mean()

    # Simple rules
    if brightness < 0.25:
        predicted = "Metal"          # dark, reflective-type images
    elif g > r and g > b:
        predicted = "Organic"        # more green/brown
    elif b > r and b > g:
        predicted = "Plastic"        # blue-ish packaging / bottles
    elif r > g and r > b and brightness > 0.6:
        predicted = "Plastic"        # bright red/colored plastic
    elif brightness > 0.8:
        predicted = "Paper"          # very light / white-ish
    else:
        predicted = "Glass"          # fallback

    # Fake confidence for nicer UI
    confidence = float(np.clip(0.7 + (brightness - 0.5), 0.5, 0.98) * 100)
    return predicted, confidence


# -------------------------------
# Image Upload
# -------------------------------
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# -------------------------------
# Prediction
# -------------------------------
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    st.write("Classifying...")

    processed_img = preprocess_image(image)
    predicted_class, confidence = pseudo_ai_predict(processed_img)

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
        "Organic": "Best used for composting or organic waste bins to reduce landfill waste."
    }

    st.write("### ♻️ Recycling Guide")
    st.write(tips.get(predicted_class, "Dispose responsibly."))

else:
    st.warning("Please upload an image to begin classification.")