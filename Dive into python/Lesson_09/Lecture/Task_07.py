"""
Множественное декорирование

- функция может быть декорирована одновременно несколькими декораторами
- декорирование происходит снизу вверх по коду и один раз
- работа декораторов просиходит сверху вниз по коду
"""
from typing import Callable


def deco_a(func: Callable):
    def wrapper_a(*args, **kwargs):
        print('Start deco A')
        print(f'Start {func.__name__ = }')
        result = func(*args, **kwargs)
        print('Finish deco A')
        return result

    print('Return deco A')
    return wrapper_a


def deco_b(func: Callable):
    def wrapper_b(*args, **kwargs):
        print('Start deco B')
        print(f'Start {func.__name__ = }')
        result = func(*args, **kwargs)
        print('Finish deco B')
        return result

    print('Return deco B')
    return wrapper_b


def deco_c(func: Callable):
    def wrapper_c(*args, **kwargs):
        print('Start deco C')
        print(f'Start {func.__name__ = }')
        result = func(*args, **kwargs)
        print('Finish deco C')
        return result

    print('Return deco C')
    return wrapper_c


@deco_c
@deco_b
@deco_a
def main():
    print('Start main function')


if __name__ == '__main__':
    print('>>> Start main()')
    main()
    print('>>> End main()')
