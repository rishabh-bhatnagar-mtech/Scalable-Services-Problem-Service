from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Text, JSON, ARRAY, DateTime, text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Problem(Base):
    __tablename__ = "problems"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    difficulty = Column(String(20), nullable=False)
    description = Column(Text, nullable=False)
    starter_code = Column(JSON, nullable=False)
    test_cases = Column(JSON, nullable=False)
    constraints = Column(ARRAY(String), default=[])
    created_at = Column(DateTime, server_default=text("NOW()"))
    updated_at = Column(DateTime, server_default=text("NOW()"), onupdate=text("NOW()"))


# Pydantic model for creating a problem
class ProblemCreate(BaseModel):
    title: str
    difficulty: str
    description: str
    starter_code: str
    test_cases: str
    constraints: str
