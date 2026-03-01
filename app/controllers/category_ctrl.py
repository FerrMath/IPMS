from typing import Type

from app.controllers.general import GeneralController, transactional
from app.models.category import Category
from app.models.product import Product
from sqlalchemy.orm import Session, selectinload
from sqlalchemy import select

class CategoryController(GeneralController[Category]):
    def __init__(self):
        super().__init__(Category)
    
    @transactional
    def get_category_by_id(self, session:Session,  obj_id:int) -> Category | None:
        return self.get_by_id(session, obj_id)
    
    @transactional
    def get_all_categories(self, session=None):
        return self.get_all(session=session) # type: ignore
    
    @transactional
    def get_category_with_prods(self, obj_id:int, session: Session|None =None ) -> Category | None:
        stmt = select(Category).options(selectinload(Category.products)).where(Category.id == obj_id)
        cat = session.execute(stmt).scalar_one() # type: ignore
        return cat
    
    @transactional
    def save_category(self, obj:Category, session=None) -> Category:
        return self.save(session, obj) # type: ignore
    
    @transactional
    def update_category(self, session: Session, obj_id:int, data:dict) -> Category | None:
        return self.update(session, obj_id, data)
    
    @transactional
    def delete_category(self, session: Session, obj: Category) -> None:
        return self.delete(session, obj)