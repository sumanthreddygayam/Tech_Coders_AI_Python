from flask import Flask, render_template, request
import pickle
import os
import numpy as np

app = Flask(__name__)

# Absolute path (important for EC2/Linux)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "model", "model.pkl")

# Load model once
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Read inputs safely (defaults prevent empty-field crashes)
        posted_by = int(request.form.get("posted_by", 0))
        under_construction = int(request.form.get("under_construction", 0))
        rera = int(request.form.get("rera", 0))
        bhk_no = int(request.form.get("bhk_no", 0))
        bhk_or_rk = int(request.form.get("bhk_or_rk", 0))
        square_ft = float(request.form.get("square_ft", 0))
        ready_to_move = int(request.form.get("ready_to_move", 0))
        resale = int(request.form.get("resale", 0))
        longitude = float(request.form.get("longitude", 0))
        latitude = float(request.form.get("latitude", 0))

        # Feature order MUST match training
        features = np.array([[
            posted_by,
            under_construction,
            rera,
            bhk_no,
            bhk_or_rk,
            square_ft,
            ready_to_move,
            resale,
            longitude,
            latitude
        ]])

        prediction = model.predict(features)[0]

        return render_template(
            "index.html",
            prediction=round(float(prediction), 2)
        )

    except Exception as e:
        # Show error clearly instead of silent 500
        return f"Prediction Error: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
