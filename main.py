from fastapi import FastAPI
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

app = FastAPI()

# -----------------------------
# Train Model (same as app.py)
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
# Home Route
# -----------------------------
@app.get("/")
def home():
    return {
        "message": "🎓 Student Pass/Fail Prediction API is running"
    }

# -----------------------------
# Predict API
# -----------------------------
@app.get("/predict")
def predict(hours: float):

    input_data = np.array([[hours]])
    prediction = model.predict(input_data)
    prob = model.predict_proba(input_data)

    return {
        "hours_studied": hours,
        "passing_probability": round(float(prob[0][1]) * 100, 2),
        "result": "PASS 🎉" if prediction[0] == 1 else "FAIL ❌"
    }

# -----------------------------
# Graph Data API (for frontend)
# -----------------------------
@app.get("/graph")
def graph():

    hours_range = np.linspace(0, 10, 100).reshape(-1,1)
    probs = model.predict_proba(hours_range)[:,1]

    return {
        "hours": hours_range.flatten().tolist(),
        "probability": probs.tolist()
    }
