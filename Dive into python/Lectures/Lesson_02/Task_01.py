a = 4
print(type(a), id(a)) # type(a) тип переменной, id(a) номер ячейки в памяти
a = 'Hello world'
print(type(a), id(a)) # type(a) тип переменной, id(a) номер ячейки в памяти
a = 3.14
print(type(a), id(a)) # type(a) тип переменной, id(a) номер ячейки в памяти

# isinstance() проверка вляется ли объект нужным нам типом
data = 42
print(isinstance(data, int)) # проверка на принадлежность типу int
data = True
print(isinstance(data, int)) # True идет от int, потому вывод True
data = 3.14
print(isinstance(data, (int, float, complex))) # проверка сразу на несколько типов

# isinstance() проверка вляется ли объект нужным нам типом
num = 2+2+2
digit = 36/6
print(num, digit) # 6 6.0
print(num == digit) # True
print(num is digit) # False