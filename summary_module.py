import os
import time
from dotenv import load_dotenv
from google import genai


# Load environment variables
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)


def summarize_text(text: str) -> str:
    """
    Summarize a long educational passage.
    """

    prompt = f"""
You are EduGenie, an educational summarization assistant.

Summarize the following passage.

Requirements:
- Keep the important information.
- Remove unnecessary repetition.
- Use simple and clear language.
- Make the summary suitable for students.
- Do not add information that is not present in the passage.

PASSAGE:

{text}
"""

    for attempt in range(3):

        try:
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt
            )

            return response.text.strip()

        except Exception as e:

            error_message = str(e)

            # Retry temporary 503 errors
            if "503" in error_message or "UNAVAILABLE" in error_message:

                if attempt < 2:
                    time.sleep(2)
                    continue

            return f"Error in summarization: {e}"

    return "Gemini is temporarily unavailable. Please try again."