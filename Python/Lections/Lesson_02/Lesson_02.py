# a - открытие для добавления данных
# r - открытие для чтения
# w - открытие для записи
# w+, r+ 




with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')




# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей не будет
# data.close()




exit() # команда позволяет не выполнять код последующий после нее
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()




import hello as h # импортирование функций из соседнего файла где hello - имя файла  as h - замена имени файла
print(hello.f(1)) # функция f со значением 1

def new_sstring(symbol, count):
    return symbol * count

print(new_sstring('!', 5)) # !!!!!
print(new_sstring('!')) # TypeError missing 1 required

# or

def new_sstring(symbol, count = 3):
    return symbol * count

print(new_sstring('!', 5)) # !!!!!
print(new_sstring('!')) # !!!
print(new_sstring(4)) # 12





def concatenatio(*params):
    res:str = ""
    for item in params:
        res += item
    return res

print(concatenatio('a', 's', 'd', 'w')) # asdw
print(concatenatio('a', '1')) # a1
print(concatenatio(1, 2, 3, 4)) # TypeError: ...



def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

list = []
for e in range(1, 10):
    list.append(fib(e))
print(list) # 1 1 2 3 5 8 13 21 34




a = (3, 4) # a = (3,) - кортеж с одним элементом
print(a)
print(a[0]) # [0] - index,  [-1]-last index
a[0] = 12 # not work

t = ()
print(type(t)) # tuple
t = (1,)
print(type(t)) # tuple
t = (1)
print(type(t)) # int
t = (28, 9, 1990)
print(type(t)) # tuple
colors = ['red', 'green', 'blue']
print(colors) # ['red', 'green', 'blue']
t = tuple(colors)
print(t) # ('red', 'green', 'blue')
t = tuple(['red', 'green', 'blue'])
print(t[0]) # red
print(t[2]) # blue
# print(t[10]) # IndexError: tuple index out of range
print(t[-2]) # green
# print(t[-200]) # IndexError: tuple index out of range
for e in t:
 print(e) # red green blue
t[0] = 'black' #  TypeError: 'tuple' object does not support item assignment
t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue)) # r:red g:green b:blue



# Неупорядоченные коллекции произвольных объектов с доступом по ключу
dictionary = {}
dictionary = \
 {
 'up': '↑',
 'left': '←',
 'down': '↓',
 'right': '→'
 }
 # \ для переноса списка
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←
# типы ключей могут отличаться
print(dictionary['up']) # ↑
# типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
#print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
for item in dictionary: # for (k,v) in dictionary.items():
 print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →
for k in dictionary.keys():# print keys
    print(k)
for k in dictionary.values():# print values
    print(k)
for v in dictionary:# print values
    print(k)



# Множества
colors = {'red', 'green', 'blue'}
print(type(colors)) # <class 'set'>

colors.add('gray') # add gray 
print(colors) # {'red', 'green', 'blue', 'gray'}

colors.remove('red') # remove red 
print(colors) # {'green', 'blue', 'gray'}
colors.remove('red') # KeyError: 'red'
colors.discard('red') # ok

colors.clear() # { }
print(colors) # set ()

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}  объединение множеств
i = a.intersection(b) # i = {8, 2, 5}
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}
q = a \
 .union(b) \
 .difference(a.intersection(b))
# {1, 21, 3, 13}

# неизменяемое множество
a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b) # frozenset({1, 2, 3, 5, 8})





# списки - доп инфа
list1 = [1, 2, 3, 4, 5]
list2 = list1

for e in list1:
    print(e)

print()

for e in list2:
    print(e)

list1[0] = 123 # chenge both lists
list2[1] = 333 # change both lists

print(list1.pop()) # delete last value
print(list1.pop(2)) # delete value with index 2

print(list1.insert(2, 11)) # insert value where 2-index and 11-value

print(list1.append(11)) # add value 11 in last place list