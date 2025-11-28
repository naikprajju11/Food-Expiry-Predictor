import streamlit as st
import pandas as pd
import joblib
import os
from datetime import datetime

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="AI Food Expiry Predictor",
    layout="centered",
)

# -------------------------
# Header
# -------------------------
st.markdown("""
<div style="
    text-align:center; 
    padding:20px; 
    background-color:#f8e672; 
    border-radius:15px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
    <h1 style="color:#333;">🥛 AI Food Expiry Predictor</h1>
    <p style="font-size:16px; color:#444;">
        Smart ML-powered spoilage prediction + real-world data collection
    </p>
</div>
""", unsafe_allow_html=True)

# -------------------------
# Load Model
# -------------------------
try:
    model = joblib.load("strong_food_model.pkl")
except:
    st.error("❌ Model not found! Please run train_model.py first.")
    st.stop()

st.write("\n")

# -------------------------
# Input Mode Selection
# -------------------------
mode = st.radio(
    "Choose Input Type:",
    ["Predefined Food Types", "Custom (New Food Type)"],
    horizontal=True
)

st.markdown("---")

# -------------------------
# User Input Form
# -------------------------

st.markdown("### 🍱 Enter Food Details")

col1, col2 = st.columns(2)

with col1:
    if mode == "Predefined Food Types":
        food_type = st.selectbox("Food Type", ["Dairy", "Fruit", "Bakery", "Vegetable"])
    else:
        food_type = st.text_input("Enter Custom Food Type", placeholder="Example: Meat, Chips, Chocolate")

    storage = st.selectbox("Storage Method", ["Fridge", "Room", "Freezer", "Other"])
    packaging = st.selectbox("Packaging Type", ["Sealed", "Open", "Loose"])

with col2:

    # Dynamic slider based on storage
    if storage == "Fridge":
        temperature = st.slider("Temperature (°C)", 1, 12, 5)
    elif storage == "Freezer":
        temperature = st.slider("Temperature (°C)", -25, 0, -5)
    elif storage == "Room":
        temperature = st.slider("Temperature (°C)", 18, 40, 26)
    else:
        temperature = st.slider("Temperature (°C)", -10, 45, 25)

    humidity = st.slider("Humidity (%)", 10, 100, 50)
    age = st.slider("Age (days since production)", 0, 60, 1)

st.markdown("---")

# -------------------------
# Predict Button
# -------------------------

if st.button("🔍 Predict Expiry", use_container_width=True):

    # Create DataFrame
    input_df = pd.DataFrame([[food_type, storage, packaging, temperature, humidity, age]],
                            columns=['Type', 'Storage', 'Packaging', 'Temperature', 'Humidity', 'Age'])

    # Predict
    prediction = model.predict(input_df)[0]

    # Result Card
    if prediction == 1:
        st.markdown("""
        <div style="
            background-color:#ff6b6b; 
            color:white; 
            padding:20px; 
            border-radius:15px;
            text-align:center;
            box-shadow:0 4px 10px rgba(0,0,0,0.1);">
            <h2>❌ Food is Likely EXPIRED</h2>
            <p>Based on ML analysis of conditions & spoilage patterns</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="
            background-color:#51d88a; 
            color:white; 
            padding:20px; 
            border-radius:15px;
            text-align:center;
            box-shadow:0 4px 10px rgba(0,0,0,0.1);">
            <h2>✅ Food is SAFE to Consume</h2>
            <p>Storage & environment conditions seem normal</p>
        </div>
        """, unsafe_allow_html=True)

    # -------------------------
    # Save Data for Future Training
    # -------------------------
    input_df['Prediction'] = prediction
    input_df['Timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not os.path.exists("user_data.csv"):
        input_df.to_csv("user_data.csv", index=False)
    else:
        input_df.to_csv("user_data.csv", mode='a', header=False, index=False)

    st.info("📁 Your input has been saved for future AI training.")


# -------------------------
# Footer
# -------------------------
st.markdown("""
<div style='text-align:center; margin-top:40px; font-size:13px; color:gray;'>
    Made with ❤️ using Python, Streamlit & Machine Learning
</div>
""", unsafe_allow_html=True)
