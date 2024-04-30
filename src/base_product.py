from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """ Базовый абстрактный класс"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass
