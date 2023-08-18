# изменяемы объекты
# list, bytearray, frozenset, dict

# неизменяемые объекты
# int, str, bool, float, complex, tuple, bytes, set

txt = 'Hello world'
# txt[5] = '_' # error неизменяемый объект
txt = txt.replace(' ', '_') # на самом деле создает новый объект а не изменяет старый

a = c = 2 # обе переменных указывают на один и тот же объект
b = 3

# проверкой на изменяемость/неизменяемость служит просто вычисление хэш суммы
# у неизменяемых объектов хэш вычисляется, у неизменяемых - нет
x = 10
y = 'text'
z = 3.14
my_list = [1, 2, 3, 4]
print(hash(x), hash(y), hash(z))
print(hash(my_list)) # error

