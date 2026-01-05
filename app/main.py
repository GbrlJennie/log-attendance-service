from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from . import database
import uvicorn

app = FastAPI(title="Attendance Log Service Pro", version="2.0.0")

database.init_db()
templates = Jinja2Templates(directory="app/templates")

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic Schema Update
class LogCreate(BaseModel):
    user_id: int
    event_type: str  # CHECK_IN, CHECK_OUT
    category: str    # WFO, WFH, SAKIT, IZIN
    notes: Optional[str] = None

# --- API ENDPOINTS ---

@app.post("/api/logs", status_code=201)
def create_log(log: LogCreate, db: Session = Depends(get_db)):
    new_log = database.AttendanceLog(
        user_id=log.user_id,
        event_type=log.event_type,
        category=log.category,
        notes=log.notes,
        node_id="STB-UNIT-1" # Simulasi nama device
    )
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    return {"message": "Success", "data": new_log}

@app.get("/api/logs")
def get_logs(limit: int = 20, db: Session = Depends(get_db)):
    return db.query(database.AttendanceLog).order_by(database.AttendanceLog.timestamp.desc()).limit(limit).all()

# --- FRONTEND ---
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=3002, reload=True)