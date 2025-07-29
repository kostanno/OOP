import pytest
from src.homework_class import Product
from src.homework_class import Category


@pytest.fixture
def sample_product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_product_initialization(sample_product):
    assert sample_product.name == "Samsung Galaxy S23 Ultra"
    assert sample_product.description == "256GB, Серый цвет, 200MP камера"
    assert sample_product.price == 180000.0
    assert sample_product.quantity == 5


def test_change_price(sample_product):
    sample_product.price = 45000.0
    assert sample_product.price == 45000.0


@pytest.fixture
def sample_category():
    product1 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product2 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    return Category("Электроника", "Техника", [product1, product2])


def test_category_count(sample_category):
    assert Category.category_count == 1
    Category("Iphone 15", "512GB, Gray space", [])
    assert Category.category_count == 2
