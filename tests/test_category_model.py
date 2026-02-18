from app.models.category import Category
from app.models.product import Product
import pytest

class TestCategoryModel:
    def test_create_category_with_valid_data(self):
        c = Category(id=1, name="Category")
        assert c.id == 1
        assert c.name == "Category"
        assert not c.products
    
    def test_create_category_with_valid_dict(self):
        data = {"id":1, "name":"Category"}
        c = Category.from_dict(data)
        assert c.id == 1
        assert c.name == "Category"
        assert not c.products
    
    def test_create_category_with_empty_dict_will_raise_value_error(self):
        data = dict()
        with pytest.raises(ValueError, match="Empty dictionary provided"):
            Category.from_dict(data)
    
    def test_create_category_with_non_dict_data_format_raises_type_error(self):
        data = [1, "A valid name"]
        with pytest.raises(TypeError, match=f"Data must be a dict. Got {type(data).__name__}"):
            Category.from_dict(data)

    def test_create_category_from_dict_with_missing_necessary_params_raises_value_error(self):
        data = {"name":"A valid name"}
        with pytest.raises(ValueError, match=f"Missing required fields: both 'id' and 'name' are required"):
            Category.from_dict(data)
        
    def test_create_relationship_with_product(self):
        c = Category.from_dict({"id":3,"name":"Game"})
        p = Product()
        c.products.append(p)
        
        assert len(c.products) == 1
        assert c.products[0] is p
        assert p.category is c
        