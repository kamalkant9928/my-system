import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Student Predictor", layout="centered")

 st.image("dashboard.webp", caption="Healthcare Dashboard UI", use_container_width=True)

# -----------------------------
# Login System
# -----------------------------
def login():
    st.title("🔐 Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state["logged_in"] = True
            st.success("Login Successful ✅")
        else:
            st.error("Invalid Credentials ❌")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login()
    st.stop()

# -----------------------------
# Custom CSS (Gradient UI)
# -----------------------------
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #74ebd5, #ACB6E5);
    }
    .main-title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #2c3e50;
    }
    .card {
        padding: 20px;
        border-radius: 15px;
        background-color: white;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# Title
# -----------------------------
st.markdown('<div class="main-title">📊 Student Pass/Fail Predictor</div>', unsafe_allow_html=True)

# -----------------------------
# Better Dataset (Realistic)
# -----------------------------
data = {
    "hours": [1,2,3,4,5,6,7,8,2.5,3.5,4.5,5.5,6.5,7.5],
    "pass":  [0,0,0,0,1,1,1,1,0,0,1,1,1,1]
}
df = pd.DataFrame(data)

X = df[["hours"]]
y = df["pass"]

model = LogisticRegression()
model.fit(X, y)

# -----------------------------
# Input
# -----------------------------
hours = st.number_input("📘 Enter hours studied:", min_value=0.0, max_value=24.0)

# -----------------------------
# Prediction
# -----------------------------
if st.button("🔍 Predict"):

    input_data = np.array([[hours]])
    prediction = model.predict(input_data)
    prob = model.predict_proba(input_data)

    confidence = prob[0][1] * 100

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write(f"### 📊 Passing Probability: {confidence:.2f}%")

    # -----------------------------
    # Running Animation (GIF)
    # -----------------------------
    st.image("https://media.giphy.com/media/xT0xeJpnrWC4XWblEk/giphy.gif", caption="Keep Running Towards Success 🏃‍♂️")

    if prediction[0] == 1:
        st.success("✅ You will PASS 🎉")
        st.image("https://images.unsplash.com/photo-1501004318641-b39e6451bec6",
                 caption="Success Garden 🌿", use_container_width=True)
    else:
        st.error("❌ You will FAIL")
        st.image("https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
                 caption="Hard Work Rock 🪨", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # -----------------------------
    # Graph (Probability vs Hours)
    # -----------------------------
    st.subheader("📈 Probability vs Study Hours")

    hours_range = np.linspace(0, 10, 100).reshape(-1,1)
    probs = model.predict_proba(hours_range)[:,1]

    fig, ax = plt.subplots()
    ax.plot(hours_range, probs)
    ax.set_xlabel("Hours Studied")
    ax.set_ylabel("Probability of Passing")
    ax.set_title("Study Hours vs Passing Probability")

    st.pyplot(fig)
