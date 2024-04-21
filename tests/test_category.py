def test_category_init(first_category, second_category):
    assert first_category.name == "Телевизоры"
    assert first_category.description == "Современный телевизор"
    assert len(first_category.products_list) == 1

    assert first_category.count_category == 2
    assert second_category.count_category == 2

    assert first_category.count_products == 3
    assert second_category.count_products == 3


def test_category_products_property(first_category):
    assert first_category.products == "55 QLED 4K, 123000.0 руб. Остаток: 7 шт.\n"


def test_category_products_list_setter(first_category, first_product):
    assert len(first_category.products_list) == 1
    first_category.products = first_product
    assert len(first_category.products_list) == 2


def test_category_str(first_category, second_category):
    assert str(first_category) == "Телевизоры, количество продуктов: 7 шт."
    assert str(second_category) == "Смартфоны, количество продуктов: 13 шт."


def test_category_cost_of_all_goods(second_category):
    assert second_category.cost_of_all_goods() == 2_580_000.0


def test_category_add(first_category, second_category):
    assert first_category + second_category == 3_441_000.0
