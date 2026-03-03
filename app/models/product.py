from sqlalchemy import (
    String,
    Integer,
    Boolean,
    DateTime,
    ForeignKey,
    Numeric,
    CheckConstraint,
    func
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from decimal import Decimal
from app.models.base import Base
from datetime import datetime

class Product(Base):
    __tablename__ = "products"
    __table_args__ = (
        CheckConstraint("price >= 0", name="ck_product_price_non_negative"),
        CheckConstraint("stock >= 0", name="ck_product_stock_non_negative"),
        CheckConstraint("rating >= 0 AND rating <= 5", name="ck_product_rating_range"),
    )
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=False)
    category: Mapped["Category"] = relationship(back_populates="products") # type: ignore
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    stock: Mapped[Integer] = mapped_column(Integer, default=0, server_default="0")
    rating: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=0.0, server_default="0")
    discontinued: Mapped[bool] = mapped_column(Boolean, default=False, server_default="false")
    release_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, nullable=False, server_default=func.now())
    
    @classmethod
    def from_dict(cls, data:dict) -> "Product":
        if not isinstance(data, dict):
            raise TypeError(f"Data must be a dict. Got {type(data).__name__}")
        
        if not data:
            raise ValueError(f"Empty dictionary provided")
        
        required = {"name", "price"}
        missing = [key for key in required if data.get(key) is None]

        if missing:
            raise ValueError(f"Missing required key/value: {missing}")
        
        return cls(
            **data
        )
    
    def __repr__(self) -> str:
        return f"Product(id={self.id!r}, name={self.name!r}, category={self.category_id}, price_usd={self.price:.2f}, stock={self.stock}, rating={self.rating}, is_discontinued={self.discontinued}, release_date={self.release_date})"