# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
#
# while True:
#     inpmonth = int(input('ВВедите номер месяца: '))
#     if inpmonth < 0 or inpmonth > 12:
#         print(' Неверное число. Поробуйте ещё')
#         continue
#     year = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#     for i in year:
#         if 3 <= i <= 5 and i == inpmonth:
#             print("Spring")
#             break
#         elif 6 <= i <= 8 and i == inpmonth:
#             print("Summer")
#             break
#         elif 9 <= i <= 11 and i == inpmonth:
#             print("Autumn")
#             break
#         elif (i == 1 or i == 2 or i == 12) and i == inpmonth:
#             print('Winter')
#             break


search_mounth = int(input('ВВедите месяц: '))
dict = {'winter': [1, 2, 12], 'spring': [3, 4, 5], 'Summer': [6, 7, 8], 'Autumn': [9, 10, 11]}

for i in dict:
    for j in dict.get(i):
        if j == search_mounth:
            print(i)
