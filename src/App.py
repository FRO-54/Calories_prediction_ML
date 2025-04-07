# src/predict_app.py

import streamlit as st
import pickle
import numpy as np

# Load model
with open('./models/xgboost_calorie_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.set_page_config(page_title="Calories Burnt Predictor", layout="centered")

st.title("🔥 Calories Burnt Prediction App")
st.markdown("Enter your details below to predict how many calories you’ll burn.")

# Input form
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.slider("Age", 10, 80, 25)
height = st.slider("Height (cm)", 100, 220, 170)
weight = st.slider("Weight (kg)", 30, 150, 70)
duration = st.slider("Duration (minutes)", 1, 300, 60)
heart_rate = st.slider("Heart Rate", 60, 200, 100)
body_temp = st.slider("Body Temperature (°C)", 35.0, 42.0, 37.5)

# Convert gender to numeric
gender_numeric = 0 if gender.lower() == "male" else 1

# Predict button
if st.button("Predict Calories Burnt"):
    input_data = np.array([[gender_numeric, age, height, weight, duration, heart_rate, body_temp]])
    prediction = model.predict(input_data)
    st.success(f"🔥 Estimated Calories Burnt: **{prediction[0]:.2f}** kcal")
