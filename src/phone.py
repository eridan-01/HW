from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.price}, {self.quantity}, {self.number_of_sim})'

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise TypeError("Складывать можно только объекты классов с родительским классом Item")

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if isinstance(value, int) and value >= 0:
            self.__number_of_sim = value
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

