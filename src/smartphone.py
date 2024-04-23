from src.product import Product


class Smartphone(Product):
    """Класс для описания смартфона"""
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """ Конструктор для инициализации экземпляра класса Smartphone"""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


if __name__ == "__main__":
    product_item = Smartphone('Test1', 'Test1', 2000, 10, 1.5, 'Xiaomi', 10000, 'red')
    print(product_item.name)
    print(product_item.description)
    print(product_item.price)
    print(product_item.quantity)
    print(product_item.efficiency)
    print(product_item.model)
    print(product_item.memory)
    print(product_item.color)

    product_item2 = Smartphone('Test2', 'Test2', 2000, 10, 1.5, 'Xiaomi', 10000, 'red')

    print(product_item + product_item2)
