# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

a = int(input('Min amount of km: '))
b = int(input('Target of amount of km: '))
counter_day = 1
while True:
    print('День {}: {:.2f}km'.format(counter_day, a))
    if a >= b:
        print('На ' + str(counter_day) + '-й день спортсмен достиг результат')
        break
    a += (a * 0.1)
    counter_day += 1



