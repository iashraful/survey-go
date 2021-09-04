import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = os.getenv("DB_CONN_STRING")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = None
    try:
        db = LocalSession()
        yield db
    finally:
        if db:
            db.close()
