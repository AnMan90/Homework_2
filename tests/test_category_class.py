from src.category_class import Category


def test_category_init(category_phone, product_samsung, product_iphone, product_xiaomi):
    assert category_phone.name == "Смартфоны"
    assert (
        category_phone.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_phone.products_lst == [product_samsung, product_iphone, product_xiaomi]


def test_category_count(category_phone):
    assert Category.category_count == 1


def test_product_count(category_phone):
    assert Category.product_count == 3


def test_products(product_samsung):
    cat = Category("Смартфоны", "", [])
    cat.add_product(product_samsung)
    assert cat.products == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
