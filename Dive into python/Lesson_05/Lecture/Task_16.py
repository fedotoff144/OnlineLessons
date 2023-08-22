def factorial(n):
    number = 1
    result = []
    for i in range(1, n+1):
        number *= i
        result.append(number)
    return result


for i, num in enumerate(factorial(10), start=1):
    print(f'{i}! = {num}')
# 1! = 1
# 2! = 2
# 3! = 6
# 4! = 24
# 5! = 120
# 6! = 720
# 7! = 5040
# 8! = 40320
# 9! = 362880
# 10! = 3628800


"""
Команда yield

Команда yield работает аналогично return.
Но вместо завершения функции запоминает её состояние.
Повторный вызов продолжает код после yield.
def gen(*args, **kwargs):
    ...
    yield result
"""


def factorial_yield(n):
    number = 1
    for i in range(1, n+1):
        number *= i
        yield number


for i, num in enumerate(factorial_yield(10), start=1):
    print(f'{i}! = {num}')