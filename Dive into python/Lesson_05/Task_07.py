"""
next(iterator[, default])
На вход функция принимает итератор,
который вернула функция iter.
Второй параметр функции next — default
нужен для возврата значения по умолчанию
вместо выброса исключения StopIteration.
"""

data = [2, 4, 6, 8]
list_iter = iter(data)

print(next(list_iter)) # 2
print(next(list_iter)) # 4
print(next(list_iter)) # 6
print(next(list_iter)) # 8
# print(next(list_iter))  # StopIteration


data = [2, 4, 6, 8]
list_iter = iter(data)

print(next(list_iter, 42)) # 2
print(next(list_iter, 42)) # 4
print(next(list_iter, 42)) # 6
print(next(list_iter, 42)) # 8
print(next(list_iter, 42)) # 42
print(next(list_iter, 42)) # 42