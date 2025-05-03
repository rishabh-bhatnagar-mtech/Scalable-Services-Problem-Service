from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import get_settings, Settings


def get_db(settings: Settings):
    engine = create_engine(settings.get_database_url())
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = session_local()
    try:
        yield db
    finally:
        db.close()
