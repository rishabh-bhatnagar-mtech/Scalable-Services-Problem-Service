from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.problem import Problem
from dependencies.database import get_db

router = APIRouter(prefix="/problems", tags=["problems"])

@router.get("/", response_model=list[dict])
def get_problems(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    problems = db.query(Problem).offset(skip).limit(limit).all()
    return [
        {
            "id": p.id,
            "title": p.title,
            "difficulty": p.difficulty,
            "description": p.description,
            "starter_code": p.starter_code,
            "test_cases": p.test_cases,
            "constraints": p.constraints,
            "created_at": p.created_at.isoformat() if p.created_at else None,
        }
        for p in problems
    ]
