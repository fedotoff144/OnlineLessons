a: int = 42 # аннотация, мы указываем что в переменной будет храниться int
# a: int | float = 42 # аннотация, мы указываем что в переменной будет храниться либо int либо float
b: float = float(input('Enter num: ')) # аннотация, мы указываем что в переменной будет храниться float
a = a / b


def my_func(data: list[int, float]) -> float:
    # data: list[int, float] - ожидаем что будет передан список состоящий из int или float
    # -> float: ожидаем что результатом будет число типа float
    res = sum(data) / len(list)
    return res

print(my_func([2, 5, 8, 1, 4]))