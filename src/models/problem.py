from typing import List

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


class TestCase(BaseModel):
    input: str
    output: str

    @classmethod
    def from_dict(cls, data: dict) -> 'TestCase':
        return cls(
            input=data.get("input"),
            output=data.get("output"),
        )

    def to_dict(self):
        return {
            "input": self.input,
            "output": self.output,
        }


class StarterCode(BaseModel):
    language: str
    code: str

    @classmethod
    def from_dict(cls, data: dict) -> 'StarterCode':
        return cls(
            language=data.get("language"),
            code=data.get("code"),
        )

    def to_dict(self):
        return {
            "language": self.language,
            "code": self.code,
        }


class ProblemCreate(BaseModel):
    title: str
    difficulty: str
    description: str
    starter_code: StarterCode
    test_cases: List[TestCase]
    constraints: List[str]

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data.get("title"),
            difficulty=data.get("difficulty"),
            description=data.get("description"),
            starter_code=StarterCode.from_dict(data.get("starter_code")),
            test_cases=[TestCase.from_dict(tc) for tc in data.get("test_cases")],
            constraints=data.get("constraints"),
        )
