from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
from middleware.security import sanitize_input

describe_bp = Blueprint("describe", __name__)

@describe_bp.route("/describe", methods=["POST"])
def describe():

    data = request.get_json()

    user_input = data.get("input_text")

    text = sanitize_input(user_input)

    if not text:
        return jsonify({
            "error": "Prompt injection detected"
        }), 400

    response = call_groq(text)

    return jsonify(response)