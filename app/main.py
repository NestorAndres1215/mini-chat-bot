from fastapi import FastAPI
from app.services.chatbot import responder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parent.parent

frontend_path = BASE_DIR / "frontend"
static_path = BASE_DIR / "frontend"

# HTML
@app.get("/")
def home():
    return FileResponse(frontend_path / "index.html")

# STATIC (CSS + JS)
app.mount("/static", StaticFiles(directory=static_path), name="static")

@app.get("/chat")
def chat(mensaje: str):
    return {"respuesta": responder(mensaje)}