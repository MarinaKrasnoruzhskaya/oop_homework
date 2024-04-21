def test_category_init(first_category, second_category):
    assert first_category.name == "Телевизоры"
    assert first_category.description == "Современный телевизор"
    assert len(first_category.products_list) == 1

    assert first_category.count_category == 2
    assert second_category.count_category == 2

    assert first_category.count_products == 3
    assert second_category.count_products == 3


def test_products_property(first_category):
    assert first_category.products == "55 QLED 4K, 123000.0 руб. Остаток: 7 шт.\n"


def test_products_list_setter(first_category, one_product):
    assert len(first_category.products_list) == 1
    first_category.products = one_product
    assert len(first_category.products_list) == 2
