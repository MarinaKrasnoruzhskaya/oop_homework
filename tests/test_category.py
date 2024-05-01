import pytest

from src.product import Product


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


def test_category_products_list_setter(first_category, first_product, first_smartphone, first_lawn_grass):
    assert len(first_category.products_list) == 1
    first_category.products = first_product
    assert len(first_category.products_list) == 2
    first_category.products = first_smartphone
    assert len(first_category.products_list) == 3
    first_category.products = first_lawn_grass
    assert len(first_category.products_list) == 4


def test_category_str(first_category, second_category):
    assert str(first_category) == "Телевизоры, количество продуктов: 7 шт."
    assert str(second_category) == "Смартфоны, количество продуктов: 13 шт."


def test_category_cost_of_all_goods(second_category):
    assert second_category.cost_of_all_goods() == 2_580_000.0


def test_category_add(first_category, second_category):
    assert first_category + second_category == 3_441_000.0


def test_category_products_list_setter_error(first_category):
    with pytest.raises(TypeError):
        first_category.products = 1


def test_category_middle_price(second_category, category_without_products):
    assert second_category.middle_price() == 195_000.0
    assert category_without_products.middle_price() == 0


def test_custom_exception(capsys, first_category):
    assert len(first_category.products_list) == 1

    broken_product = Product('Test', 'Test', 1000, -5)
    first_category.products = broken_product
    message = capsys.readouterr()

    assert message.out.strip().split('\n')[-2] == "Нельзя добавить товар с отрицательным количеством"
    assert message.out.strip().split('\n')[-1] == "Обработка продукта завершена"

    broken_product = Product('Test', 'Test', 1000, 5)
    first_category.products = broken_product
    message = capsys.readouterr()

    assert message.out.strip().split('\n')[-2] == "Продукт добавлен"
    assert message.out.strip().split('\n')[-1] == "Обработка продукта завершена"
    assert len(first_category.products_list) == 2
