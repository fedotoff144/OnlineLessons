# Task 3
# Напишите программу, которая будет на вход принимать число
# и выводить числа от N до -N
# -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5


# n = int(input("введите число ")) 
# numbers = [] 
# for i in range(-n, n+1): 
# numbers.append(i) 
# print(numbers) 

n = int(input('Enter number: '))

for i in range(-n, n+1):
    print(i) # print(i, end=" ") - output in oneline

    # print(value, ..., sep='', end='\n  - разделение коллекции
