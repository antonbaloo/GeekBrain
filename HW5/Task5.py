# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint as ri

with open('task5.txt', 'w+') as f:
    my_list = [str(ri(1, 20)) for _ in range(20)]
    f.write(' '.join(my_list))
    print(sum(map(int, my_list)))