# Генераторы

a = range(0,10, 2)
print(f'{a=}, {type(a)}, {a.__sizeof__()}, {len(a)}')
# a=range(0, 10, 2), <class 'range'>, 48, 5

b = range(-1_000_000, 1_000_000, 2)
print(f'{b=}, {type(b)}, {b.__sizeof__()}, {len(b)}')
# b=range(-1000000, 1000000, 2), <class 'range'>, 48, 1000000
