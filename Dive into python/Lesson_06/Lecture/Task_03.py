# импортируем конкретные модули и добавляем их псевдонимы
from sys import builtin_module_names as bmn, path as p

print(bmn)  # builtin_module_names
print(*p, sep='\n')  # path

# после указания псевдонимов обращение по полному имени невозможно
# print(builtin_module_names) # NameError: name 'builtin_module_names' is not defined
# print(*path, sep='\n') # NameError: name 'path' is not defined
