from src.product_class import Product


class Category:
    """Наименование, описание и список входящих продуктов"""

    name: str
    description: str
    __products: list

    category_count = 0

    product_count = 0

    def __init__(self, name, description, products):
        """Создание новой категории"""
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1

        Category.product_count += len(self.__products)

    def add_product(self, new_product: Product):
        if isinstance(new_product, Product):
            self.__products.append(new_product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        prod_lst = self.__products
        result = ""
        for el in prod_lst:
            result += f"{el.name}, {el.price} руб. Остаток: {el.quantity} шт.\n"
        return result

    @property
    def products_lst(self):
        prod_lst = self.__products
        return prod_lst

    def __str__(self):
        total = 0
        for product in self.__products:
            total += product.quantity
        return f"{self.name}, количество продуктов: {total} шт."
