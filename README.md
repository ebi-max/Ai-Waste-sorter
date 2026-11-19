♻️ EcoSort AI — AI-Powered Waste Sorting and Recycling Assistant

EcoSort AI is an AI-powered waste sorting and recycling assistant designed to help individuals, communities and environmental organisations identify common waste materials and make more informed recycling and disposal decisions.

Built with Python, Streamlit and MobileNetV2, EcoSort AI uses image classification to analyse uploaded waste images and provide predicted material categories alongside practical recycling and disposal guidance.

The project combines artificial intelligence, computer vision and environmental education to encourage responsible waste management.

🌍 Project Overview

Improper waste disposal contributes to environmental pollution, blocked drainage systems and public health challenges.

EcoSort AI addresses part of this challenge by allowing users to upload an image of a waste item, receive an AI-generated classification and access relevant disposal recommendations.

The application runs its trained image-classification model locally using ONNX Runtime.

✨ Key Features

- 📸 Waste image upload and analysis.
- 🤖 AI-powered waste classification using MobileNetV2.
- ♻️ Identification of six common waste categories.
- 📊 Prediction scores for model outputs.
- 🗑️ Practical recycling and disposal recommendations.
- 🌱 Environmental awareness and education.
- 📱 Interactive Streamlit interface.
- 🔒 Local image inference without sending uploaded images to an external image-classification API.

🧠 AI Model

EcoSort AI uses a MobileNetV2 image-classification model trained through transfer learning with the TrashNet dataset.

The trained TensorFlow model was exported to ONNX format and verified using ONNX Runtime.

Model specifications:

Specification| Details
Architecture| MobileNetV2
Training approach| Transfer learning
Dataset| TrashNet
Input dimensions| 128 × 128 × 3
Input format| RGB
Deployment format| ONNX
Inference engine| ONNX Runtime
Classification outputs| 6

Supported AI Classification Categories

1. Cardboard
2. Glass
3. Metal
4. Paper
5. Plastic
6. Trash

Model Evaluation Results

The model was evaluated on a held-out test set of 380 images.

Evaluation Metric| Result
Test accuracy| 80%
Macro F1-score| 0.77
Weighted F1-score| 0.80
Test images| 380

These results represent performance on the TrashNet test split. Real-world performance may vary with image quality, lighting, backgrounds and waste-item conditions.

The model's prediction score should not be interpreted as a guarantee of correct identification.

♻️ Recycling and Disposal Guidance

Beyond its six AI classification categories, EcoSort AI provides general educational guidance covering additional waste-management concerns.

Category| Recommended Action
Plastic| Separate suitable plastics and check local recycling requirements.
Paper| Keep paper clean and dry for reuse or recycling.
Cardboard| Flatten and recycle dry cardboard.
Glass| Handle broken glass carefully and use suitable collection facilities.
Metal| Separate recyclable metal materials.
Organic Waste| Compost suitable biodegradable materials.
Food Waste| Reduce food waste and compost suitable scraps.
Batteries| Use authorised battery and electronic-waste collection points.

Important: Organic waste, food waste and batteries are currently covered by educational guidance, not the six-class image-classification model.

🛠️ Technology Stack

- Python
- TensorFlow
- MobileNetV2
- ONNX
- ONNX Runtime
- Streamlit
- NumPy
- Pillow
- Google Colab
- GitHub

📂 Project Structure

Ai-Waste-sorter/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── Model/
│   ├── waste_model.onnx
│   ├── labels.txt
│   └── metadata.json
│
└── SKILL.md

🚀 Installation and Usage

1. Clone the repository

git clone https://github.com/ebi-max/Ai-Waste-sorter.git

2. Enter the project directory

cd Ai-Waste-sorter

3. Install dependencies

pip install -r requirements.txt

4. Run EcoSort AI

streamlit run app.py

5. Classify waste

- Open the Streamlit application.
- Upload a supported waste image.
- Select Identify waste.
- Review the predicted category and model score.
- Read the recycling and disposal recommendations.

🌱 Environmental Impact

EcoSort AI aims to contribute to:

- Improved waste identification and sorting awareness.
- More responsible recycling practices.
- Environmental education within communities.
- Increased awareness of waste reduction and reuse.
- Responsible handling of potentially hazardous waste.

⚠️ Limitations

- The model currently recognises six waste categories.
- Its training dataset is relatively small and may not represent every real-world waste condition.
- Test accuracy does not guarantee the same performance in everyday environments.
- Prediction scores are not calibrated guarantees of correctness.
- Users should follow local waste-management regulations and authorised hazardous-waste disposal procedures.

🔮 Future Development

Potential improvements include:

- Expanding the training dataset with locally sourced waste images.
- Improving classification performance, especially for the trash category.
- Adding more waste categories.
- Introducing waste-sorting tutorials and interactive learning.
- Exploring community-based recycling awareness features.
- Improving accessibility for mobile users.

👨‍💻 Developer

Ebieme Bassey

GitHub: https://github.com/ebi-max

Project: https://github.com/ebi-max/Ai-Waste-sorter

---

EcoSort AI — Building a cleaner and greener future through artificial intelligence.
