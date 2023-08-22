# Итераторы
"""
iter(object[, sentinel])
Функция принимает на вход object поддерживающий
итерацию. Второй параметр функции iter — sentinel
передают для вызываемых объектов-итераторов.
"""

a = 42
# iter(a)  # TypeError: 'int' object is not iterable

data = [2, 4, 6, 8]
list_iter = iter(data)
print(list_iter)  # <list_iterator object at 0x000001FF9457ED00>

data = [2, 4, 6, 8]
list_iter = iter(data)
print(*list_iter)  # 2 4 6 8
print(*list_iter) # ничего не вернет так как iter() работает всего один раз


data = [2, 4, 6, 8]
# list_iter = iter(data, 6) # TypeError: iter(v, w): v must be callable

import functools

# открываем файл на чтение бинарной информации
f = open('mydata.bin', 'rb')

# используем чтение файла блоками по 16 байт
for block in iter(functools.partial(f.read, 16), b''): # partial - функция читает блоками
    print(block)
f.close()