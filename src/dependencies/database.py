from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import Settings


def get_engine(settings: Settings):
    engine = create_engine(settings.get_database_url())
    return engine


def get_db(settings: Settings):
    engine = get_engine(settings)
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = session_local()
    try:
        yield db
    finally:
        db.close()
