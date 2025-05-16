def test_smartphone_init(subclass_phone):
    assert subclass_phone.model == "Note 11"
    assert subclass_phone.efficiency == 90.3
    assert subclass_phone.memory == 1024
    assert subclass_phone.color == "Синий"


def test_lawn_grass_init(subclass_grass):
    assert subclass_grass.country == "Россия"
    assert subclass_grass.germination_period == "7 дней"
    assert subclass_grass.color == "Зеленый"