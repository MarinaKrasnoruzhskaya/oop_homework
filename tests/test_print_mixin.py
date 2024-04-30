from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_print_mixin_init(capsys):
    Product("55 QLED 4K", "Фоновая подсветка", 123000.0, 7)
    message = capsys.readouterr()
    assert message.out.strip() == "Product('55 QLED 4K', 'Фоновая подсветка', 123000.0, 7)"

    Smartphone('Test1', 'Test1', 2000, 10, 1.5, 'Xiaomi', 10000, 'red')
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone('Test1', 'Test1', 2000, 10)"

    LawnGrass('Test1', 'Test1', 3000, 10, 'Canada', '1 year', 'light green')
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass('Test1', 'Test1', 3000, 10)"
