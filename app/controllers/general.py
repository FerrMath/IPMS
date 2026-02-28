from typing import Type, Generic, TypeVar
from sqlalchemy.orm import Session, DeclarativeBase
from functools import wraps
from app.db.engine import SessionLocal

T = TypeVar("T", bound=DeclarativeBase)

def transactional(func):
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