from src.product import Product


class LawnGrass(Product):
    """Класс для описания трава газонная"""
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


if __name__ == "__main__":
    product_item = LawnGrass('Test3', 'Test3', 3000, 10, 'Canada', '1 year', 'light green')
    print(product_item.name)
    print(product_item.description)
    print(product_item.price)
    print(product_item.quantity)
    print(product_item.country)
    print(product_item.germination_period)
    print(product_item.color)

    product_item2 = LawnGrass('Test2', 'Test2', 3000, 10, 'Canada', '1 year', 'light green')
    print(product_item + product_item2)
