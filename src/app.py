from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/tip", methods=["POST"])
def calculate_tip():
    data = request.get_json()

    # Validate JSON
    if not data or "total_bill" not in data or "tip" not in data:
        return jsonify({"error": "total_bill and tip are required"}), 400

    total_bill = data["total_bill"]
    tip = data["tip"]

    # Validate numbers
    try:
        total_bill = float(total_bill)
        tip = float(tip)
    except:
        return jsonify({"error": "total_bill and tip must be numeric"}), 400

    if total_bill <= 0:
        return jsonify({"error": "total_bill must be greater than 0"}), 400

    tip_pct = tip / total_bill

    return jsonify({
        "total_bill": total_bill,
        "tip": tip,
        "tip_pct": tip_pct
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
