# EduMind AI — Website Starter

A responsive React + Vite frontend prototype for the EduMind AI student learning platform.

## What's included
- Overview dashboard with daily study plan, completion tracking, skill passport, learning streak, and progress cards
- Clickable sidebar navigation for My learning, Skill assessment, Study planner, Career roadmap, Rescue Mode, and Settings
- Interactive task checkboxes and add-task control
- Quick skill assessment modal
- AI study-coach chat UI (sample responses only)
- Responsive layouts for desktop, tablet, and mobile
- FastAPI backend starter with a Gemini API integration point
- Firebase setup template for authentication and Firestore

## Run the frontend
1. Install Node.js (LTS).
2. Extract this folder and open a terminal in it.
3. Run `npm install`
4. Copy `.env.example` to `.env` and add Firebase settings if you want to enable Firebase.
5. Run `npm run dev`
6. Open the local URL printed by Vite.

## Backend (optional starter)
Python 3.10+ recommended.

```bash
cd backend
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env
uvicorn main:app --reload
```

The backend currently exposes `/health` and `/api/coach`. Add your Gemini API key to `backend/.env`. Do not expose secret API keys in React.

## Important
This is a working frontend prototype with demo/sample data, not a fully deployed production application. Firebase authentication, Firestore persistence, and Gemini-generated responses require your own project credentials and setup. The backend includes a safe integration point for Gemini; the sample chat on the frontend does not call it yet.

## Suggested stack
- Frontend: React, Vite, JavaScript, CSS
- Backend: Python, FastAPI
- Data/auth: Firebase Authentication + Cloud Firestore (starter module included)
- AI: Google Gemini API (backend integration point)
- Deployment: Vercel for frontend; Render or another Python host for backend
- Version control: GitHub
