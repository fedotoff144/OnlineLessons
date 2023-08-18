# множества хранят только уникальные элементы!

# - my_set = {1, 2, 3, 4, 2, 5, 6, 7} # 2 встречается 2 раза поэтому вывод будет 1, 2, 3, 4, 5, 6, 7
# Изменяемое множество

# - my_f_set = frozenset((1, 2, 3, 4, 2, 5, 6, 7,))
# Неизменяемое множество

# not_set = {1, 2, 3, 4, 2, 5, 6, 7, ['a', 'b']} # TypeError: unhashable type: 'list'
# список является изменяемым объектом поэтому ловим ошибку


# -Метод add() - Добавляет элемент
my_set = {1, 2, 3, 4, 2, 5, 6, 7}
my_set.add(9)
print(my_set)  # {1, 2, 3, 4, 5, 6, 7, 9}
my_set.add(7)
print(my_set)  # {1, 2, 3, 4, 5, 6, 7, 9}
# my_set.add(9, 10) # TypeError: set.add() takes exactly one argument (2 given) need 1 element
my_set.add((9, 10))
print(my_set)  # {(9, 10), 1, 2, 3, 4, 5, 6, 7, 9}

# -Метод remove() - Удаляет элемент
my_set = {1, 2, 3, 4, 2, 5, 6, 7}
my_set.remove(5)
print(my_set)  # {1, 2, 3, 4, 6, 7}
# my_set.remove(10) # KeyError: 10 - don't have element 10


# -Метод discard() - Удаляет элемент
my_set = {1, 2, 3, 4, 2, 5, 6, 7}
my_set.discard(5)
print(my_set)  # {1, 2, 3, 4, 6, 7}
my_set.discard(10)  # don't have element 10 but don't have Errors
print(my_set)  # {1, 2, 3, 4, 6, 7}

# -Метод intersection() - Пересечение множеств, &
my_set = {1, 2, 3, 4, 2, 5, 6, 7}
other_set = {22, 4, 10, 7}
mix_set = my_set.intersection(other_set)
print(mix_set)  # {4, 7}
mix_set = my_set & other_set
print(mix_set)  # {4, 7}

# -Метод union() - Объединение множеств, |
my_set = {1, 2, 3, 4, 2, 5, 6, 7}
other_set = {22, 4, 10, 7}
mix_set = my_set.union(other_set)
print(mix_set)  # {1, 2, 3, 4, 5, 6, 7, 10, 22}
mix_set = my_set | other_set
print(mix_set)  # {1, 2, 3, 4, 5, 6, 7, 10, 22}

print(f'{my_set = }\n{other_set = }\n{mix_set = }')

# -Метод difference() - Разность множеств,
my_set = {1, 2, 3, 4, 2, 5, 6, 7}
other_set = {22, 4, 10, 7}
mix_set = my_set.difference(other_set)
print(mix_set)  # {1, 2, 3, 5, 6}
mix_set = my_set - other_set
print(mix_set)  # {1, 2, 3, 5, 6}

print(f'{my_set = }\n{other_set = }\n{mix_set = }')
# my_set = {1, 2, 3, 4, 5, 6, 7}
# other_set = {10, 4, 22, 7}
# mix_set = {1, 2, 3, 5, 6}


my_set = ({3, 4, 1, 2, 5, 6, 1, 7, 2, 7})
print(len(my_set)) # 7 - количество уникальных элементов
print(my_set - {1,2,3}) # {4, 5, 6, 7} - Разность множеств,
print(my_set.union({2,4,6,8})) # {1, 2, 3, 4, 5, 6, 7, 8} - Объединение множеств
print(my_set & {2,4,6,8}) # {2, 4, 6} - Пересечение множеств
print(my_set.discard(10)) # None - множество низменяемое поэтому ошибка
