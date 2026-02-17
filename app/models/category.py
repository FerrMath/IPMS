from app.models.base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, relationship, mapped_column

class Category(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    products: Mapped[list["Product"]] = relationship(back_populates="category") # type: ignore
    
    @classmethod
    def from_dict(cls, data:dict):        
        if not isinstance(data, dict):
            raise TypeError(f"Data must be a dict. Got {type(data).__name__}")

        if not data:
            raise ValueError(f"Empty dictionary provided")
        
        id = data.get("id", None)
        name = data.get("name", None)
        
        if not id or not name:
            raise ValueError (f"Missing required fields: 'id' and 'name' are required")
        
        return cls(id=id, name=name)
    
    def __repr__(self) -> str:
        return f"Category(id={self.id!r}, name={self.name!r}"