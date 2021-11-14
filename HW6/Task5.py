# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('НАчало отрисовки')

class Pen(Stationery):

    def draw(self, sym):
        self.sym = sym
        print(f'Ручка рисует {self.sym}')


class Pencil(Stationery):

    def draw(self, collor):
        self.collor = collor
        print(f'ВЫ написали {self.title} {self.collor}(м) цветом')


class Handle(Stationery):

    def draw(self, target, reason):
        self.target = target
        self.reason =reason
        print(f'Вы подчеркнули {self.target}. Потому что там {self.reason}.')


white_pen = Pen('White Pen')
blue_pencil = Pencil('BLue Pencil')
red_handle = Handle('Red Handle')

white_pen.draw('=')
blue_pencil.draw('синий')
red_handle.draw('предложение', 'ошибка')