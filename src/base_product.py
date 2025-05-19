from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """ Абстрактный класс для дочернего класса Product """

    @classmethod
    @abstractmethod  # pragma: no cover
    def new_product(cls, *args, **kwargs):
        pass
