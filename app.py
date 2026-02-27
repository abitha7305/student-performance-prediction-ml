from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Load Model
model_path = os.path.join(os.path.dirname(__file__), "student_model.pkl")
model = joblib.load(model_path)

# Load Dataset for VLE Lookup
vle_path = os.path.join(os.path.dirname(__file__), "studentVle.csv")
studVle = pd.read_csv(vle_path)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        student_id = int(request.form["student_id"])
        prev_attempts = int(request.form["prev_attempts"])
        scores_input = request.form["scores"]
        scores = [float(s.strip()) for s in scores_input.split(",")]

        # Dynamic Calculations
        weighted_grade = sum(scores) / len(scores)
        pass_rate = sum(1 for s in scores if s >= 40) / len(scores)
        
        student_activity = studVle[studVle["id_student"] == student_id]
        if student_activity.empty:
            return render_template("index.html", error="Student ID not found.")
        sum_click = student_activity["sum_click"].sum()

        # Prepare Features and Predict
        features = np.array([[prev_attempts, weighted_grade, pass_rate, sum_click]])
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0][1] * 100

        return render_template(
            "index.html",
            prediction_text="PASS" if prediction == 1 else "FAIL / AT RISK",
            probability_text=f"{probability:.2f}%",
            average=f"{weighted_grade:.2f}",
            pass_rate=f"{pass_rate:.2f}",
            activity=sum_click,
            color="green" if prediction == 1 else "red"
        )
    except Exception as e:
        return render_template("index.html", error=str(e))

if __name__ == "__main__":
    app.run(debug=True)