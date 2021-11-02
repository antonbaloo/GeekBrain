# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_funk(a, b, c):
    my_list = [int(a), int(b), int(c)]
    my_list.remove(min(my_list))
    print(sum(my_list))


my_funk(3, 5, 15)