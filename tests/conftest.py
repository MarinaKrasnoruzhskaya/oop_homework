import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def one_product():
    return Product("55 QLED 4K","Фоновая подсветка", 123000.0, 7)


@pytest.fixture
def first_category():
    return Category(
        "Телевизоры",
        "Современный телевизор",
        [Product("55 QLED 4K","Фоновая подсветка", 123000.0, 7)]
    )

@pytest.fixture
def second_category():
    return Category("Смартфоны", "Смартфоны", [
        Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    ])


@pytest.fixture
def data_test():
    return [
  {
    "name": "Смартфоны",
    "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
    "products": [
      {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      }
    ]
  }
]


@pytest.fixture
def product_test():
    return {
        'name': 'New Product',
        'description': 'New Description',
        'price': 500,
        'quantity': 5
    }