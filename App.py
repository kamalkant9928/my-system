import streamlit as st
import pickle
import numpy as np

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("📊 Simple ML Model (Pass/Fail Prediction)")

# User input
hours = st.number_input("Enter hours studied:", min_value=0.0, max_value=24.0)

# Prediction
if st.button("Predict"):
    input_data = np.array([[hours]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ You will PASS")
    else:
        st.error("❌ You will FAIL")