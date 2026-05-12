from flask import Flask, request, jsonify
from services.groq_client import call_groq, MODEL

app = Flask(__name__)

@app.after_request
def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    response.headers["Referrer-Policy"] = "no-referrer"
    return response

# ---------------------------------------------------
# HOME ENDPOINT
# ---------------------------------------------------

@app.route("/", methods=["GET"])
def home():

    return {
        "message": "AI Service Running"
    }, 200


# ---------------------------------------------------
# HEALTH ENDPOINT
# ---------------------------------------------------

@app.route("/health", methods=["GET"])
def health():

    return {
        "status": "healthy",
        "model": MODEL,
        "uptime": "running"
    }, 200


# ---------------------------------------------------
# DESCRIBE ENDPOINT
# ---------------------------------------------------

@app.route("/describe", methods=["POST"])
def describe():

    data = request.get_json()

    if not data or "input_text" not in data:
        return jsonify({
            "error": "input_text is required"
        }), 400

    input_text = data["input_text"]

    # Empty input validation
    if not input_text.strip():
        return jsonify({
            "error": "Input cannot be empty"
        }), 400

    # Large payload validation
    if len(input_text) > 5000:
        return jsonify({
            "error": "Payload too large"
        }), 400

    # Prompt injection detection
    blocked_phrases = [
        "ignore previous instructions",
        "reveal system prompt",
        "bypass security"
    ]

    for phrase in blocked_phrases:
        if phrase.lower() in input_text.lower():
            return jsonify({
                "error": "Prompt injection detected"
            }), 400

    result = call_groq(input_text)

    return jsonify(result), 200


# ---------------------------------------------------
# RECOMMEND ENDPOINT
# ---------------------------------------------------

@app.route("/recommend", methods=["POST"])
def recommend():

    data = request.get_json()

    if not data or "input_text" not in data:
        return jsonify({
            "error": "input_text is required"
        }), 400

    result = call_groq(data["input_text"])

    return jsonify(result), 200


# ---------------------------------------------------
# GENERATE REPORT ENDPOINT
# ---------------------------------------------------

@app.route("/generate-report", methods=["POST"])
def generate_report():

    data = request.get_json()

    if not data or "input_text" not in data:
        return jsonify({
            "error": "input_text is required"
        }), 400

    result = call_groq(data["input_text"])

    return jsonify(result), 200


# ---------------------------------------------------
# MAIN
# ---------------------------------------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)