"""
Декораторы
"""
import time
from typing import Callable


def main(func: Callable):
    def wrapper(*args, **kwargs):
        print(f'Запуск функции {func.__name__} в {time.time()}')
        # Запуск функции factorial в 1694111634.1757228
        result = func(*args, **kwargs)
        print(f'Результат функции {func.__name__} : {result = }')
        # Результат функции factorial : result = 2432902008176640000
        print(f'Завершение функции {func.__name__} в {time.time()}')
        # Завершение функции factorial в 1694111634.1757228
        return result

    return wrapper


def factorial(n: int) -> int:
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


print(f'{factorial(20)}')  # 2432902008176640000
control = main(factorial)
print(f'{control.__name__ = }')  # control.__name__ = 'wrapper'
print(f'{control(20) = }')  # control(20) = 2432902008176640000
