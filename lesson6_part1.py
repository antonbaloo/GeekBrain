# my_favorite_var = 2  # snake_case
# MyFavoriteVar = 20  # CamelCase
#
#
# class Auto:
#     # Атрибут уровня класса
#     auto_count = 0
#
#     def create_car(self, color, speed, name):  # метод  self -> объект
#         # Атрибуты уровня обьекта
#         self.color = color
#         self.speed = speed
#         self.name = name
#         # ferrari.speed = 350
#         Auto.auto_count += 1
#
#     def __init__(self, color, speed, name):  # метод  self -> объект | init - автозапуск метода
#         # тогда надо вводить в создание объекта  ferrari = Auto('red', 350, 'Феррари')
#         # Атрибуты уровня обьекта
#         self.color = color
#         self.speed = speed
#         self.name = name
#         # ferrari.speed = 350
#
#     def start(self):
#         print(f'{self.name} - начал движение')
#
#
# ferrari = Auto()
# zaz = Auto()
#
# print(zaz.auto_count, ferrari.auto_count)
#
# ferrari.create_car('red', 350, 'Феррари')
# zaz.create_car('blu', 100, 'Запорожец')  # вызов метода через объект
#
# Auto.create_car(zaz, 'blu', 100, 'Запорожец')  # вызов метода через класс
#
# print(ferrari.speed, ferrari.name, ferrari.color)
# print(zaz.speed, zaz.name, zaz.color)

# -------------------------------------------------------------------------------------


class Unit:

    def __init__(self, name, hp, dmg, armor, speed):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.armor = armor
        self.speed = speed

    def __add__(self, other):
        print(f'{self.name} hug {other.name}')

    def attack(self, target):
        target_damage = self.dmg - target.armor
        if target_damage > 0:
            print(f'{self.name} attack {target.name} wth damage {target.dmg}')
            target.hp -= target_damage
        else:
            print(f'{self.name} any damage to {target.name}')

    def run(self):
        print(f'{self.name}  run {self.speed}')


class FLyMixIn:
    def fly(self, item):
        print(f'{self.name} fly on {item}')


class Dragon(Unit, FLyMixIn): # Пример наследования классов (Unit, FlyMixIn)
    item = 'Крылья'

    def __init__(self, name, hp, dmg, armor, speed, fly_speed):  # вызов родителя локально (полиморфизм)
        Unit.__init__(self, name, hp, dmg, armor, speed)
        self.fly_speed = fly_speed

    def attack(self, item):
        print(f'{self.name}  fireball wth damage {self.dmg}')


class Witch(Unit,FLyMixIn):
    item = 'Метла'

    def spoilage(self):
        print(f'{self.name}  damage {self.dmg}')


orche = Unit('Орк', 150, 30, 15, 10)
elf = Unit('Эльф', 110, 60, 10, 30)

gorynych = Dragon('Горыныч', 500, 100, 100, 100, 50)
yaga = Witch('Яга', 110, 60, 10, 30)

enemy = [orche, gorynych, elf]
for unit in enemy:
    unit.attack(elf)

print(yaga + gorynych)