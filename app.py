import random
from flask import Flask, request, jsonify

REG_NO = "FA24-BSE-113"
SEED = REG_NO   # change to 113 if instructor says numeric roll number

random.seed(SEED)
a1 = random.uniform(-5, 5)
a2 = random.uniform(-5, 5)
a3 = random.uniform(-5, 5)
b = random.uniform(-10, 10)

app = Flask(__name__)

@app.route("/predict")
def predict():
    try:
        x1 = float(request.args["x1"])
        x2 = float(request.args["x2"])
        x3 = float(request.args["x3"])
    except (KeyError, ValueError):
        return jsonify(error="Provide numeric x1, x2, x3"), 400
    y = a1 * x1 + a2 * x2 + a3 * x3 + b
    return jsonify({"registration number": REG_NO, "prediction": round(y, 2)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
