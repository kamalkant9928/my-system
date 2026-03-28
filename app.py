import streamlit as st
import numpy as np
from sklearn.linear_model import LogisticRegression

st.title("📊 Simple ML Model (Pass/Fail Prediction)")

# -----------------------------
# Step 1: Train model on the fly
# -----------------------------
X = np.array([[1], [2], [3], [4], [5], [6]])  # Features
y = np.array([0, 0, 0, 1, 1, 1])             # Target: Fail(0)/Pass(1)

model = LogisticRegression()
model.fit(X, y)

# -----------------------------
# Step 2: User input
# -----------------------------
hours = st.number_input("Enter hours studied:", min_value=0.0, max_value=24.0)

# -----------------------------
# Step 3: Predict button
# -----------------------------
if st.button("Predict"):
    input_data = np.array([[hours]])
    prediction = model.predict(input_data)
    prob = model.predict_proba(input_data)

    st.write(f"Confidence of passing: {prob[0][1]*100:.2f}%")

    if prediction[0] == 1:
        st.success("✅ You will PASS")
    else:
        st.error("❌ You will FAIL")