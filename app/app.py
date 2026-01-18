from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    posted_by = int(request.form["posted_by"])
    under_construction = int(request.form["under_construction"])
    rera = int(request.form["rera"])
    bhk_no = int(request.form["bhk_no"])
    bhk_or_rk = int(request.form["bhk_or_rk"])
    square_ft = float(request.form["square_ft"])
    ready_to_move = int(request.form["ready_to_move"])
    resale = int(request.form["resale"])
    longitude = float(request.form["longitude"])
    latitude = float(request.form["latitude"])

    # 🔒 DETERMINISTIC LOGIC (NO ML)
    base_price = square_ft * 0.06           # price per sq.ft (lakhs logic)
    bhk_factor = bhk_no * 5
    location_factor = (latitude + longitude) % 10
    rera_bonus = 5 if rera == 1 else 0
    resale_penalty = -3 if resale == 1 else 0

    predicted_price = (
        base_price
        + bhk_factor
        + location_factor
        + rera_bonus
        + resale_penalty
    )

    # Ensure non-negative
    predicted_price = max(predicted_price, 10)

    return render_template(
        "index.html",
        prediction=round(predicted_price, 2)
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
