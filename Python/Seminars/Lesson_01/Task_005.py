# Task 5
# Напишите программу, которая принимает на вход число и проверяет,
# кратно ли оно 5 и 10 или 15, но не 30

# n = int(input("введите число "))
# print((n % 5 == 0) and (n % 10 == 0)) or ((n % 15 == 0) and not (n % 30 == 0))

# a is not None # Так круто 
# a != None # Не круто 

n = int(input('Enter number: '))
if ((n % 5 == 0) and (n % 10 == 0)) or (n % 15 == 0):
    if (n % 30 != 0):
        print('no')
    print('yes')
else:
    print('no')
