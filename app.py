import streamlit as st
import os

st.title("🗑️ Offline Waste AI")

model_path = "model/waste_model.onnx"

if not os.path.exists(model_path):
    st.error("❌ Model file missing. Please add: model/waste_model.onnx")
    st.stop()

st.success("Model found. Ready to run.")