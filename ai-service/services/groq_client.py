import os
import time
import logging
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def call_groq(prompt):

    retries = 3

    for attempt in range(retries):

        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3,
                max_tokens=300
            )

            content = response.choices[0].message.content

            return {
                "success": True,
                "response": content
            }

        except Exception as e:

            logging.error(f"Attempt {attempt+1} failed: {e}")

            if attempt < retries - 1:
                time.sleep(2 ** attempt)

    return {
        "success": False,
        "response": "AI service unavailable"
    }