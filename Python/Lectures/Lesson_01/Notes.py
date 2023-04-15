print('Hello world')

# типы данных и переменная
# int, float, boolean, str, list, None

value = None  # WARNING no empty
a = 123
b = 1.23
print(a)
print(type(a))
print(b)
print(type(b))

s = 'hello world'
# for examples
s = 'hello "world"'  # or 'hello \nworld' or 'hello "world'
print(s)  # output string


# output
print(a, '-', b, '-', s)
print('{} - {} - {}'.format(a, b, s))
print('{1} - {2} - {0}'.format(a, b, s))
print(f'{a} - {b} - {s}')

f = True  # or False
print(f)

list = ['1', '2', '3', 'hello', 1, 2, 3, True]  # not correct
print(list)


# input
print('Enter a')
a = int(input())  # or a = float(input())
print('Enter b')
b = int(input())
print(a, '+', b, '=', a+b)


# Arifm operations
a = 123
b = -321
c = a + b
d = round(c / a, 5)  # 5 - количество цифр после запятой
e = e + 3  # or e += 3
# /для деления вещественных чисел (0,333333)
# // для деления целых чисел (0)
# ** возведение в степень
# % остаток от деления
print(c)


# logic operation
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# is, is not, in, not in
# gen

a = 1 < 4 and 5 > 2
b = 1 != a
print(a)

c = [1, 2]  # or 'qwe'
d = [1, 2]    # 'qwe'
print(a == b)

e = 1 < 3 < 5 < 7
print(e)

func = 1
T = 4
x = 3
print(func < T > x)  # сравнение больше меньше

f = 1 > 2 or 4 < 6
print(f)

g = [1, 2, 3, 4]
print(2 in g)  # True 2 in g

is_odd = g[1] % 2 == 0


# if, if - else

a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)

username = input('Input your name')
if username == 'Masha':
    print('Hi Masha!')
elif username == 'Artem':
    print('Hi Artem!')
else:
    print('Hi' + username)


# while, for

original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
    print(original)
else:
    print('Maybe')
    print('enough )')
print(inverted)


k = int(input('Enter positiv number: '))
while k <= 0:
	k = int(input('Enter positiv number: '))
else:
    print('Ok')
	# or example bottom
while k:=int(input('Enter positiv number: ')) <= 0: # моржевый оператор
	pass 


for i in "Hipjd !": # Hipjd
    print(i)
    if i == 'd':
        break
    else:
        continue
        
        
for i in range(-n, n+1):
    print(i, end=" ") # output in oneline
        
        
for i in 1,2,3,4,5:
    print(i**2)
    

r = range(10) # 10 not include
for i in r:
    print(i)
    
    
for num in range(5): # 01234
    print(num)


for i in range(2, 8):    # 2, 3, 4, 5, 6, 7
    print(i)

# for i in range(2, 8, 2):    # 2, 4, 6
#    print(i)


list = [1,2,3,4,5]
for i in list:
    print(i)

# convert range to list
num = [1, 2, 3, 4, 5]
print(num)
ran = range(1, 6)
print(type(ran))
num = list(ran)
print(type(num))

numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]
numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]
numbers[0] = 10
print(f'{len(numbers)} len')
print(numbers) # [10, 2, 3, 4, 5]
for i in numbers:
    i *= 2
print(i) # [20, 4, 6, 8, 10]
print(numbers) # [10, 2, 3, 4, 5] not change original


# strings

text = 'съешь еще этих мягких французских булок'
# help(text.istitle)    help about function
print(len(text))                    # 39
print('еще' in text)                # True
print(text.isdigit())               # False
print(text[0])                      # c
print(text[1])                      # ъ
print(text[len(text)-1])            # к
print(text[-5])                     # б
print(text[:])                      # print(text) default print(text[0:len(text)-1]) 
print(text[:2])                     # съ
print(text[len(text)-2:])           # ок
print(text[2:9])                    # ешь ещё
print(text[6:-18])                  # ещё этих мягких
print(text[0:len(text):6])          # сеикакл
print(text[::6])                    # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...



# spiski

colors = ['red', 'green', 'blue']
for e in colors:
    print(e) # red green blue
for e in colors:
    print(e*2) # redred greengreen blueblue
colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') #del colors[0] # удалить элемент


# function

def f(x):
    return x**2
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 1 # 2.3, 
print(f(arg))
print(type(f(arg)))
