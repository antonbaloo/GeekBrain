# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

data_dict = {
    'name': input('Enter name: '),
    'Surname': input('Enter surname: '),
    'BRTY': input('Enter birth year: '),
    'City': input('Enter city: '),
    'Email': input('Enter Email: '),
    'Phone': input('Enter phone number: ')
}


def people_info(**some):
    return ' '.join(some.values())


print(people_info(**data_dict))
