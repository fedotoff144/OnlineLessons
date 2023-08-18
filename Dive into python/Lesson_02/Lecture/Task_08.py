# неявное преобразование к типу
DEFAULT = 42
num = int(input('Enter level you want: '))
level = num or DEFAULT
print(level)

# *************************

name = input('Enter your name: ')

if name:
    print('Hi' + name)
else:
    print('Hi anonimus')

# *************************

data = [0, 1, 2, 3, 4, 5, 18, 20]
while data:
    print(data.pop())
