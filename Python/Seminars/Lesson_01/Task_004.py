# Task 4
# Напишите программу, которая будет принимать на вход дробь и показывать
# первую цифру дробной части числа
# Например:
# 6,87 -> 7
# 5 -> no
# 3,45 -> 4

# string = input('Введите дробное число: ').split(',')[1][0] 
# print(string)

num = float(input('Enter number: '))
secDigital = (num*10) % 10
print(int(secDigital))
