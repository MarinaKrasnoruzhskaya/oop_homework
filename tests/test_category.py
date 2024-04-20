def test_category_init(first_category, second_category):
    assert first_category.name == "Телевизоры"
    assert first_category.description == "Современный телевизор"
    assert len(first_category.products) == 1

    assert first_category.count_category == 2
    assert second_category.count_category == 2

    assert first_category.count_products == 3
    assert second_category.count_products == 3
