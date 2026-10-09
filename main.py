import os
from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
app = FastAPI(title="EduMind AI API", version="0.1.0")

origins = os.getenv("FRONTEND_ORIGIN", "http://localhost:5173").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in origins],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CoachRequest(BaseModel):
    message: str
    student_level: Optional[str] = "beginner"
    goal: Optional[str] = "study planning"

@app.get("/health")
def health():
    return {"status": "ok", "service": "edumind-ai-api"}

@app.post("/api/coach")
async def coach(request: CoachRequest):
    """Demo endpoint. Add Gemini API invocation here using a server-side key."""
    if not os.getenv("GEMINI_API_KEY"):
        return {
            "reply": (
                "This is a demo coach response. Add GEMINI_API_KEY to backend/.env "
                "and connect the Gemini SDK here for personalized AI responses."
            ),
            "mode": "demo",
        }

    # Intentionally do not call an AI service until you configure a model/API version.
    # Keep provider API keys on the server, never in the browser.
    return {
        "reply": "Your Gemini key is configured. Complete the model invocation in backend/main.py.",
        "mode": "configured-placeholder",
    }
