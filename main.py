from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# ==============================
# EduGenie AI Modules
# ==============================

from explanation_module import explain_topic
from qna import answer_question_with_gemini
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations


# ==============================
# Create FastAPI Application
# ==============================

app = FastAPI(
    title="EduGenie",
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0"
)


# ==============================
# Templates
# ==============================

templates = Jinja2Templates(directory="templates")


# ==============================
# Static Files
# ==============================

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# =========================================================
# DASHBOARD
# =========================================================

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html"
    )
# =========================================================
# PROGRESS
# =========================================================

@app.get("/progress", response_class=HTMLResponse)
async def progress_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="progress.html"
    )


# =========================================================
# SETTINGS
# =========================================================

@app.get("/settings", response_class=HTMLResponse)
async def settings_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="settings.html"
    )

# =========================================================
# Q & A
# =========================================================

@app.get("/qa", response_class=HTMLResponse)
async def qa_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="qa.html",
        context={
            "answer": None,
            "question": ""
        }
    )


@app.post("/qa", response_class=HTMLResponse)
async def qa(
    request: Request,
    question: str = Form(...)
):

    answer = answer_question_with_gemini(question)

    return templates.TemplateResponse(
        request=request,
        name="qa.html",
        context={
            "answer": answer,
            "question": question
        }
    )


# =========================================================
# EXPLAIN TOPIC
# =========================================================

@app.get("/explain", response_class=HTMLResponse)
async def explain_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="explain.html",
        context={
            "explanation": None,
            "topic": ""
        }
    )


@app.post("/explain", response_class=HTMLResponse)
async def explain(
    request: Request,
    topic: str = Form(...)
):

    explanation = explain_topic(topic)

    return templates.TemplateResponse(
        request=request,
        name="explain.html",
        context={
            "explanation": explanation,
            "topic": topic
        }
    )


# =========================================================
# QUIZ GENERATOR
# =========================================================

@app.get("/quiz", response_class=HTMLResponse)
async def quiz_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="quiz.html",
        context={
            "quiz": None,
            "topic": ""
        }
    )


@app.post("/quiz", response_class=HTMLResponse)
async def quiz(
    request: Request,
    topic: str = Form(...)
):

    result = generate_quiz(topic)

    return templates.TemplateResponse(
        request=request,
        name="quiz.html",
        context={
            "quiz": result,
            "topic": topic
        }
    )


# =========================================================
# SUMMARY
# =========================================================

@app.get("/summarize", response_class=HTMLResponse)
async def summarize_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="summary.html",
        context={
            "summary": None,
            "text": ""
        }
    )


@app.post("/summarize", response_class=HTMLResponse)
async def summarize(
    request: Request,
    text: str = Form(...)
):

    summary = summarize_text(text)

    return templates.TemplateResponse(
        request=request,
        name="summary.html",
        context={
            "summary": summary,
            "text": text
        }
    )


# =========================================================
# LEARNING PATH
# =========================================================

@app.get("/learning-path", response_class=HTMLResponse)
async def learning_path_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="learning_path.html",
        context={
            "learning_path": None,
            "topic": ""
        }
    )


@app.post("/learning-path", response_class=HTMLResponse)
async def learning_path(
    request: Request,
    topic: str = Form(...)
):

    recommendations = get_learning_recommendations(topic)

    return templates.TemplateResponse(
        request=request,
        name="learning_path.html",
        context={
            "learning_path": recommendations,
            "topic": topic
        }
    )


# =========================================================
# HEALTH CHECK
# =========================================================

@app.get("/health")
async def health():

    return {
        "status": "ok",
        "message": "EduGenie backend is running successfully!"
    }