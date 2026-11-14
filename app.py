import streamlit as st
import numpy as np
import onnxruntime as ort
from PIL import Image, ImageOps
from pathlib import Path

# ==========================================
# ECOSORT AI - SMART WASTE CLASSIFIER
# ==========================================

st.set_page_config(
    page_title="EcoSort AI",
    page_icon="♻️",
    layout="wide"
)

st.title("♻️ EcoSort AI")
st.subheader("AI-Powered Waste Classification Assistant")

st.write(
    "Upload an image of waste to identify its predicted category "
    "and receive recycling and disposal guidance."
)

# ==========================================
# MODEL CONFIGURATION
# ==========================================

MODEL_PATHS = [
    Path("Model/waste_model.onnx"),
    Path("model/waste_model.onnx")
]

LABEL_PATHS = [
    Path("Model/labels.txt"),
    Path("Model/class_names.txt"),
    Path("model/labels.txt"),
    Path("labels.txt")
]

model_path = next(
    (path for path in MODEL_PATHS if path.exists()),
    None
)

# ==========================================
# WASTE CATEGORY GUIDANCE
# ==========================================

WASTE_GUIDANCE = {
    "plastic": {
        "category": "Plastic Waste",
        "advice": "Separate plastic items from general waste.",
        "action": "Clean and dry recyclable plastics before taking them to a recycling centre.",
        "impact": "Recycling plastic helps reduce pollution and conserve resources."
    },
    "paper": {
        "category": "Paper Waste",
        "advice": "Keep paper clean and dry.",
        "action": "Reuse paper where possible or send recyclable paper to a recycling facility.",
        "impact": "Paper recycling helps reduce the demand for fresh timber."
    },
    "cardboard": {
        "category": "Cardboard Waste",
        "advice": "Flatten cardboard boxes before storage.",
        "action": "Keep cardboard dry and send it to a paper recycling centre.",
        "impact": "Cardboard recycling reduces landfill waste."
    },
    "glass": {
        "category": "Glass Waste",
        "advice": "Separate glass containers from other waste.",
        "action": "Reuse glass bottles or take them to an appropriate glass recycling facility.",
        "impact": "Glass can be recycled repeatedly."
    },
    "metal": {
        "category": "Metal Waste",
        "advice": "Separate metal cans and containers.",
        "action": "Take recyclable metals to a scrap-metal collection or recycling centre.",
        "impact": "Metal recycling saves energy and raw materials."
    },
    "organic": {
        "category": "Organic Waste",
        "advice": "Separate food scraps and biodegradable materials.",
        "action": "Consider composting suitable organic waste.",
        "impact": "Composting helps return nutrients to the soil."
    },
    "food": {
        "category": "Food Waste",
        "advice": "Separate leftover food from recyclable materials.",
        "action": "Compost suitable food scraps where facilities are available.",
        "impact": "Reducing food waste helps conserve resources."
    },
    "battery": {
        "category": "Battery / Electronic Hazardous Waste",
        "advice": "Do not put batteries in ordinary household waste.",
        "action": "Use an authorised battery or electronic waste collection point.",
        "impact": "Proper disposal helps prevent hazardous substances from contaminating the environment."
    }
}


def get_guidance(label):
    label = label.lower()

    for keyword, guidance in WASTE_GUIDANCE.items():
        if keyword in label:
            return guidance

    return {
        "category": label.title(),
        "advice": "Keep this material separate until its composition is confirmed.",
        "action": "Check with a local waste management or recycling facility.",
        "impact": "Correct waste sorting supports responsible waste management."
    }


# ==========================================
# LOAD CLASS LABELS
# ==========================================

def load_labels():
    for path in LABEL_PATHS:
        if path.exists():
            with open(path, "r", encoding="utf-8") as file:
                labels = [
                    line.strip()
                    for line in file
                    if line.strip()
                ]

            if labels:
                return labels

    return None


# ==========================================
# LOAD ONNX MODEL
# ==========================================

@st.cache_resource
def load_model(path):
    return ort.InferenceSession(
        str(path),
        providers=["CPUExecutionProvider"]
    )


# ==========================================
# IMAGE PREPROCESSING
# ==========================================

def prepare_image(image, input_shape):
    image = ImageOps.exif_transpose(image).convert("RGB")

    height = input_shape[2] if isinstance(input_shape[2], int) else 224
    width = input_shape[3] if isinstance(input_shape[3], int) else 224

    # Detect channels-last input if applicable
    channels_last = (
        isinstance(input_shape[3], int)
        and input_shape[3] == 3
    )

    if channels_last:
        height = input_shape[1] if isinstance(input_shape[1], int) else 224
        width = input_shape[2] if isinstance(input_shape[2], int) else 224

    image = image.resize((width, height))

    array = np.asarray(image).astype(np.float32) / 255.0

    if channels_last:
        array = np.expand_dims(array, axis=0)
    else:
        array = np.transpose(array, (2, 0, 1))
        array = np.expand_dims(array, axis=0)

    return array


