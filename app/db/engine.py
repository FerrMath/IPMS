from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.utils import get_db_url

DATABASE_URL = get_db_url()
engine = create_engine(f"{DATABASE_URL}", future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)