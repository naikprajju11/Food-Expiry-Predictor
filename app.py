import streamlit as st
import pandas as pd
import joblib

# Page config
st.set_page_config(page_title="🥛 Strong Food Expiry Predictor", layout="centered")

# Header
st.markdown("""
<div style="text-align:center; padding:10px; background-color:#FFD966; border-radius:10px">
    <h1>🥛 Food Expiry Predictor</h1>
    <p>Predict food spoilage based on real-world conditions</p>
</div>
""", unsafe_allow_html=True)

# Load model
try:
    model = joblib.load("strong_food_model.pkl")
except FileNotFoundError:
    st.error("❌ Model not found! Run train_strong_model.py first.")
    st.stop()

# -----------------------------
# DYNAMIC INPUTS BASED ON STORAGE
# -----------------------------

st.markdown("### 🍱 Enter Food Details")

col1, col2 = st.columns(2)

with col1:
    food_type = st.selectbox("Food Type", ["Dairy", "Fruit", "Bakery", "Vegetable"])
    storage = st.selectbox("Storage", ["Fridge", "Room", "Freezer"])
    packaging = st.selectbox("Packaging", ["Sealed", "Open"])

with col2:
    # Dynamic temperature ranges
    if storage == "Fridge":
        temperature = st.slider("Temperature (°C)", 2, 10, 5)
    elif storage == "Room":
        temperature = st.slider("Temperature (°C)", 18, 35, 25)
    else:  # Freezer
        temperature = st.slider("Temperature (°C)", -20, 0, -5)

    humidity = st.slider("Humidity (%)", 10, 100, 50)
    age = st.slider("Age (days since production)", 0, 30, 1)

st.markdown("---")

# Predict button
if st.button("Predict Expiry"):
    input_df = pd.DataFrame([[food_type, storage, packaging, temperature, humidity, age]],
                            columns=['Type','Storage','Packaging','Temperature','Humidity','Age'])

    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.markdown("""
        <div style="text-align:center; padding:20px; background-color:#FF6F61; color:white; border-radius:10px;">
            ❌ <b>This food item is likely EXPIRED!</b><br>
            (Based on storage conditions & spoilage patterns)
        </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown("""
        <div style="text-align:center; padding:20px; background-color:#6FCF97; color:white; border-radius:10px;">
            ✅ <b>This food item is SAFE to consume</b><br>
            (Storage & conditions look normal)
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align:center; margin-top:30px; font-size:12px; color:gray;">
    Made with ❤️ using Python, Streamlit & Machine Learning
</div>
""", unsafe_allow_html=True)
