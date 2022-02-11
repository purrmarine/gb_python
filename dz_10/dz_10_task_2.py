# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
# одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма(2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания. Реализовать абстрактные
# классы для основных классов проекта и проверить работу декоратора @property.
from abc import abstractmethod, ABC


class Clothes(ABC):
    fabric_consumption = 0

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        self.name = name
        self.V = size
        Coat.fabric_consumption += self.consumption

    @property
    def consumption(self):
        return self.V / 6.5 + 0.5, 2


class Suit(Clothes):
    def __init__(self, name, height):
        self.name = name
        self.H = height
        Suit.fabric_consumption += self.consumption

    @property
    def consumption(self):
        return self.H / 6.5 + 0.5, 2


coat_1 = Coat("пальто 1", 50)
print(coat_1.consumption)
print(coat_1.fabric_consumption)

coat_2 = Coat("пальто 2", 42)
print(coat_2.consumption)
print(coat_2.fabric_consumption)

suit_1 = Suit("Костюм 1", 170)
print(suit_1.consumption)
print(suit_1.fabric_consumption)

suit_2 = Suit("Костюм 2", 190)
print(suit_2.consumption)
print(suit_2.fabric_consumption)
