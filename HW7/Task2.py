# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class CLoses(ABC):

    @abstractmethod
    def amount_cloth(self):
        pass


class Palto(CLoses):
    def __init__(self, size):
        self.size = size

    @property
    def amount_cloth(self):
        return self.size/6.5 + 0.5


class Costume(CLoses):
    def __init__(self, height):
        self.height = height

    @property
    def amount_cloth(self):
        return 2 * self.height + 0.3


class SumCloth(CLoses):

    def amount_cloth(self):
        pass

    def __add__(self, other):
        self.amount_cloth + other.amount_cloth

    def __iadd__(self, other):
        self.amount_cloth += other.amount_cloth



nike = Costume(180)
zara = Palto(160)
sum_cloth = SumCloth()

print(nike.amount_cloth)
print(zara.amount_cloth)

print(nike.amount_cloth + zara.amount_cloth)
