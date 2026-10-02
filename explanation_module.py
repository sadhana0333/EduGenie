import os
from dotenv import load_dotenv
from google import genai


# Load environment variables
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)


def explain_topic(topic: str) -> str:
    """
    Explain a given topic in simple language using Gemini.
    """

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

        error_message = str(e)

        if "429" in error_message or "RESOURCE_EXHAUSTED" in error_message:
            return (
                "⚠️ Gemini API quota has been reached.\n\n"
                "Please try again after the quota resets."
            )

        return (
            "⚠️ Unable to connect to Gemini right now.\n\n"
            "Please try again later."
        )