"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from pytest import fixture

from src.item import Item

@fixture
def item():
    return Item("Смартфон", 10000, 20)

def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200000

def test_apply_discount(item):
    item.apply_discount()
    assert item.price == 10000.0

def test_name():
    item = Item('Телефон', 10000, 5)
    item.name = 'Смартфон'
    item.name = 'СуперМегаПуперСмартфог'
    assert item.name == 'Смартфон'

def test_instantiate_from_csv():
    item = Item('Телефон', 10000, 5)
    item.instantiate_from_csv()
    assert len(Item.all) == 5

def test_string_to_number():
    assert Item.string_to_number('1') == 1
    assert Item.string_to_number('1.0') == 1
    assert Item.string_to_number('1.5') == 1

def test_str_repr():
    item1 = Item("Смартфон", 200, 10)
    assert repr(item1) == "Item('Смартфон', 200, 10)"
    assert str(item1) == 'Смартфон'






