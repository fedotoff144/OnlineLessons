from typing import Callable
import random


def cache(func: Callable):
    _cache_dict = {}

    def wrapper(*args):
        if args not in _cache_dict:
            _cache_dict[args] = func(*args)
        return _cache_dict[args]

    return wrapper


@cache
def rnd(a: int, b: int) -> int:
    return random.randint(a, b)


print(f'{rnd(1, 10) = }') # rnd(1, 10) = 7
print(f'{rnd(1, 10) = }') # rnd(1, 10) = 7
print(f'{rnd(1, 10) = }') # rnd(1, 10) = 7