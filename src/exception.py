class ZeroQuantityProduct(Exception):
    """ Класс ошибки - продукт с нулевым количеством"""
    def __init__(self, message):
        super().__init__(message)
