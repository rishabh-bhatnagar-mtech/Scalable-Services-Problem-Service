from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from dependencies.database import get_db
from models.problem import Problem, ProblemCreate

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


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=dict)
def create_problem(problem: ProblemCreate, db: Session = Depends(get_db)):
    db_problem = Problem(
        title=problem.title,
        difficulty=problem.difficulty,
        description=problem.description,
        starter_code=problem.starter_code,
        test_cases=problem.test_cases,
        constraints=problem.constraints,
    )
    db.add(db_problem)
    db.commit()
    db.refresh(db_problem)
    return {
        "id": db_problem.id,
        "title": db_problem.title,
        "difficulty": db_problem.difficulty,
        "description": db_problem.description,
        "starter_code": db_problem.starter_code,
        "test_cases": db_problem.test_cases,
        "constraints": db_problem.constraints,
        "created_at": db_problem.created_at.isoformat() if db_problem.created_at else None,
    }
