class Product:
    """ Наименование, описание, цена и количество продукта """
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """ Создание нового продукта """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
