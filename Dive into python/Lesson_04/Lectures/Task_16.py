"""
💡 map(function, iterable)
Принимает на вход функцию и последовательность.
Функция применяется к каждому элементу
последовательности и возвращает map итератор.
💡 filter(function, iterable)
Принимает на вход функцию и последовательность.
Если функция возвращает истину, элемент остаётся
в последовательности. Как и map возвращает объект итератор.
💡 zip(*iterables, strict=False)
Принимает несколько последовательностей и итерируется
по ним параллельно. Если передать ключевой аргумент
strict=True, вызовет ошибку ValueError в случае разного
числа элементов в каждой из последовательностей.
"""

"""map(function, iterable)"""
texts = ['Hello', 'HELLO', 'heLLo']
res = map(lambda x: x.lower(), texts)
print(res)
print(*res) # * - распаковка объектов

"""filter(function, iterable)"""
numbers = [42, -73, 1024]
res = tuple(filter(lambda x: x > 0, numbers))
print(res)
print(*res) # * - распаковка объектов

"""zip(*iterables, strict=False)"""
names = ['Jhon', 'Sam', 'Eddy']
salaries = [125_000, 250_000, 96_000]
awards = [0.1, 0.25, 0.13, 0.99] # 0.99 не идет в учет так как для нее нет пары
for name, salary, award in zip(names, salaries, awards):
    print(f'{name} заработал: {salary:.2f} денег и премию {salary * award:.2f}: ИТОГО:', salary + salary * award)