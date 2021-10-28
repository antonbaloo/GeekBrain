# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

data=input('Заполните список: ').split(' ')
list(data)
print(list(data))
print(len(data))
cntr = 0
while True:
    try:
        [data[cntr], data[cntr + 1]] = data[cntr + 1], data[cntr]
    except IndexError:
        break
    cntr += 2
    print(data)
    if cntr == len(data):
        break
    elif cntr >= len(data):
        break
