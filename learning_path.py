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


def get_learning_recommendations(topic: str) -> str:
    """
    Generate a personalized learning path for a topic.
    """

    prompt = f"""
You are EduGenie, a personalized learning assistant.

Create a structured learning path for:

Topic: {topic}

Organize the learning path from beginner to advanced.

For each stage include:

1. Topic or concept
2. Difficulty level
3. What the learner should understand
4. Suggested learning resources
5. Practical activities or exercises

Make the roadmap clear and suitable for a student.

Start from basic concepts and gradually move to advanced concepts.
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

            # Retry temporary Gemini 503 errors
            if "503" in error_message or "UNAVAILABLE" in error_message:

                if attempt < 2:
                    time.sleep(2)
                    continue

            return f"Error generating learning path: {e}"

    return "Gemini is temporarily unavailable. Please try again."

