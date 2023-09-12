"""
Дополнительные переменные в декораторе

Аналогично замыканию переменных в функции,
декоратор может замыкать переменные в себе
"""
from typing import Callable


def cache(func: Callable):
    _cache_dict = {}

    def wrapper(*args):
        if args not in _cache_dict:
            _cache_dict[args] = func(*args)
        return _cache_dict[args]

    return wrapper


@cache
def factorial(n: int) -> int:
    print(f'Calculate factorial for {n}')
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


print(f'{factorial(10) = }')
print(f'{factorial(15) = }')
print(f'{factorial(10) = }')
print(f'{factorial(20) = }')
print(f'{factorial(10) = }')
print(f'{factorial(20) = }')
# Calculate factorial for 10
# factorial(10) = 3628800
# Calculate factorial for 15
# factorial(15) = 1307674368000
# factorial(10) = 3628800
# Calculate factorial for 20
# factorial(20) = 2432902008176640000
# factorial(10) = 3628800
# factorial(20) = 2432902008176640000