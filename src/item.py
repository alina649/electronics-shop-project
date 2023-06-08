import csv
import os


class InstantiateCSVError(Exception):
    """Класс-исключение для отлавливания ошибки, если файл поврежден"""

    def __init__(self):
        self.message = '_InstantiateCSVError: Файл item.csv поврежден_'


class FileNotFoundCSVError(InstantiateCSVError):
    """Класс-исключение для отлавливания ошибки, если файл отсутствует"""

    def __init__(self):
        self.message = '_FileNotFoundError: Отсутствует файл item.csv_'


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


    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return int(self.quantity) + int(other.quantity)
        raise ValueError('Нельзя складывать.')


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if len(value) > 10:
            raise Exception('Длина товара превышает 10 символов.')
        self._name = value

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
    def csv_reader(cls, filename):
        '''
        класс-метод, читающий файл и инициализирующий экземпляры
        класса `Item` данными из этого файла
        '''

        try:
            cls.all.clear()

            with open(filename, newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    cls(row['name'], row['price'], row['quantity'])

                    if not row['name'] or not row['price'] or not row['quantity']:
                        raise InstantiateCSVError
                if len(cls.all) <= 0:
                    raise InstantiateCSVError

        except FileNotFoundError:
            raise FileNotFoundCSVError
        except KeyError:
            raise InstantiateCSVError

    @classmethod
    def instantiate_from_csv(cls) -> None:
        '''класс-метод, инициализирующий данными из файла _src/items.csv'''
        try:
            cls.csv_reader('../src/items.csv')
        except FileNotFoundCSVError as ex:
            print(ex.message)
        except InstantiateCSVError as ex:
            print(ex.message)

    @staticmethod
    def string_to_number(num):
        """статический метод, возвращающий число из числа-строки"""
        numb = float(num)
        return int(numb)