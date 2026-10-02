from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from explanation_module import explain_topic
from qna import answer_question_with_gemini
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <body>
            <h1>EduGenie Import Test</h1>
            <p>All EduGenie modules imported successfully.</p>
        </body>
    </html>
    """