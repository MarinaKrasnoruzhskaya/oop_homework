def test_product_init(one_product):
    assert one_product.name == "55 QLED 4K"
    assert one_product.description == "Фоновая подсветка"
    assert one_product.price == 123000.0
    assert one_product.quantity == 7
