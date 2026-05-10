import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

try:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": "Explain regulatory inspection in one sentence."
            }
        ],
        temperature=0.3,
        max_tokens=50
    )

    print("\n AI Response:\n")
    print(response.choices[0].message.content)

except Exception as e:
    print(" Error:", e)