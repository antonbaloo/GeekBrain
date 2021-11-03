# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, first_param, second_param, third_param = argv

print("Имя скрипта: ", script_name)
print("Параметр 1: ", first_param)
print("Параметр 2: ", second_param)
print("Параметр 3: ", third_param)

# def salary_counter():
#     money_hour, time, bonus = map(float, argv[1:])
#     salary = (list_salary[0] * list_salary[1]) + list_salary[2]
#     print(salary)
#
# salary_counter()
