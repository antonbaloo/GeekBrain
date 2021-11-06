class MyList(list):
    def append(self, __object):
        print(f'Элемент {__object} был добавлен')
        list.append(self, __object)



data = MyList()
data.append('Hi')
data.append('asdasd')

print(data)