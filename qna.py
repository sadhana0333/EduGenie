import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def answer_question_with_gemini(question: str) -> str:

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=f"""
You are EduGenie, an educational AI assistant.

Answer this question clearly and simply for a student:

{question}
"""
        )

        return response.text.strip()

    except Exception as e:

        error = str(e)

        if "429" in error or "RESOURCE_EXHAUSTED" in error:
            return (
                "⚠️ Gemini API quota has been reached.\n\n"
                "Please wait until the quota resets and try again."
            )

        return (
            "⚠️ Unable to connect to Gemini right now.\n\n"
            "Please try again later."
        )