# Генераторы
# генераторы списков

"""
list_comp = [expression for expr in
sequense1 if condition1 ...]
Генератор списков формирует list заполненный
данным и присваивает его переменной.
"""


# Listcomprehentions
my_listcomp = [chr(i) for i in range(97, 123)]
print(
    my_listcomp)  # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for char in my_listcomp:
    print(char)
