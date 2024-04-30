class PrintMixin:
    """ Класс-миксин """

    def __init__(self):
        """ Печатать в консоль информацию о том, от какого класса и с какими параметрами был создан объект """
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"
