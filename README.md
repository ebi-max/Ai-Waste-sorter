# ♻️ EcoSort AI – Smart Waste Classification Assistant

**EcoSort AI** is an AI-powered waste classification project designed to help individuals, communities and environmental organisations understand waste categories and make more informed recycling and disposal decisions.

The project combines machine learning, image processing and environmental guidance to support responsible waste management.

## 🌍 Project Overview

Improper waste disposal contributes to environmental pollution, blocked drainage systems and public health challenges.

EcoSort AI aims to make waste identification easier by allowing users to upload an image and receive a predicted waste category, together with practical recycling and disposal recommendations.

## ✨ Key Features

- 📸 Waste image upload.
- 🤖 AI-powered image classification using ONNX Runtime.
- ♻️ Waste category identification.
- 📊 Prediction confidence display.
- 🗑️ Recycling and disposal recommendations.
- 🌱 Environmental awareness and education.
- 📱 Simple, interactive Streamlit interface.

**Note:** Classification requires a compatible trained ONNX model and its corresponding class-label file.

## 🧪 Supported Waste Guidance

EcoSort AI includes guidance for the following waste categories:

| Waste Category | Recommended Action |
|---|---|
| Plastic | Separate and recycle suitable plastics. |
| Paper | Reuse or recycle clean paper. |
| Cardboard | Flatten and recycle dry cardboard. |
| Glass | Reuse or send to a glass recycling facility. |
| Metal | Separate recyclable metal materials. |
| Organic | Compost suitable biodegradable materials. |
| Food Waste | Reduce food waste and compost suitable scraps. |
| Batteries | Use authorised hazardous-waste collection points. |

Actual classification categories depend on the trained model and its labels.

## 🛠️ Technology Stack

- Python
- Streamlit
- NumPy
- Pillow
- ONNX Runtime
- Machine Learning

## 📂 Project Structure

```text
Ai-Waste-sorter/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── Model/
│   ├── waste_model.onnx
│   └── labels.txt
│
└── SKILL.md