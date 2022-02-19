# 1
name = 'Екатерина'
print(name)

# 2
age = 18
print('возраст приходит с годами...', age)

# 3
print(name + name + name + name + name)
print(name * 5)

# 6
print(name[1:-1], name[::-1], name[-3:], name[0:5])

# 9
t = name.isalpha()
if not t:
    print('введите только имя без посторонних символов')
if age > 150:
    print('введите ваш реальный возраст')

# 7
s = 0
p = 1
while age > 0:
    n = age % 10
    s = n + s
    age = age // 10
    p = p * n
print(len(name), s, p)

# 8
sb = name.upper()
sl = name.lower()
st = name.capitalize()
print(sb, sl, st)
