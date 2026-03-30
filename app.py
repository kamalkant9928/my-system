import streamlit as st
import numpy as np
from sklearn.linear_model import LogisticRegression

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Student Result Predictor", layout="centered")

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
    <style>
    body {
        background-color: #f5f7fa;
    }
    .main-title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #2c3e50;
    }
    .sub-text {
        text-align: center;
        color: gray;
        margin-bottom: 20px;
    }
    .card {
        padding: 20px;
        border-radius: 15px;
        background-color: white;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# Title Section
# -----------------------------
st.markdown('<div class="main-title">📊 Student Pass/Fail Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Predict result based on study hours</div>', unsafe_allow_html=True)

# -----------------------------
# Step 1: Train model
# -----------------------------
X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([0, 0, 0, 1, 1, 1])

model = LogisticRegression()
model.fit(X, y)

# -----------------------------
# Step 2: Input
# -----------------------------
hours = st.number_input("📘 Enter hours studied:", min_value=0.0, max_value=24.0)

# -----------------------------
# Step 3: Prediction
# -----------------------------
if st.button("🔍 Predict Result"):

    input_data = np.array([[hours]])
    prediction = model.predict(input_data)
    prob = model.predict_proba(input_data)

    confidence = prob[0][1] * 100

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write(f"### 📊 Confidence of Passing: {confidence:.2f}%")

    if prediction[0] == 1:
        st.success("✅ You will PASS 🎉")

        # Good garden image
        st.image("https://images.unsplash.com/photo-1501004318641-b39e6451bec6", 
                 caption="Success Garden 🌿", use_container_width=True)

        st.success("🌟 Keep it up! Bright future ahead!")
    else:
        st.error("❌ You will FAIL")

        # Rock / hard life image
        st.image("https://images.unsplash.com/photo-1500530855697-b586d89ba3ee", 
                 caption="Hard Work Needed 🪨", use_container_width=True)

        st.warning("💪 Work harder! You can improve!")

    st.markdown('</div>', unsafe_allow_html=True)
