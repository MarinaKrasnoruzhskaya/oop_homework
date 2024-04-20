class Category:
    """ Класс для категорий товара"""
    name: str
    description: str
    products: list

    count_category = 0
    count_products = 0

    def __init__(self, name, description, products = None):
        self.name = name
        self.description = description
        self.products = products if products else []

        Category.count_category += 1
        Category.count_products += len(self.products)

