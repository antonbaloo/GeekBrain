# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_funk(a):
    b = a.title()
    return b


def int_funk_2(words):
    upper_list = []
    list_words = words.split(' ')
    for _ in list_words:
        upper = int_funk(_)
        upper_list.append(upper)
    new_words = ' '.join(upper_list)
    print(new_words)


words = input('ВВедите слова: ')

int_funk_2(words)