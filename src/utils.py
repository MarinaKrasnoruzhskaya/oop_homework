import json
import os


from confyg import ROOT_DIR
from src.category import Category
from src.product import Product


def load_json_file(pash: str) -> list:
    """ Функция читает json - данные из файла """
    path_file = os.path.join(ROOT_DIR, "data", pash)
    with open(path_file, encoding="utf-8") as json_file:
        return json.load(json_file)


def create_objects_from_json(data: list) -> list:
    """ Функция создаёт список объектов Category """
    data_object = []
    for category in data:
        products_object = []

        for product in category['products']:
            product_object = Product(**product)
            products_object.append(product_object)

        category['products'] = products_object
        category_object = Category(**category)
        data_object.append(category_object)
    return data_object


if __name__ == "__main__":
    data_json = load_json_file("data.json")
    print(type(data_json))
    print(data_json)

    data_list_object = create_objects_from_json(data_json)
    print(data_list_object)
    print(data_list_object[0].products[0].name)
