from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.utils import get_db_url

def create_my_engine(test=False):
    DATABASE_URL = get_db_url(test)
    return create_engine(f"{DATABASE_URL}", future=True)

def create_sessionLocal(test=False):
    engine = create_my_engine(test)
    return sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)