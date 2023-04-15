# a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input()) print(max(a, b, c, d, e))

# num = 0
# maximum = 0
# for _ in range(5):
# num = int(input("Введите число: "))
# if num > maximum:
# maximum = num print(maximum)

# from random import randint 
# numbers = [] for i in range(5): 
# numbers.append(randint(-10, 10)) 
# max_count = max(numbers) 
# print(numbers) 
# print(max_count) 

# numbers = [] 
# for _ in range(1, 5): 
# numbers.append(int(input('--> '))) 
# max_count = max(numbers) 
# print(numbers) 
# print(max_count) 

a = int(input('Enter number a:'))
b = int(input('Enter number b:'))
c = int(input('Enter number c:'))
d = int(input('Enter number d:'))
e = int(input('Enter number e:'))
max = 0

if a > max:
    max = a
elif b > max:
    max = b
elif c > max:
    max = c
elif d > max:
    max = d
elif e > max:
    max = e
else:
    print(max)