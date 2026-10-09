from typing import Type

from app.controllers.general import GeneralController, transactional
from app.models.product import Product
from sqlalchemy.orm import Session, selectinload
from sqlalchemy import select


class ProductController(GeneralController[Product]):
    def __init__(self):
        super().__init__(Product)
    
    @transactional
    def get_prod_by_id(self, obj_id:int, session: Session| None = None) -> Product | None:
        return self.get_by_id(session=session, obj_id=obj_id) # type: ignore
    
    @transactional
    def get_all_prods(self, session: Session|None = None) -> list[Product] | list:
        return self.get_all(session) # type: ignore

    @transactional
    def get_prod_with_category(self, obj_id:int, session: Session| None = None) -> Product | None:
        stmt = select(Product).options(selectinload(Product.category)).where(Product.id == obj_id)
        prod = session.execute(stmt).scalar_one() # type: ignore
        return prod
    
    @transactional
    def save_prod(self, obj:Product, session: Session|None =None) -> Product:
        return self.save(session, obj) # type: ignore

    @transactional
    def update_prod(self, obj_id:int, data: dict, session: Session|None = None) -> Product | None:
        return self.update(session, obj_id, data) # type: ignore
    
    @transactional
    def delete_prod(self, session: Session|None, obj: Product) -> None:
        return self.delete(session, obj) # type: ignore