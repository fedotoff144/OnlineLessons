"""
✔ max(iterable, *[, key, default])или max(arg1,
arg2, *args[, key]) Функция принимает на вход
итерируемую последовательность или несколько
позиционных элементов и ищет максимальное из них.
✔ min(iterable, *[, key, default]) или min(arg1,
arg2, *args[, key]) Функция работает аналогично
max, но ищет минимальный элемент.
✔ sum(iterable, /, start=0)
Функция принимает объект итератор и подсчитывает
сумму всех элементов. Ключевой аргумент start задаёт
начальное значение для суммирования
"""

"""max(iterable, *[, key, default])или max(arg1, arg2, *args[, key])"""
list_1 = []
list_2 = [42, 256, 73]
list_3 = [('Ivan', 125_000), ('Nikolaj', 96_000), ('Piter', 109_000)]
print(max(list_1, default='empty'))  # чтобы избежать ошибок дефолтное значение для вывода 'empty'
print(max(*list_2))  # возвращаем самое большое значение в списке
print(max(list_3, key=lambda x: x[1]))  # перебор по ключам, но ищет макс значение в кортеже :x[1]

"""min(iterable, *[, key, default]) или min(arg1, arg2, *args[, key])"""
list_1 = []
list_2 = [42, 256, 73]
list_3 = [('Ivan', 125_000), ('Nikolaj', 96_000), ('Piter', 109_000)]
print(min(list_1, default='empty'))  # чтобы избежать ошибок дефолтное значение для вывода 'empty'
print(min(*list_2))  # возвращаем минимальное значение в списке
print(min(list_3, key=lambda x: x[1]))  # перебор по ключам, но ищет минимальное значение в кортеже :x[1]

"""sum(iterable, /, start=0)"""
my_list = [42, 256, 73]
print(sum(my_list)) # 371
print(sum(my_list, start=1024)) #1395 (my_ list + 1024)

