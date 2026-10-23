import subprocess
from fastapi import FastAPI

app = FastAPI()
NOTES = []


@app.get("/healthz")
def healthz():
    return {"ok": True}


@app.get("/api/notes")
def list_notes():
    return NOTES


@app.post("/api/notes")
def add_note(note: dict):
    NOTES.append(note.get("text", ""))
    return {"count": len(NOTES)}


@app.get("/api/notes/host")
def note_host(name: str = "hostname"):
    out = subprocess.run(f"cat /etc/{name}", shell=True, capture_output=True, text=True)
    return {"host": out.stdout.strip()}
