# Task 1
# Напишите программу, которая принимает на вход число n и выдаёт последовательность из n членов.
# Пример:
# Для n = 5: 1, -3, 9, -27, 81


# i = int(input('Введите число N: '))
# y = 1
# while i:
#   print(y)
#   y *= -3
#   i -= 1
#   break   or continue
# else:
#   print(000)

n = int(input('Enter n: '))
first = 1

for i in range(n):
    print(first, end=', ')  # end=', ' change output in oneline
    first *= -3