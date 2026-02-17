from sqlalchemy import String, ForeignKey, Float, Integer, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base
from datetime import datetime

class Product(Base):
    __tablename__ = "products"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    category: Mapped["Category"] = relationship(back_populates="products") # type: ignore
    price: Mapped[float] = mapped_column(Float)
    stock: Mapped[int] = mapped_column(Integer, default=0)
    rating: Mapped[float] = mapped_column(Float, default=0.0)
    discontinued: Mapped[bool] = mapped_column(Boolean, default=False)
    release_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    
    @classmethod
    def from_dict(cls, data:dict) -> "Product":
        if not isinstance(data, dict):
            raise TypeError(f"Data must be a dict. Got {type(data).__name__}")
        
        if not data:
            raise ValueError(f"Empty dictionary provided")
        
        required = {"name", "price", "category_id"}
        missing = [key for key in required if data.get(key) is None]

        if missing:
            raise ValueError(f"Missing required key/value: {missing}")
        
        return cls(
            **data
        )
    
    def __repr__(self) -> str:
        return f"Product(id={self.id!r}, name={self.name!r}, category={self.category_id}, price_usd={self.price:.2f}, stock={self.stock}, rating={self.rating}, is_discontinued={self.discontinued}, release_date={self.release_date})"