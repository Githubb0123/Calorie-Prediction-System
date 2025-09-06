import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("calorie_model.pkl")

st.title("🔥 Calories Burned Predictor")

# Input fields
gender = st.selectbox("Gender", [0, 1])
age = st.number_input("Age", min_value=1, max_value=100, value=25)
height = st.number_input("Height (cm)", min_value=50, max_value=250, value=170)
weight = st.number_input("Weight (kg)", min_value=20, max_value=200, value=70)
duration = st.number_input("Duration (min)", min_value=1, max_value=300, value=30)
heart_rate = st.number_input("Heart Rate", min_value=40, max_value=200, value=100)
body_temp = st.number_input("Body Temperature (°C)", min_value=30.0, max_value=45.0, value=37.0)

if st.button("Predict Calories"):
    inputs = np.array([gender, age, height, weight, duration, heart_rate, body_temp]).reshape(1, -1)
    prediction = model.predict(inputs)[0]
    st.success(f"Estimated Calories Burned: {prediction:.2f}")