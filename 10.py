task = input('решите пример: 2*2+2. Ответ:')
if int(task) == 6:
    print('верно')
else:
    print('неверно. попробуйте снова')
    while int(task) != 6:
        task = input('введите новый ответ: ')
    if int(task) == 6:
        print('верно')