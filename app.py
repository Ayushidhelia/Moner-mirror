from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend requests

@app.route("/")
def home():
    return jsonify({"message": "Finance Advisor API running successfully!"})

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    income = data.get("income", 0)
    expenses = data.get("expenses", 0)
    savings_rate = data.get("savings_rate", 0)
    categories = data.get("categories", {})

    suggestions = []

    # --- Financial insights ---
    if savings_rate > 30:
        suggestions.append("💰 Excellent savings rate! Keep investing consistently.")
    elif 10 <= savings_rate <= 30:
        suggestions.append("⚖️ Good balance, but consider increasing your savings rate to over 30%.")
    else:
        suggestions.append("🚨 Low savings rate! Try cutting unnecessary expenses.")

    # --- Expense analysis ---
    for category, percent in categories.items():
        if percent > 40:
            suggestions.append(f"⚠️ You're spending {percent}% on {category}. Try reducing it.")
        elif percent < 10:
            suggestions.append(f"✅ {category} spending is under control.")

    # --- Income/Expense advice ---
    if expenses > income:
        suggestions.append("🔴 You're spending more than you earn. Reevaluate your monthly budget.")
    else:
        suggestions.append("🟢 You're earning more than you spend — great job!")

    return jsonify({"suggestions": suggestions})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
