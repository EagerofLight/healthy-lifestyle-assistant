from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import get_db

router = APIRouter(
    prefix="/api/v1/database",
    tags=["/database"]
)

@router.get("/health")
def health(db: Session = Depends(get_db)):
    # connection test
    result = db.execute(text("SELECT 1")).scalar()
    return {"status": "ok", "db": result}