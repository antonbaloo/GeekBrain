# # class Auto:
# #
# #     def info(): # статичный метод. существуют сами по себе и ни с чем не взаимоджействует работает без self
# #         print('Hi')
# #
# # Auto.info()
# #
# # class VK:
# #
# #     @staticmethod # статичные классы закрыты в своих классах вызываются напрямую через имыя класса
# #     def send_message():
# #         print('Send mes vk')
# #
# # class Telegram:
# #     @staticmethod
# #     def sen_message():
# #         print('Send mes vk')
# #
# # VK.send_message()
#
#
# # class A:
# #     count = 0
# #
# #     @classmethod  # cls - принятие в метод класса а не объекта (вместо self  пишется cls) пишется первым аргументом
# #     def increment_count(cls): # cls = class A (тоесть используется переменна от класса А -> count = 0)
# #         cls.count += 1
# #
# #
# # class B(A):
# #     count = 0
# #
# #
# # A.increment_count()
# # B.increment_count()
# # print(A.count, B.count)
# #
# #
# # class User:
# #     def __init__(self, name, login, passwd, email):
# #         self.name = name
# #         self.login = login
# #         self.passwd = passwd
# #         self.email = email
# #
# #     def on_get_data(self):
# #         print(f"имя: {self.name}, логин: {self.login}, "
# #             f"пароль: {self.passwd}, email: {self.email}")
# #
# #
# # u = User("Ivan Ivanov", "IvIv", "11111", "iviv@mail.ru")
# # u.on_get_data()
# # print(f"__name__ - {User.__name__}, \n __module__ - {User.__module__}, \n"
# #     f"__dict__ - {User.__dict__}, \n __bases__ - {User.__bases__}, \n"
# #     f"__doc__ - {User.__doc__}")
#
#
# # Исключения
# import traceback
#
# def summator(*args):
#     for i in args:
#         try:
#             print(10 / i)
#         except (ZeroDivisionError, TypeError):
#             with open('errors.txt', 'a') as f:
#                 f.write(traceback.format_exc() + '\n')
#             print('Bad data')
#         except Exception as e:
#             print(f'Fail - {e}')
#
#
#
# def main():
#     print('start')
#     summator(10, 5, 2, 0, 20)
#     print('finish')
#
#
# main()

# Создание своей ошибки
# class AutoCrushError(Exception): # Атрибут Exception говорит о создании ошибки
#     def __init__(self, text):
#         self.text = text
#
#
# class Auto:
#
#     def __add__(self, other):
#         raise AutoCrushError('Авария')
#
#
# zaz = Auto()
# ferrari = Auto()
#
# zaz + ferrari


# PIP

import requests

response = requests.get('https://wikipedia.org')
print(response.text)