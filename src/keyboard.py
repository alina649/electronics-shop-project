from src.item import Item



class Language:
    __lang = "EN"

    #def __init__(self, name: str, price: float, quantity: int):
    #    super().__init__(name, price, quantity)

    @property
    def language(self):
        return self.__lang

    def change_lang(self):
        if self.__lang == "EN":
            self.__lang = "RU"
            return self
        else:
            self.__lang = "EN"
            return self
class KeyBoard(Language, Item):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)

#kb = KeyBoard('Dark Project KD87A', 9600, 5)
#print(repr(kb))

#print(KeyBoard.__mro__)


