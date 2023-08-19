# abs(x) — возвращает абсолютное значение числа x,
# число по модулю.
x = -42
print(abs(x))


# divmod(a, b) — функция принимает два числа
# в качестве аргументов и возвращает пару чисел —
# частное и остаток от целочисленного деления.
# Аналогично вычислению a // b и a % b.
a = 42
b = 5
print(divmod(a, b))


# pow(base, exp[, mod]) — при передаче 2-х аргументов
# возводит base в степень exp. При передаче 3-х
# аргументов, результат возведения в степень делится
# по модулю на значение mod.
print(pow(a, b))
print(pow(a, b, 10))

# round(number[, ndigits]) — округляет число
# number до ndigits цифр после запятой. Если второй
# аргумент не передать, округляет до ближайшего целого
print(round(3.141_592, 3))