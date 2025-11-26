from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/tip", methods=["POST"])
def calculate_tip():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON body provided"}), 400

    total_bill = data.get("total_bill")
    tip_amount = data.get("tip")

    if not isinstance(total_bill, (int, float)) or not isinstance(tip_amount, (int, float)):
        return jsonify({"error": "total_bill and tip must be numbers"}), 400

    tip_pct = tip_amount / total_bill

    return jsonify({
        "total_bill": total_bill,
        "tip": tip_amount,
        "tip_pct": round(tip_pct, 4)
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
