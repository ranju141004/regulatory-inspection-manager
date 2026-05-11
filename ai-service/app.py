from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from services.security import sanitize_input

# Create Flask app
app = Flask(__name__)

# Configure CORS
CORS(app, resources={
    r"/*": {
        "origins": ["http://localhost"]
    }
})

# Configure rate limiter
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["30 per minute"]
)

limiter.init_app(app)


# Security headers
@app.after_request
def add_security_headers(response):

    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"

    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; "
        "script-src 'self'; "
        "style-src 'self'; "
        "img-src 'self' data:; "
        "font-src 'self'; "
        "connect-src 'self'; "
        "frame-ancestors 'none'; "
        "base-uri 'self'; "
        "form-action 'self'"
    )

    response.headers["Referrer-Policy"] = "no-referrer"

    response.headers["Server"] = "SecureServer"

    return response


# Home route
@app.route("/")
def home():
    return jsonify({
        "message": "AI Service Running Successfully"
    })


# Test route
@app.route("/test", methods=["POST"])
def test():

    data = request.get_json()

    # Validate JSON body
    if not data:
        return jsonify({
            "success": False,
            "content": None,
            "is_fallback": False,
            "error": "No JSON body provided"
        }), 400

    text = data.get("text", "")

    # Empty input validation
    if not text.strip():
        return jsonify({
            "success": False,
            "content": None,
            "is_fallback": False,
            "error": "Empty input not allowed"
        }), 400

    # Input size validation
    if len(text) > 5000:
        return jsonify({
            "success": False,
            "content": None,
            "is_fallback": False,
            "error": "Input too large"
        }), 400

    # Sanitize input
    sanitized = sanitize_input(text)

    # Injection detection
    if sanitized is None:
        return jsonify({
            "success": False,
            "content": None,
            "is_fallback": False,
            "error": "Malicious input detected"
        }), 400

    return jsonify({
        "success": True,
        "content": sanitized,
        "is_fallback": False
    })


# Run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)