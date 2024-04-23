import pytest


def test_smartphone_init(first_smartphone):
    assert first_smartphone.name == "Test1"
    assert first_smartphone.description == "Test1"
    assert first_smartphone.price == 2000
    assert first_smartphone.quantity == 10
    assert first_smartphone.efficiency == 1.5
    assert first_smartphone.model == 'Xiaomi'
    assert first_smartphone.memory == 10000
    assert first_smartphone.color == 'red'


def test_product_add(first_smartphone, second_smartphone):
    assert first_smartphone + second_smartphone == 65_000
