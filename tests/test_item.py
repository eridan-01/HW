"""Здесь надо написать тесты с использованием pytest для модуля item."""
import csv

import pytest

from src.item import Item
from src.phone import Phone


class TestItem:
    def test_init_item(self, item):
        assert item.price == 10000.0
        assert item.name == "Смартфон"
        assert item.quantity == 20
        assert Item.all == [item]

    def test_total_price(self, item):
        assert item.calculate_total_price() == 200000.0
        assert isinstance(item.calculate_total_price(), float)

    def test_apply_discount(self, item):
        item.pay_rate = 0.8
        item.apply_discount()
        assert item.price == 8000.0

    def test_instantiate_from_csv(self):
        Item.instantiate_from_csv()
        item1 = Item.all[1]
        assert len(Item.all) == 5
        assert item1.name == 'Computer'

    def test_string_to_number(self):
        assert Item.string_to_number('5') == 5
        assert Item.string_to_number('5.0') == 5
        assert Item.string_to_number('5.5') == 5

    def test_repr_item(self):
        item1 = Item("Смартфон", 10000, 20)
        assert repr(item1) == "Item(Смартфон, 10000, 20)"

    def test_str_item(self):
        item1 = Item("Смартфон", 10000, 20)
        assert str(item1) == 'Смартфон'

    def test_sum_quantity(self):
        phone1 = Phone("iPhone 14", 120_000, 5, 2)
        item1 = Item("Смартфон", 10000, 20)
        assert item1 + phone1 == 25

    def test_instantiate_from_csv_(self):
        with open('items.csv') as file:
            read = csv.DictReader(file)
            assert read is not None
            for x in read:
                assert "name" in x
                assert "price" in x
                assert "quantity" in x

    def test_instantiate_from_csv_file_not(self):
        with pytest.raises(FileNotFoundError):
            Item.instantiate_from_csv()
