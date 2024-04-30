from src.product import Product


class Category:
    """ Класс для категорий товара"""
    name: str
    description: str
    products: list

    count_category = 0  # кол-во категорий
    count_products = 0  # кол-во продуктов

    def __init__(self, name, description, products=None):
        """ Конструктор для инициализации экземпляра класса Category"""
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.count_category += 1
        Category.count_products += len(self.__products)

    def __str__(self):
        """ Метод реализует строковое отображение """
        total_products = sum([p.quantity for p in self.products_list])
        return f"{self.name}, количество продуктов: {total_products} шт."

    def __add__(self, other):
        """ Метод возвращает общую стоимость продуктов двух категорий"""
        return self.cost_of_all_goods() + other.cost_of_all_goods()

    @property
    def products_list(self):
        """ Метод-геттер возвращает список продуктов """
        return self.__products

    @property
    def products(self):
        """ Метод-геттер для вывода списка продуктов в виде строк в формате Название продукта, 80 руб. Остаток: 15 шт. """
        products_str = ""
        for product in self.__products:
            products_str += str(product) + "\n"
        return products_str

    @products.setter
    def products(self, new_product):
        """ Метод-сеттер для добавления товаров в категорию"""
        if isinstance(new_product, Product):
            self.__products.append(new_product)
        else:
            raise TypeError
        Category.count_products += 1

    def cost_of_all_goods(self):
        """
        Метод возвращает стоимость всех продуктов self.products_list
        """
        return sum([p.quantity * p.price for p in self.products_list])


if __name__ == "__main__":
    category_1 = Category(
        "Смартфоны",
        "Смартфоны",
        [Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)]
    )
    print(category_1.products)
    print(Category.count_products)

    category_1.products = Product("55 QLED 4K", "Фоновая подсветка", 123000.0, 7)
    print(category_1.products)
    print(Category.count_products)
    print(category_1)

    print(category_1.cost_of_all_goods())

    category_2 = Category(
        "Телевизоры",
        "Современный телевизор",
        [Product("55 QLED 4K", "Фоновая подсветка", 123000.0, 7)]
    )

    print(category_1 + category_2)

    data = [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5
                },
                {
                    "name": "Iphone 15",
                    "description": "512GB, Gray space",
                    "price": 210000.0,
                    "quantity": 8
                },
                {
                    "name": "Xiaomi Redmi Note 11",
                    "description": "1024GB, Синий",
                    "price": 31000.0,
                    "quantity": 14
                }
            ]
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
            "products": [
                {
                    "name": "55 QLED 4K",
                    "description": "Фоновая подсветка",
                    "price": 123000.0,
                    "quantity": 7
                }
            ]
        }
    ]
    categories = []
    for category in data:
        products = []
        for product in category['products']:
            products.append(Product.new_product(product))
        category['products'] = products
        categories.append(Category(**category))

# 15.1
    try:
        categories[0].products = 1
    except TypeError:
        print('Можно добавить только объекты класса Product или его наследников (Smartphone/LawnGrass)')

    product_item = Product('Test', 'Test', 1000, 10)
    categories[0].products = product_item
    print(product_item.name in categories[0].products)
