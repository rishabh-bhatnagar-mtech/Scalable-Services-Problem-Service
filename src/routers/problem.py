from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from dependencies.database import get_db
from handlers.problem import get_problems_handler, create_problem_handler
from models.problem import ProblemCreate

router = APIRouter(prefix="/problems", tags=["problems"])


@router.get("/", response_model=list[dict])
def get_problems(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_problems_handler(skip, limit, db)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=dict)
def create_problem(problem: ProblemCreate, db: Session = Depends(get_db)):
    return create_problem_handler(problem, db)
