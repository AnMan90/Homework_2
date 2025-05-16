import pytest

from src.product_class import Product


def test_product_init(product_xiaomi):
    assert product_xiaomi.name == "Xiaomi Redmi Note 11"
    assert product_xiaomi.description == "1024GB, Синий"
    assert product_xiaomi.price == 31000.0
    assert product_xiaomi.quantity == 14


def test_price_setter(product_samsung, capsys):
    product_samsung.price = -1000
    assert capsys.readouterr().out == "Цена не должна быть нулевая или отрицательная\n"
    product_samsung.price = 1000
    assert product_samsung.price == 1000


def test_new_product():
    product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_mag_str(product_xiaomi):
    assert str(product_xiaomi) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."


def test_mag_add(product_xiaomi, product_samsung):
    assert product_xiaomi + product_samsung == 1334000


def test_mag_add_error(product_xiaomi):
    with pytest.raises(TypeError):
        res = product_xiaomi + 1
