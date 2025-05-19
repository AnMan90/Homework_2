from src.base_product import BaseProduct
from src.mixin import MixinLog


class Product(BaseProduct, MixinLog):
    """Наименование, описание, цена и количество продукта"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Создание нового продукта"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    @classmethod
    def new_product(cls, product: dict):
        """Создание нового объекта класса Product из словаря"""
        prod = Product(**product)
        return prod

    @property
    def price(self):
        """Метод геттер возвращает цену продукта"""
        return self.__price

    @price.setter
    def price(self, price):
        """В методе сеттер реализована проверка цены и вывод результата в консоль"""
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price

    def __str__(self):
        """Добавляет строковое отображение для класса Product"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Метод сложения произведений цены и количества товаров"""
        if type(other) is type(self):
            return self.__price * self.quantity + other.price * other.quantity
        else:
            raise TypeError
