🥛 AI Food Expiry Prediction System

A machine learning–powered application that predicts whether a food item is Expired or Safe to Consume based on multiple real-world factors like food type, storage condition, temperature, humidity, and age.

Built with Python, Scikit-Learn, Streamlit, and Joblib.

🚀 Project Overview

This AI application uses a trained Machine Learning model to estimate spoilage likelihood.
Instead of relying on fixed dates or rules, the model learns from real data and predicts spoilage like a human would.

✔ Key Features

Intelligent expiry prediction using ML

Supports multiple food categories (Dairy, Fruits, Vegetables, Bakery)

Considers temperature, humidity, age, storage type, packaging

Simple web UI built using Streamlit

Fast inference using joblib-loaded ML model

Fully offline — no internet required

🧠 How It Works
1️⃣ Data Preparation

A custom dataset is created with realistic spoilage patterns.

2️⃣ Model Training

A machine learning model (Random Forest) is trained using:

Food Type

Storage

Packaging

Temperature

Humidity

Age

The trained model is saved using:

joblib.dump(model, "strong_food_model.pkl")

3️⃣ Deployment with Streamlit

The UI collects user inputs and sends them to the model for prediction.

🛠️ Technologies Used
Component	Technology
Machine Learning	Scikit-Learn
Model Storage	Joblib
Frontend UI	Streamlit
Language	Python
IDE	VS Code / PyCharm
📂 Project Structure
📁 Food-Expiry-AI
│
├── train_strong_model.py      # ML model training script
├── app.py                     # Streamlit UI
├── strong_food_model.pkl      # Saved AI model
├── README.md                  # Project documentation
└── requirements.txt           # Dependencies

▶️ How to Run the Project
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Train the AI model
python train_strong_model.py

3️⃣ Run the Streamlit App
streamlit run app.py

🖥️ User Interface (Streamlit)

The UI allows the user to select:

Food Type

Storage Method

Packaging

Temperature

Humidity

Age of Food

Then the model predicts:

✔ Safe

or

❌ Expired
🤖 Why This Is an AI Project

Uses a trained machine learning model

Learns spoilage patterns instead of using fixed rules

Makes intelligent predictions based on multiple inputs

Real-world simulation of food shelf-life estimation

This makes it a valid AI/ML project for interviews and resumes.

📌 Possible Enhancements

Add real grocery datasets

Add expiry prediction in hours instead of days

Add mobile app version

Add API (Flask/FastAPI) for integration

Add QR-code scanning for packaged foods

🏁 Conclusion

This project demonstrates how AI and ML can be used to predict real-world food spoilage. It is simple, fast, and accurate — perfect for students, beginners, and AI/ML portfolio building.
