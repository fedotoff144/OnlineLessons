# Задача №5
# Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
# Используйте комплексные числа для извлечения квадратного корня.

import decimal

decimal.getcontext().prec = 4

a = 1
b = 6
c = -34
d = b ** 2 - 4 * a * c

if d != 0:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    result = 'уравнение имеет два корня х1=' + str(x1) + 'x2=' + str(x2)
else:
    x = (-b) / (2 * a)
    result = 'уравнение имеет один короень х=' + x

print(result)
