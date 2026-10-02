import os
import json
from dotenv import load_dotenv
from google import genai


# Load environment variables
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)


def clean_json_block(text: str) -> str:
    """
    Remove Markdown code blocks from Gemini response.
    """

    text = text.strip()

    if text.startswith("```json"):
        text = text[7:]

    elif text.startswith("```"):
        text = text[3:]

    if text.endswith("```"):
        text = text[:-3]

    return text.strip()


def generate_quiz(passage: str):
    """
    Generate 3 MCQs with 4 options each.
    """

    try:
        prompt = f"""
You are EduGenie, an educational quiz generator.

Read the following passage and create exactly 3 multiple-choice questions.

PASSAGE:
{passage}

Requirements:

1. Create exactly 3 questions.
2. Each question must have exactly 4 options.
3. Provide one correct answer.
4. Questions must be based only on the given passage.
5. Make the questions suitable for students.
6. Return ONLY valid JSON.
7. Do not use Markdown.

Use this exact JSON format:

[
    {{
        "question": "Question text",
        "options": [
            "Option A",
            "Option B",
            "Option C",
            "Option D"
        ],
        "correct_answer": "Option A"
    }}
]
"""

        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )

        cleaned_response = clean_json_block(
            response.text
        )

        quiz = json.loads(cleaned_response)

        return quiz

    except json.JSONDecodeError as e:
        return {
            "error": f"Quiz JSON parsing error: {e}"
        }

    except Exception as e:
        return {
            "error": f"Quiz generation error: {e}"
        }