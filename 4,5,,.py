# 4
name = input('введите ваше имя:')
age = input('введите ваш возраст:')
print('здарова,', name, 'возраст приходит с годами')

# 5
if int(age) > 18:
    joke = 'пора на пенсию'
else:
    joke = 'уже собрал(а) рюкзак в школу?'
print('здарова,', name, '.', joke)
