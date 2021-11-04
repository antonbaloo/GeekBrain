from sys import argv


def salary_counter():
    money_hour, time, bonus = map(float, argv[1:])
    print('Salary = {:.2f}'.format(money_hour * time + bonus))

salary_counter()
