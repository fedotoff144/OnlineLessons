"""
Декоратор с параметрами
Три уровня вложенности позволяют передавать аргументы в декоратор
"""
import time
from typing import Callable


# first internal level
def count(num: int = 1):
    # second internal level
    def deco(func: Callable):
        # thirt internal level
        def wrapper(*args, **kwargs):
            time_for_count = []
            result = None
            for _ in range(num):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                stop = time.perf_counter()
                time_for_count.append(stop - start)
                print(f'Measurement result {time_for_count}')
            return result

        return wrapper

    return deco


@count(10)
def factorial(n: int) -> int:
    print(f'Calculate factorial for {n}')
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


print(f'{factorial(10) = }')
print(f'{factorial(20) = }')