from src.product import Product


def test_product_init(one_product):
    assert one_product.name == "55 QLED 4K"
    assert one_product.description == "Фоновая подсветка"
    assert one_product.price == 123000.0
    assert one_product.quantity == 7


def test_new_product(product_test):
    new_product = Product.new_product(product_test)
    assert new_product.name == 'New Product'
    assert new_product.description == 'New Description'
    assert new_product.price == 500
    assert new_product.quantity == 5


def test_price_property(one_product):
    assert one_product.price == 123000.0


def test_price_setter(one_product):
    one_product.price = 80_000
    assert one_product.price == 80_000
    one_product.price = -80_000
    assert one_product.price == 80_000
