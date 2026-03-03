from sqlalchemy.orm import Session, DeclarativeBase
from sqlalchemy import select
from typing import Type, Generic, TypeVar
from functools import wraps
from app.db.engine import SessionLocal

T = TypeVar("T", bound=DeclarativeBase)

def transactional(func):
    """Decorator that wraps methods in a database transaction.
    
    Provides a SQLAlchemy session using `SessionLocal`and in injects it into the decorated method/function.
    If an exception is raised, the transaction is rolled back and the exception
    is re-raised.

    Args:
        func (Callable): Function to be wrapped. It must accept a `session` keyword argument

    Returns:
        Callable: The wrapped function to be executed
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        with SessionLocal() as session:
            try:
                result = func(*args, session=session, **kwargs)
                session.commit()
                return result
            except:
                session.rollback()
                raise
    return wrapper

class GeneralController(Generic[T]):
    def __init__(self, model: Type[T]):
        self.model = model
    
    def save(self, session: Session, obj:T) -> T:
        session.add(obj)
        session.flush()
        session.refresh(obj)
        return obj
    
    def get_all(self, session: Session) -> list[T]:
        stmt = select(self.model)
        result = session.scalars(stmt).all()
        return list(result)
    
    def get_by_id(self, session:Session, obj_id:int) -> T | None:
        return session.get(self.model, obj_id)
    
    def update(self, session: Session, obj_id:int, data: dict) -> T | None:
        obj = session.get(self.model, obj_id)
        
        if not obj:
            return None
        
        for k, v in data.items():
            if hasattr(obj, k):
                setattr(obj, k, v)
            else:
                raise ValueError(f"invalid field []")
            
        session.flush()
        session.refresh(obj)
        return obj
    
    def delete(self, session:Session, obj: T) -> None:
        session.delete(obj)