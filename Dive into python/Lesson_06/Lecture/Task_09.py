# Модуль random
#
# Модуль используется для генерации псевдослучайных чисел.
# ✔ random() — генерирует псевдослучайные числа в диапазоне [0, 1)
# ✔ seed(a=None, version=2) — инициализирует генератор. Если значение
# a не указано, для инициализации используется текущее время ПК
# ✔ getstate() — возвращает объект с текущим состоянием генератора
# ✔ setstate(state) — устанавливает новое состоянии генератора,
# принимая на вход объект, возвращаемый функцией getstate
# ===============================================================================


import random as rnd

START = -100
STOP = 1_000
STEP = 10
data = [2, 4, 6, 8, 42, 73]

# randint(a, b)
# целое число от a до b
print(f'{rnd.randint(START, STOP) = }')  # rnd.randint(START, STOP) = 121

# ✔ uniform(a, b)
# вещественное число от a до b
print(f'{rnd.uniform(START, STOP) = }')  # rnd.uniform(START, STOP) = 148.04442585474936

# ✔ choice(seq)
# случайный элемент последовательности
print(f'{rnd.choice(data) = }')  # rnd.choice(data) = 6

# ✔ randrange(start, stop[, step])
# число из диапазона
print(f'{rnd.randrange(START, STOP, STEP) = }')  # rnd.randrange(START, STOP, STEP) = 680

# ✔ shuffle(x)
# перемешиваем коллекцию x in place
rnd.shuffle(data)
print(f'{data}')  # [4, 42, 2, 73, 6, 8]

# ✔ sample(population, k, *, counts=None)
# Выборка в k элементов из population
print(f'{rnd.sample(data, 3) = }')  # rnd.sample(data, 3) = [73, 8, 2]
print(f'{rnd.sample(data, 3, counts=[1,1,1,1,1,100]) = }')  # rnd.sample(data, 3, counts=[1,1,1,1,1,100]) = [8, 8, 8]
