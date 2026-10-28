from pathlib import Path
from fastapi.responses import FileResponse
from fastapi import FastAPI

app = FastAPI(
    title="TrustOne API",
    description="A unified student-record system for six educational campuses.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "project": "TrustOne",
        "status": "running",
        "milestone": 1,
    }


@app.get("/health")
def health():
    return {"status": "healthy"}
@app.get("/dashboard")
def dashboard():
    return FileResponse(Path(__file__).resolve().parent.parent / "frontend.html")