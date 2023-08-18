# Задача №4
# Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру. Диаметр не превышает 1000 у.е. Точность вычислений должна составлять не менее 42 знаков после запятой.

from math import pi
import decimal

decimal.getcontext().prec = 42 # 42 знака после запятой в числе
diam_circle = decimal.Decimal(10)
pi_ = decimal.Decimal(pi)

squere = (pi_ * diam_circle ** 2) / 4
length = pi_ * diam_circle

print(squere, length)
