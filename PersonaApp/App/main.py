from fastapi import FastAPI
from App.routers.chat import router as chat_router

app = FastAPI(
    title="Persona API",
    description="AI Persona Backend using FastAPI",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to Persona API 🚀"
    }

app.include_router(chat_router)