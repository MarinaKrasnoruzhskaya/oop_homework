from src.product import Product


class Category:
    """ Класс для категорий товара"""
    name: str
    description: str
    products: list

    count_category = 0
    count_products = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.count_category += 1
        Category.count_products += len(self.__products)

    @property
    def products_list(self):
        return self.__products

    @property
    def products(self):
        """ Метод-геттер для вывода списка продуктов в виде строк в формате Название продукта, 80 руб. Остаток: 15 шт. """
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    @products.setter
    def products(self, new_product: Product):
        """ Метод-сеттер для добавления товаров в категорию"""
        self.__products.append(new_product)
        Category.count_products += 1


if __name__ == "__main__":
    category_1 = Category(
        "Смартфоны",
        "Смартфоны",
        [Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)]
    )
    print(category_1.products)
    print(Category.count_products)

    category_1.products = Product("55 QLED 4K","Фоновая подсветка", 123000.0, 7)
    print(category_1.products)
    print(Category.count_products)
