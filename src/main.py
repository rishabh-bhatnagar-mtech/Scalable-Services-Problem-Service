import uvicorn
from fastapi import FastAPI

from src.dependencies.database import engine
from src.models.problem import Base
from src.routers.problem import router as problems_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(problems_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
