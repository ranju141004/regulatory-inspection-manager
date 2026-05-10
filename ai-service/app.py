from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from services.security import sanitize_input

app = Flask(__name__)

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["30 per minute"]
)

limiter.init_app(app)

@app.route("/")
def home():
    return {
        "message": "AI Service Running Successfully"
    }

@app.route("/test", methods=["POST"])
def test():

    data = request.get_json()

    text = data.get("text", "")

    if not text.strip():

        return jsonify({
            "success": False,
            "content": None,
            "is_fallback": False,
            "error": "Empty input not allowed"
        }), 400

    sanitized = sanitize_input(text)

    if sanitized is None:

        return jsonify({
            "success": False,
            "content": None,
            "is_fallback": False
        }), 400

    return jsonify({
        "success": True,
        "content": sanitized,
        "is_fallback": False
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)