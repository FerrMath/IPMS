import pytest

from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from app.db.engine import create_my_engine
from app.models.base import Base
from app.models import Category, Product

engine = create_my_engine(test=True)

@pytest.fixture(scope="session")
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def db_session(setup_database):
    connenction = engine.connect()
    transaction = connenction.begin()
    
    TestingSession = sessionmaker(
        bind=connenction,
        autoflush=False,
        autocommit=False,
        expire_on_commit=False
    )
    
    session = TestingSession()
    
    yield session
    
    session.close()
    transaction.rollback()
    connenction.close()


class TestDatabase:
    
    def test_execute_simple_read_returns_correct_value(self, db_session):
        result = db_session.execute(text("SELECT 1"))
        assert result.scalar() == 1
    
    def test_create_and_read_category(self, db_session):
        cat = Category(name="Test")
        db_session.add(cat)
        db_session.flush()
        
        result = db_session.get(Category, cat.id)
        
        assert result is not None
        assert cat.id == result.id
        assert cat == result
    
    def test_delete_category(self, db_session):
        cat = Category(name="Test")
        db_session.add(cat)
        db_session.commit()
        
        assert db_session.get(Category, cat.id) is not None
        
        db_session.delete(cat)
        db_session.flush()
        
        assert db_session.get(Category, cat.id) is None