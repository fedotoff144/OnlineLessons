# картежи это неизменяеые списки

# Способы создания
# кортежа
a = ()
b1 = 1,
b2 = (1,)
c1 = 1, 2, 3,
c2 = (1, 2, 3)
d = tuple(range(3))
print(a, b1, b2, c1,
c2, d, sep='\n')


# Работа с кортежем
# - Обращение к элементу по индексу
# - Срезы
# - Методы count(), index()
# - Функция len()


# Особенность кортежей
# - f(a, b, c) — это вызов функции с тремя аргументами
# - f((a, b, c)) — вызов функции с кортежем в качестве единственного аргумента