# Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк,
# количества слов в каждой строке

#
# cntr_st = 0
# cntr_sym = 0
# with open('task2.txt', 'r') as f:
#     for _ in f:
#         cntr_st+=1
#         sym = _.split()
#         cntr_sym = len(sym)
#         print(f'В {cntr_st}-й строке {cntr_sym} слов(о)')
#     print(f'Всего {cntr_st} строк')


# этот вариант стырен с твоего решения! просто хотел прописать, что бы понять как он работает
# cntr = 0
# with open('task2.txt', 'r') as f:
#     info_file = [f'{num}. {" ".join(line.split())} - {len(line.split())}' for num, line  in enumerate(f, 1)]
#     print(*info_file, f'Всего строк {len(info_file)}', sep='\n')
