from app.models.product import Product
from app.models.category import Category
import pytest

class TestProductModel:
    def test_create_product_with_valid_data_of_only_required_attributes_before_persistence(self):
        p = Product(name="Produto", price=123.45)
        assert p.name == "Produto"
        assert p.price == 123.45
        
        # Attributes unset before persistence
        
        assert p.stock is None
        assert p.category is None
        assert p.category_id is None
        assert p.release_date is None
        assert p.discontinued is None    
    
    def test_create_product_with_valid_dict_of_required_attributes_before_persistence(self):
        data = {
            "name": "Produto",
            "price": 50.00
        }
        p = Product.from_dict(data)
        assert p.name == "Produto"
        assert p.price == 50.00
        
        # Attributes unset before persistence
        
        assert p.stock is None
        assert p.category is None
        assert p.category_id is None
        assert p.release_date is None
        assert p.discontinued is None 
        
    def test_create_product_with_empty_dict_will_raise_value_error(self):
        data = dict()
        with pytest.raises(ValueError, match="Empty dictionary provided"):
            Product.from_dict(data)
    
    def test_create_product_with_non_dict_data_format_raises_type_error(self):
        data = ["Produto", 1.50]
        with pytest.raises(TypeError, match=f"Data must be a dict"):
            Product.from_dict(data)
    
    def test_create_product_without_required_attributes_raises_value_error(self):
        data = {
            "stock": 5,
            "discontinued": True
        }
        with pytest.raises(ValueError, match=f"Missing required key/value"):
            Product.from_dict(data)
    
    def test_create_relationship_with_category(self):
        p = Product(id=3, name="Produto", price=543.21)
        c = Category(id=2, name="Categoria")
        
        p.category = c
        
        assert p.category is c
        assert p in c.products
        assert len(p.category.products) == 1
        
        # Attributes unset before persistence

        assert p.category_id is None
