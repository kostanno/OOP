import pytest
from src.homework_class import Product, Category, LawnGrass,Smartphone


@pytest.fixture
def sample_product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_product_initialization(sample_product):
    assert sample_product.name == "Samsung Galaxy S23 Ultra"
    assert sample_product.description == "256GB, Серый цвет, 200MP камера"
    assert sample_product.price == 180000.0
    assert sample_product.quantity == 5


def test_change_price(sample_product):
    sample_product.price = 180000.0
    assert sample_product.price == 180000.0


@pytest.fixture
def sample_category():
    product1 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product2 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    return Category("Электроника", "Техника", [product1, product2])


def test_category_count(sample_category):
    assert Category.category_count == 0
    Category("Iphone 15", "512GB, Gray space", [])
    assert Category.category_count == 0


def test_price(sample_product):
    product = Product
    product.price = 75
    assert product.price == 75
    product.price = 30
    assert product.price == 30


def test_products():
    products = [{"name": "Телефон", "price": 50000, "quantity": 10}, {"name": "Ноутбук", "price": 80000, "quantity": 5},]
    expected = ("Телефон, 50000 руб. Остаток: 10 шт.\n", "Ноутбук, 80000 руб. Остаток: 5 шт.\n")
    assert(products, expected)


test1 = [
    ("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
    ("Iphone 15", "512GB, Gray space", 210000.0, 8),
    ("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
]


@pytest.fixture(params=test1)
def product(request):
    return Product(*request.param)


def test_str(product):
    result = str(product)
    assert product.name in result
    assert f"{product.price} руб." in result
    assert f"Остаток: {product.quantity} шт." in result

def test_Smartphone():
    smartphone1 = Smartphone(
        name="iPhone 13",
        description="Флагман Apple",
        price=999,
        quantity=5,
        efficiency="High",
        model="13",
        memory=128,
        color="Midnight"
    )

    smartphone2 = Smartphone(
        name="Galaxy S21",
        description="Флагман Samsung",
        price=899,
        quantity=3,
        efficiency="High",
        model="S21",
        memory=256,
        color="Phantom"
    )
    try:
        total_phones = smartphone1 + smartphone2
        expected_phones = (999 * 5) + (899 * 3)
        assert total_phones == expected_phones, f"Ожидалось {expected_phones}, получено {total_phones}"
        print("Тест 1 пройден: сложение смартфонов работает корректно")
    except Exception as e:
        print(f"Тест 1 не пройден: {e}")


def test_LawnGrass():
    lawn_grass1 = LawnGrass(
        name="Premium Grass",
        description="Мягкий газон",
        price=25,
        quantity=100,
        country="Russia",
        germination_period="14 дней",
        color="Green"
    )

    lawn_grass2 = LawnGrass(
        name="Standard Grass",
        description="Обычный газон",
        price=15,
        quantity=200,
        country="Belarus",
        germination_period="21 день",
        color="Dark Green"
    )

    try:
        total_grass = lawn_grass1 + lawn_grass2
        expected_grass = (25 * 100) + (15 * 200)
        assert total_grass == expected_grass, f"Ожидалось {expected_grass}, получено {total_grass}"
        print("Тест 2 пройден: сложение газонных трав работает корректно")
    except Exception as e:
        print(f"Тест 2 не пройден: {e}")
