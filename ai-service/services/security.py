import bleach

BLOCKED_WORDS = [
    "ignore previous instructions",
    "system prompt",
    "bypass",
    "hack"
]

def sanitize_input(text):

    cleaned = bleach.clean(text, tags=[], strip=True)

    lower_text = cleaned.lower()

    for word in BLOCKED_WORDS:
        if word in lower_text:
            return None

    return cleaned