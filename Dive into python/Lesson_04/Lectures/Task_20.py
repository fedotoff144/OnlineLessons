"""
✔ locals() Функция возвращает словарь
переменных из локальной области
видимости на момент вызова функции.
✔ globals() Функция возвращает словарь
переменных из глобальной области
видимости, т.е. из пространства модуля.
✔ vars() Функция без аргументов работает
аналогично функции locals(). Если передать
в vars объект, функция возвращает его атрибут
__dict__. А если такого атрибута нет у объекта,
вызывает ошибку TypeError.
"""

"""locals()"""
SIZE = 10 # не видим потому что она находится за пределами функции где вызывается locals()


def func(a, b, c):
    x = a + b
    print(locals()) # {'a': 1, 'b': 2, 'c': 3, 'x': 3}
    z = x + c # не видим потому что переменная создана после вызова locals()
    return z


func(1, 2, 3)

"""globals()"""
SIZE = 10  # не видим потому что она находится за пределами функции где вызывается locals()


def func(a, b, c):
    x = a + b
    print(globals())  # {'a': 1, 'b': 2, 'c': 3, 'x': 3}
    z = x + c  # не видим потому что переменная создана после вызова locals()
    return z


print(globals())
print(f'{func(1,2,3) = }') # func(1,2,3) = 6

# изменяем словарь globals()
x = 42
global_dict = globals()
global_dict['x'] = 73
print(f'{x = }') # x = 73