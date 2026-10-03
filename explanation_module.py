import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def explain_topic(topic: str) -> str:

    prompt = f"""
You are EduGenie, an educational AI assistant.

Explain the following topic in a simple and clear way for a student.

Topic:
{topic}

Include:

1. Simple definition
2. Easy explanation
3. Real-life example
4. Key points

Keep the explanation easy to understand.
"""

    try:

        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:

        print("\n========== GEMINI EXPLANATION ERROR ==========")
        print(type(e).__name__)
        print(str(e))
        print("===============================================\n")

        return f"Gemini Error: {str(e)}"