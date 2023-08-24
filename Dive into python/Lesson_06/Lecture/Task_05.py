# хороший пример импорта
from super_module_right import *

SIZE = 49, 5

print(f'{SIZE = }\n{result = }')
# SIZE = (49, 5)
# result = 'в диапозоне от 1 до 6 получили 2'

print(f'{_secret = }')
# _secret = 'qwerty'

print(f'{__top_secret = }')
# __top_secret = '1saf23f1'

print(f'{func(100, 200) = }\n{randint(10, 20) = }')
# func(100, 200) = 'в диапозоне от 100 до 200 получили 111'
# randint(10, 20) = 20


def func(a: int, b: int) -> int:
    return a + b


print(f'{func(100, 200) = }')
# func(100, 200) = 300
