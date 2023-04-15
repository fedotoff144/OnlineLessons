# Task 02

# Найдите корни квадратного уровня Ах^2 + Вх + С = 0 двумя способами:
#     1 с помощью математических формул нахождения корнейквадратного корня
#     2 с помощью дополнительных библиотек Python (scipy)

a = 9
b = -11
c = 3

discr = b * b - 4 * (a * c)

if discr == 0:
    my_typle = (-b / (2*a), )
elif discr > 0:
    my_typle = ((-b + discr ** 0.5) / (2*a), (-b - discr ** 0.5) / (2*a))
else:
    my_typle = ("Empty", )

print(my_typle)
