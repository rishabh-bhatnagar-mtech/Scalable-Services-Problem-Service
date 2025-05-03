import json
from pathlib import Path

from sqlalchemy.orm import Session

from core.config import get_settings
from dependencies.database import get_db
from handlers.problem import create_problem_handler, get_problems_handler
from models.problem import ProblemCreate


def load_problems(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def add_seed_problems(db: Session):
    json_file_path = "sample_problems.json"
    problems = load_problems(json_file_path)
    for problem in problems:
        problem_payload = ProblemCreate.from_dict(problem)
        created_problem = create_problem_handler(problem_payload, db)
        print(f"Added problem: {created_problem['title']}")


def create_seed_problems_if_not_exists():
    db: Session = next(get_db(get_settings()))
    existing_problems = get_problems_handler(0, 2, db)
    if len(existing_problems) > 0:
        print("Initial data already exists. Not adding any more problems.")
    else:
        add_seed_problems(db)
