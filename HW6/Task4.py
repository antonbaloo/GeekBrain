# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f'{self.speed}km/h')

    def go_car(self):
        print(f'Car {self.name} is starting to drive')

    def stop_car(self):
        print(f'Car {self.name} is stopped')

    def turn_car(self, side):
        print(f'{self.name} turn to {"right" if side == "right" else  "Left"} ')


class TownCar(Car):
    speed_limit = 60

    def show_speed(self):
        print(f'{self.name}  is over speed limit' if self.speed > TownCar.speed_limit \
                  else f'{self.name} speed is {self.speed}')


class WorkCar(Car):
    speed_limit = 40

    def show_speed(self):
        if int(self.speed()) > 40:
            print(f'{self.name}  is over speed limit' if {self.speed} > WorkCar.speed_limit \
                      else f'{self.name} driving {self.speed}km/h')


class SportCar(Car):
    speed_limit = 100

    def show_speed(self):
        print(f'Полиция не видит нарушений в превышении скорости! Это машина мэра!' if self.speed > SportCar.speed_limit \
                  else f'{self.name} speed is {self.speed}km/h')


class Police(Car):
    def __init__(self, color, name, speed, is_police=True):
        super().__init__(color, name, speed, is_police)

    def pursuit(self):
        print(f'\033[31m Режим преследования включён')


ferrari = SportCar(160, 'red', 'Ferrari')
Hundai = TownCar(70, 'blu', 'Tucson')
Kengoo = WorkCar(60, 'white', 'Reno')
police = Police('Blu', 'LAPD', 160)

# ferrari.go_car()
# ferrari.show_speed()

Hundai.show_speed()
Kengoo.turn_car('left')
police.pursuit()
