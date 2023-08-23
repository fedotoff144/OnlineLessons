# плохой пример импорта
from super_module_wrong import *

SIZE = 49, 5

print(f'{SIZE = }\n{result = }')
# SIZE = (49, 5)
# result = 'в диапозоне от 1 до 6 получили 2'

# ЗАЩИЩЕННЫЕ И ПРИВАТНЫЕ ПЕРЕМЕННЫЕ НЕ ИМПОРТИРУЮТСЯ ЧЕРЕЗ *
# print(f'{z = }')
# NameError: name 'z' is not defined

# print(f'{_secret = }')
# NameError: name '_secret' is not defined

# print(f'{__top_secret = }')
# NameError: name '__top_secret' is not defined

print(f'{func(100, 200) = }\n{randint(10, 20) = }')
# func(100, 200) = 'в диапозоне от 100 до 200 получили 200'
# randint(10, 20) = 12


def func(a: int, b: int) -> int:
    return a + b


print(f'{func(100, 200) = }')
# func(100, 200) = 300
