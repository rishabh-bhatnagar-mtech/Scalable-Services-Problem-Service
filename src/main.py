import uvicorn
from fastapi import FastAPI

from core.config import get_settings
from create_initial_data import create_seed_problems_if_not_exists
from dependencies.database import get_engine
from models.problem import Base
from routers.problem import router as problems_router

Base.metadata.create_all(bind=get_engine(get_settings()))

app = FastAPI()
app.include_router(problems_router)

create_seed_problems_if_not_exists()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
