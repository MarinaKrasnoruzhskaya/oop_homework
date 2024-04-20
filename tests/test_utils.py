from src.utils import create_objects_from_json, load_json_file


def test_load_json():
    assert len(load_json_file("test.json")) == 1


def test_create_objects_from_json(data_test):
    data_object = create_objects_from_json(data_test)
    assert len(data_object) == 1
    assert data_object[0].name == "Смартфоны"
    assert data_object[0].description == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    assert len(data_object[0].products) == 1
