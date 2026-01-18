from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    features = [
        int(request.form["posted_by"]),
        int(request.form["under_construction"]),
        int(request.form["rera"]),              # ✅ NEW
        int(request.form["bhk_no"]),
        int(request.form["bhk_or_rk"]),
        float(request.form["square_ft"]),
        int(request.form["ready_to_move"]),
        int(request.form["resale"]),
        float(request.form["longitude"]),
        float(request.form["latitude"])
    ]

    prediction = model.predict([features])[0]

    return render_template(
        "index.html",
        prediction=round(prediction, 2)
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
