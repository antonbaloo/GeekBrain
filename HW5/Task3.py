# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open('task3.txt', 'r') as file:
    salary = {i.split()[0]: i.split()[1] for i in file}
    for name, money in salary.items():
        if int(money) < 20000:
            print(name)
    middle = sum(map(int, salary.values())) / len(salary.values())
    print('{:.2f}'.format(middle))