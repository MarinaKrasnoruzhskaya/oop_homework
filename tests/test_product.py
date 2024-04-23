import pytest

from src.product import Product


def test_product_init(first_product):
    assert first_product.name == "55 QLED 4K"
    assert first_product.description == "Фоновая подсветка"
    assert first_product.price == 123000.0
    assert first_product.quantity == 7


def test_product_new_product(product_test):
    new_product = Product.new_product(product_test)
    assert new_product.name == 'New Product'
    assert new_product.description == 'New Description'
    assert new_product.price == 500
    assert new_product.quantity == 5


def test_product_price_property(first_product):
    assert first_product.price == 123000.0


def test_product_price_setter(first_product):
    first_product.price = 80_000
    assert first_product.price == 80_000
    first_product.price = -80_000
    assert first_product.price == 80_000


def test_product_str(first_product):
    assert str(first_product) == "55 QLED 4K, 123000.0 руб. Остаток: 7 шт."


def test_product_add(first_product, second_product):
    assert first_product + second_product == 871_000


def test_product_add_error(first_product, first_smartphone, first_lawn_grass):
    with pytest.raises(TypeError):
        result = first_product + first_smartphone
        result2 = first_product + first_lawn_grass
        result3 = first_smartphone + first_lawn_grass
        result4 = first_product + 1
