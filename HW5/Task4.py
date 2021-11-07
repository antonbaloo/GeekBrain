# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

from translate import Translator as trn

with open('task4trnslt.txt', 'w') as t4t:
    with open('task4.txt', 'r') as t4:
        ru_trn = trn(to_lang='russian')
        my_data = {i.split()[2]: ru_trn.translate(i.split()[0]) for i in t4}
        print(my_data)
        for _ in my_data.items():
            t4t.write((": ".join(list(_))) + '\n')
