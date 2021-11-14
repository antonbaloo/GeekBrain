# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.
import time

class TrafficLight:
    # __color = [['red', [31, 7]], ['yellow', [33, 2]], ['green', [32, 7]], ['yellow', [33, 2]]]


    # def running(self):
    #     position = 0
    #     while True:
    #         if position == 0:
    #             print("\r\033[31m 'Red'", end='')
    #             time.sleep(7)
    #             position += 1
    #         elif position == 1:
    #             print("\r\033[33m 'Yellow'", end='')
    #             time.sleep(2)
    #             position += 1
    #         elif position == 2:
    #             print("\r\033[32m 'Green'", end='')
    #             time.sleep(7)
    #             position += 1
    #         elif position == 3:
    #             print("\r\033[33m 'Yellow'", end='')
    #             time.sleep(2)
    #             position = 0

    __color = [['red', [31, 7]], ['yellow', [33, 2]], ['green', [32, 7]], ['yellow', [33, 2]]]

    def running(self):
        while True:
            for _ in (self.__color):
                print('\r\033[{}m {}'.format(_[1][0], _[0]), end='')
                time.sleep(_[1][1])




trc = TrafficLight()
trc.running()











