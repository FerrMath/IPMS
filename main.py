from app.controllers.product_ctrl import ProductController
from app.controllers.category_ctrl import CategoryController
from app.models import Category, Product

if __name__ == "__main__":
    pc = ProductController()
    cc = CategoryController()