from src.item import Item
class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_sim: int):
        super().__init__(name, price, quantity)
        self.number_sim = number_sim #количество поддерживаемых сим-карт

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        """Возвращает полное имя сотрудника. К атрибуту можно обращаться без ()."""
        return self.number_sim
    @number_of_sim.setter
    def number_of_sim(self, new_number_sim ):
        if int(new_number_sim) > 0 and isinstance(new_number_sim, int):
            self.number_sim = new_number_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")



