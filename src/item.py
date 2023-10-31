import csv
from pathlib import Path
PATH = Path(__file__).parent.resolve().absolute()


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})'

    def __str__(self):
        return f'{self.name}'

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            self.__name = new_name[:10]

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        encoding = [
            'utf-8',
            'cp500',
            'utf-16',
            'GBK',
            'windows-1251',
            'ASCII',
            'US-ASCII',
            'Big5'
        ]

        correct_encoding = ''

        for enc in encoding:
            try:
                f = open(PATH / "items.csv", encoding=enc).read()
            except (UnicodeDecodeError, LookupError):
                pass
            else:
                correct_encoding = enc
                break
        with open(PATH / "items.csv", encoding=correct_encoding) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(**row)

    @staticmethod
    def string_to_number(number):
        return int(float(number))