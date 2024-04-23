class Product:
    """ Класс для описания товара в магазине """
    name: str
    description: str  # описание
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """ Конструктор для инициализации экземпляра класса Product"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        """ Метод реализует строковое отображение """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """ Метод сложения общей стоимости двух продуктов"""
        if type(other) is type(self):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError

    @classmethod
    def new_product(cls, product_dict: dict):
        """ Класс-метод возвращает созданный объект класса Product"""
        return cls(**product_dict)

    @property
    def price(self):
        """ Метод-геттер возвращает цену продукта"""
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """ Метод-сеттер изменяет цену продукта"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price


if __name__ == "__main__":
    product_data = {
        'name': 'New Product',
        'description': 'New Description',
        'price': 500,
        'quantity': 5
    }

    new_product = Product.new_product(product_data)
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)
    print(new_product)

    product_item = Product('Test', 'Test', 1000, 10)
    print(product_item.price)

    product_item.price = 800
    print(product_item.price)

    print(new_product + product_item)
