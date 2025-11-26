AI WASTE SORTER

AI Waste Sorter is an open-source machine learning tool that classifies waste from images to support recycling and sustainability. Built for the Loubby AI Hackathon, it includes a Streamlit app, trained model, and all files required for testing and deployment.



🌍 PROJECT OVERVIEW

AI Waste Sorter is an AI-powered environmental solution that uses deep learning to automatically classify waste into categories such as plastic, paper, metal, glass, and organic.
It promotes recycling, reduces landfill pressure, and supports clean, sustainable waste management practices.

This project is fully open-source and structured to meet all Loubby AI Hackathon submission requirements.



🚀 FEATURES

♻️ AI waste classification using a trained ML model
📷 Upload or capture images for instant prediction
🌐 Streamlit web interface for easy interaction
📁 Organized, open-source repo with models and assets
📄 MIT License for open reuse
🌱 Built for Environment & Sustainability Track



📁 PROJECT STRUCTURE

/ai-waste-sorter
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── /models
│   └── waste_classifier.h5
└── /assets
    └── icons, sample images, etc.



🧠 HOW IT WORKS

1. User uploads a waste image


2. The image is preprocessed into the format the model expects


3. The ML model predicts the waste category


4. The result is returned with confidence level and recycling guidance




📦 INSTALLATION & SETUP

1. Clone the repository:


git clone https://github.com/ebi-max/ai-waste-sorter.git
cd ai-waste-sorter

2. Install dependencies:


pip install -r requirements.txt

3. Run the app:


streamlit run app.py


🌐 DEPLOYMENT (Streamlit Cloud)

1. Push your repo to GitHub


2. Go to Streamlit Cloud


3. Connect your GitHub repository


4. Select app.py and deploy


Live App URL for Hackathon Submission: https://ai-waste-sorter.stream
YouTube Demo URL: https://youtube.com/shorts/RJam4XtU1-o?si=FyQDpRdk36TiSN_W


🧪 MODEL DETAILS

Framework: TensorFlow / Keras

Type: CNN image classifier

Trained on: curated dataset of waste categories

Output classes:

Plastic

Paper

Metal

Glass

Organic




📈 USE CASES

Waste sorting centers

Environmental agencies

Schools/universities

Smart city dashboards

Household recycling

NGOs promoting sustainability



📝 HACKATHON COMPLIANCE CHECKLIST

REQUIREMENT	STATUS

Public GitHub repo	✔️
Open-source license	✔️ MIT
Public hosted URL	✔️ Live App
Demo video	⏳ To record
Source code included	✔️
Clear README	✔️ Done
Category specified	✔️ Environment & Sustainability



📄 LICENSE

This project is licensed under the MIT License.
You are free to use, modify, and distribute it.



🤝 CONTRIBUTING

Contributions are welcome!
Feel free to open issues or submit pull requests.


👤 AUTHOR

EBIEME BASSEY
Built for the Loubby AI Hackathon
GitHub: https://github.com/ebi-max

Live App URL: https://ai-waste-sorter.stream
YouTube Demo URL: https://youtube.com/shorts/RJam4XtU1-o?si=FyQDpRdk36TiSN_W

