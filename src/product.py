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
        self.price = price
        self.quantity = quantity
