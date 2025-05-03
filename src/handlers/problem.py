from sqlalchemy.orm import Session

from models.problem import Problem, ProblemCreate


def get_problems_handler(skip: int, limit: int, db: Session):
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


def create_problem_handler(problem: ProblemCreate, db: Session):
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
