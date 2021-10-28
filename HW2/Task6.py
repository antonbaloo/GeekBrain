# Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
list_data = []
counter = 1
while True:
    dict_data = {'название': input('ВВедите название товара: '),
            'цена': input(' ВВедите цену на товар: '),
            'количество': input('ВВедите количество товара: '),
            'единица измерения': input('ВВедите единицу  измерения товара: ')
            }
    tuple_data = (counter, dict_data)
    list_data.append(tuple_data)
    counter += 1
    end_word = input('Закончить ввод? Y/N ')
    if end_word == 'Y':
        break
    else:
        continue
# print(list_data)
name_list = []
price_list = []
amount_list = []
unit_list = []
for i in list_data:
    i = list(i)
    name_list.append(i[1].get('название'))
    price_list.append(i[1].get('цена'))
    amount_list.append(i[1].get('количество'))
    unit_list.append(i[1].get('единица измерения'))
print('"название" : ', name_list)
print('"цена" : ', price_list)
print('"количество" : ', amount_list)
print('"единица измерения" : ', list(set(unit_list)))

