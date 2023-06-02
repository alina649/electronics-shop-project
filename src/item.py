import csv
import os


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
        self._name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

    #def __add__(self, other):
    #    if not isinstance(other, Item):
    #        raise ValueError('Нельзя складывать.')
    #    return int(self.quantity) + int(other.quantity)
    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return int(self.quantity) + int(other.quantity)
        raise ValueError('Нельзя складывать.')





    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        try:
            if len(new_name) <= 10:
                self._name = new_name
        except Exception:
            return ("длина наименования товара больше 10 символов")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.quantity * self.price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        cls.all.clear()
        #dir_path = os.path.dirname(os.path.realpath(__file__))
        #with open(dir_path + '/items.csv', encoding='utf-8') as csvfile:
        file = os.path.abspath('../src/items.csv')
        with open(file, encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row['name'], row['price'], row['quantity'])

    @staticmethod
    def string_to_number(num):
        """статический метод, возвращающий число из числа-строки"""
        numb = float(num)
        return int(numb)