# ==========================================
# PREDICTION
# ==========================================

def classify_image(session, image, labels):
    input_details = session.get_inputs()[0]
    input_name = input_details.name

    input_shape = input_details.shape

    processed_image = prepare_image(
        image,
        input_shape
    )

    results = session.run(
        None,
        {input_name: processed_image}
    )

    predictions = np.asarray(results[0]).squeeze()

    if predictions.ndim != 1:
        raise ValueError(
            "The model output is not a simple classification vector. "
            "Its output format needs to be configured."
        )

    # Convert logits to probabilities when necessary
    if (
        np.any(predictions < 0)
        or not np.isclose(np.sum(predictions), 1.0, atol=0.01)
    ):
        exp_values = np.exp(
            predictions - np.max(predictions)
        )
        predictions = exp_values / np.sum(exp_values)

    if labels is None:
        labels = [
            f"Class {i}"
            for i in range(len(predictions))
        ]

    if len(labels) != len(predictions):
        raise ValueError(
            f"Model returned {len(predictions)} predictions, "
            f"but the labels file contains {len(labels)} labels. "
            "Please correct the labels file."
        )

    ranked = np.argsort(predictions)[::-1]

    return [
        (labels[index], float(predictions[index]))
        for index in ranked[:3]
    ]


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:
    st.header("About EcoSort AI")

    st.write(
        "EcoSort AI helps users understand waste categories "
        "and make better recycling and disposal decisions."
    )

    st.markdown("---")

    st.subheader("Supported waste guidance")

    st.write(
        "♻️ Plastic\n\n"
        "📄 Paper and cardboard\n\n"
        "🍾 Glass\n\n"
        "🥫 Metal\n\n"
        "🍃 Organic waste\n\n"
        "🔋 Batteries and electronic waste"
    )

    st.markdown("---")

    st.caption("EcoSort AI | Smart Waste Management")


# ==========================================
# MAIN APPLICATION
# ==========================================

if model_path is None:

    st.error("ONNX model file not found.")

    st.info(
        "Place your trained model at "
        "`Model/waste_model.onnx` or "
        "`model/waste_model.onnx`."
    )

    st.warning(
        "Image classification will become available "
        "after the trained model is added."
    )

else:

    try:
        session = load_model(model_path)
        labels = load_labels()

        st.success("AI model loaded successfully.")

        uploaded_file = st.file_uploader(
            "Upload a waste image",
            type=["jpg", "jpeg", "png", "webp"]
        )

        if uploaded_file:

            image = Image.open(uploaded_file)

            col1, col2 = st.columns(2)

            with col1:
                st.image(
                    image,
                    caption="Uploaded Waste Image",
                    use_container_width=True
                )

            with col2:
                st.subheader("Image Information")
                st.write(f"File name: {uploaded_file.name}")
                st.write(f"Image size: {image.size}")

            if st.button(
                "Identify Waste",
                type="primary",
                use_container_width=True
            ):

                with st.spinner("Analysing waste image..."):

                    predictions = classify_image(
                        session,
                        image,
                        labels
                    )

                best_label, confidence = predictions[0]

                guidance = get_guidance(best_label)

                st.markdown("---")
                st.header("Classification Results")

                st.success(
                    f"Predicted category: {guidance['category']}"
                )

                st.metric(
                    "Model confidence",
                    f"{confidence * 100:.2f}%"
                )

                st.progress(
                    max(0.0, min(1.0, confidence))
                )

                st.subheader("♻️ Recycling Recommendations")

                st.write(
                    f"**Advice:** {guidance['advice']}"
                )

                st.write(
                    f"**Recommended action:** {guidance['action']}"
                )

                st.write(
                    f"**Environmental benefit:** {guidance['impact']}"
                )

                st.markdown("---")

                st.subheader("Other Model Predictions")

                for label, score in predictions[1:]:
                    st.write(
                        f"• {label}: {score * 100:.2f}%"
                    )

                st.caption(
                    "Predictions are model estimates, not guaranteed "
                    "identifications. Confirm uncertain or hazardous "
                    "materials with an appropriate waste management professional."
                )

    except Exception as error:
        st.error("The application encountered an error.")

        st.code(str(error))

        st.info(
            "Check that the ONNX model, its input dimensions, "
            "preprocessing requirements and class labels are correct."
        )


# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.markdown(
    "<div style='text-align:center;'>"
    "♻️ <b>EcoSort AI</b> | Building a Cleaner and Greener Future"
    "</div>",
    unsafe_allow_html=True
)