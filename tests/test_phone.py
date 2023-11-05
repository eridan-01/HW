from src.item import Item
from src.phone import Phone


class TestPhone:
    def test_str_item(self):
        phone1 = Phone("iPhone 14", 120_000, 5, 2)
        assert str(phone1) == 'iPhone 14'

    def test_repr_item(self):
        phone1 = Phone("iPhone 14", 120_000, 5, 2)
        assert repr(phone1) == "Phone(iPhone 14, 120000, 5, 2)"

    def test_sum_sim(self):
        phone1 = Phone("iPhone 14", 120_000, 5, 2)
        assert phone1 + phone1 == 10
