
def test_lawn_grass_init(first_lawn_grass):
    assert first_lawn_grass.name == "Test1"
    assert first_lawn_grass.description == "Test1"
    assert first_lawn_grass.price == 3000
    assert first_lawn_grass.quantity == 10
    assert first_lawn_grass.country =="Canada"
    assert first_lawn_grass.germination_period == "1 year"
    assert first_lawn_grass.color == "light green"


def test_product_add(first_lawn_grass, second_lawn_grass):
    assert first_lawn_grass + second_lawn_grass == 40_000
