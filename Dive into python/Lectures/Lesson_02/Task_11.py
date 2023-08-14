import decimal


# num = decimal.Decimal(object)
# Получаем вещественное число
# с точностью 28 знаков (до и после запятой).
pi = decimal.Decimal('3.141_592_653_141_592_653_141_592_653_8')
print(pi)

# decimal.getcontext().prec = dec
# Задаём точность в dec знаков
# для будущих операций.
decimal.getcontext().prec = 120 # число со 120 знаками
num = 2 * pi * decimal.Decimal(23.7896) ** 2
print(num)