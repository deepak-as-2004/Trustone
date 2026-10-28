
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

# Project root directory: C:\Users\deepa\trustone
BASE_DIR = Path(__file__).resolve().parent.parent
DASHBOARD_FILE = BASE_DIR / "frontend.html"

app = FastAPI(
    title="TrustOne API",
    description="Unified administration prototype for six educational campuses.",
    version="0.2.0",
)

# Synthetic demonstration data only; not connected to a database.
CAMPUSES = [
    {"id": 1, "name": "Campus 01", "type": "Engineering", "students": 3200},
    {"id": 2, "name": "Campus 02", "type": "Polytechnic", "students": 2400},
    {"id": 3, "name": "Campus 03", "type": "School", "students": 1800},
    {"id": 4, "name": "Campus 04", "type": "School", "students": 2200},
    {"id": 5, "name": "Campus 05", "type": "School", "students": 1900},
    {"id": 6, "name": "Campus 06", "type": "Higher Education", "students": 2500},
]


@app.get("/")
def root():
    return {
        "project": "TrustOne",
        "status": "running",
        "version": "0.2.0",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/api/overview")
def overview():
    return {
        "project": "TrustOne",
        "campus_count": len(CAMPUSES),
        "student_count": sum(campus["students"] for campus in CAMPUSES),
        "record_sources": 40,
        "data_mode": "synthetic_demo",
        "campuses": CAMPUSES,
    }


@app.get("/dashboard")
def dashboard():
    if not DASHBOARD_FILE.is_file():
        return {
            "error": "Dashboard file not found",
            "expected_path": str(DASHBOARD_FILE),
        }

    return FileResponse(
        path=str(DASHBOARD_FILE),
        media_type="text/html",
    )
