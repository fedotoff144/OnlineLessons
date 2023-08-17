# Функция list и квадратные скобки [ ]
# Создание списков
# - Квадратные скобки [ ]
# Доступ к элементу по индексу
# - Метод append()
# Добавление одного элемента в конец
# - Метод extend()
# Добавление нескольких элементов в конец
# - Метод pop()
# Удаление элемента по индексу
# - Метод count()
# Подсчёт вхождения элемента
# - Метод index()
# Индекс первого вхождения элемента
# - Метод insert()
# Вставка элемента по индексу
# - Метод remove()
# Удаление элемента по значению
import copy

list_1 = list()  # создание пустого списка без элементов
list_2 = list((3.14, 'Hello world', True))  # картеж сам распакуется
list_3 = []
list_4 = [3.14, 'Hello world', True]

print(list_4[0])  # 3.14
print(list_4[-1])  # True
# print(list_4[-10]) # Error list index out of range


# append
a = 5
b = 'text'
some_list = [0, 9, 8]

my_list = [1, 2, 3, 4]
my_list.append(a)
my_list.append(b)
my_list.append(some_list)

print(my_list)  # [1, 2, 3, 4, 5, 'text', [0, 9, 8]]

# extend
a_1 = 5
b_1 = 'text'
some_list_1 = [0, 9, 8]
my_list_1 = [None]  # list with None

# my_list_1.extend(a_1) # error 'int' object is not iterable
my_list_1.extend(b_1)
my_list_1.extend(some_list_1)
print(my_list_1)

# pop
my_list_2 = [1, 2, 3, 4]
num = my_list_2.pop()  # last element
num_1 = my_list_2.pop(2)  # index

# Сортировка:
# - Функция sorted()
# - Метод sort()
#
# Разворот:
# - Функция reversed()
# - Метод reverse()
# - Синтаксический сахар [::-1]

my_list_3 = ['t', 'e', 'x', 't', 0, 9, 8]
# my_list_3.sort() # error '<' not supported between instances of 'int' and 'str'
# res = sorted(my_list_3) # error '<' not supported between instances of 'int' and 'str'


# sort()
my_list_4 = [9, 2, 8, 4]
sort_list = sorted(my_list_4)  # [2, 4, 8, 9]
sort_list_1 = sorted(my_list_4, reverse=True)  # [9, 8, 4, 2]
print(sort_list, sort_list_1, sep='\n')

# не создавая новый объект
my_list_4.sort()  # [2, 4, 8, 9]
my_list_4.sort(reverse=True)  # [9, 8, 4, 2]

# reversed()
my_list_5 = [9, 2, 8, 4]
res_1 = reversed(my_list_5)  # <list_reverseiterator object at 0x000002BED2743FD0>
print(res_1)
rev_list = list(reversed(my_list_5))  # [4, 8, 2, 9]
print(rev_list)

my_list_5.reverse()  # [4, 8, 2, 9]
# or
# list[::-1] start:stop:step
new_list = my_list_5[::-1]  # reverse of list [4, 8, 2, 9]

cut_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(cut_list[2:7:2])  # [6, 10, 14]
print(cut_list[:7:2])  # [2, 6, 10, 14]
print(cut_list[2::2])  # [6, 10, 14, 18]
print(cut_list[2:7:])  # [6, 8, 10, 12, 14]
print(cut_list[8:3:-1])  # [18, 16, 14, 12, 10]
print(cut_list[3::])  # [8, 10, 12, 14, 16, 18, 20]
print(cut_list[:7:])  # [2, 4, 6, 8, 10, 12, 14]

list_5 = [2, 4, 6, 8, 10, 12]
copy_list = list_5
# внескение изменений в list_5 отразится на список copy_list
# так как списки ссылаются на один и тот же объект в ОЗУ

list_6 = [2, 4, 6, 8, 10, 12]
copy_list_1 = list_6.copy()
# внескение изменений в list_6 не отразится на список copy_list_1
# так как списки имеют разное расоложение с ОЗУ
# но если внутри имееются списки или словари то их изменение повлияет
# на список copy_list_1 так как copy() поверхностная функция

copy_list_2 = copy.deepcopy(list_6)
# внескение изменений в list_6 не отразится на список copy_list_2
# так как списки имеют разное расоложение с ОЗУ
# и даже именение вложенных списков в list_6 не важно какой глубины
# не повлияет на copy_list_2


# len()
my_list_6 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
matrix = [[1, 2, 3, 4], [6, 7, 8, 9, 0], [10, 11, 12]]
print(len(my_list_6)) # 9
print(len(matrix)) # 3
print(len(matrix[1])) # 5

