def f(x):
    x**2


print(type(f))  # <class 'function'>


def f(x):
    return x**2


g = f  # g keep function
print(f(2))  # 16
print(g(2))  # 16


def calc1(x):
    return x+10


print(calc1(10))  # 20


def calc2(x):
    return x*10


print(calc2(10))  # 100


def math(op, x):
    print(op(x))


math(calc2, 10)  # 100
math(calc1, 10)  # 20


def sum(x, y):
    return x+y


def sum(x, y): return x+y


def mylt(x, y):
    return x*y


def calc(op, a, b):
    print(op(a, b))
    # return op(a, b)


calc(mylt, 4, 5)  # 20
calc(sum, 4, 5)
calc(lambda x, y: x+y, 4, 5)


# List Comprehension
[exp for item in iterable]
[exp for item in iterable (if conditional)]
[exp <if conditional> for item in iterable (if conditional)]

list = []

for i in range(1, 21):
    if (i % 2 == 0):
        list.append(i)
print(list)
# or short write
            list = [i for i in range(1, 21) if i % 2 == 0]
            print(list)

list = [(i, i) for i in range(1, 21) if i % 2 == 0]  # cortezh
print(list)


def f(x):
    return x**3


list = [f(i) for i in range(1, 21) if i % 2 == 0]
# list = [(i, f(i)) for i in range(1, 21) if i%2 == 0]  cortezh
print(list)

# В файле хранятся числа, нужно выбрать четные и составить список пар(число; квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]
# путь к файлу из которого считываем информацию
path = '/Users/Artem/GeekBrains/Education/Python/Lesson_03/file.txt'
f = open(path, 'r')  # задаем переменную открытому файлу
data = f.read() + ' '  # ситываем информацию из файла и добавляем искуственно пробел
f.close()  # закрываем  файл

numbers = []  # пкстой список который будем наполнять в дальнейшем

while data != '':  # пробегаем по строке пока строка не пустая
    space_pos = data.index(' ')  # ищем первую позицию пробела
    # взяьт все что находится от позиции первого символа до нашего пробела конверт в число и добавить в список
    numbers.append(int(data[:space_pos]))
    # обновить строку с указанием не испольования предыдущей
    data = data[space_pos+1:]

out = []  # создаем новый список
for e in numbers:  # пробегаем по исходному списку
    if not e % 2:  # проверяем словие
        out.append((e, e**2))  # добавляем кортеж
print(out)
# or
            def select(f, col):
                return [f(x) for x in col]

            def where(f, col):
                return [x for x in col if f(x)]

            data = '1 2 3 5 8 23 38'.split()

            res = select(int, data)  # [1, 2, 3, 5, 8, 23, 38]
            res = where(lambda x: not x % 2, res)  # [2, 8, 38] just chet
            res = select(lambda x: (x, x**2), res)
            print(res)
# or
data = '1 2 3 5 8 23 38'.split()
res = map(int, data)  # [1, 2, 3, 5, 8, 23, 38]
res = filter(lambda x: not x % 2, res)  # [2, 8, 38] just chet
res = list(map(lambda x: (x, x**2), res))
print(res)


# Функция map
# Функция map() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с новыми объектами.
f(x) ⇒ x + 10
map(f, [1,  2,  3,  4,  5])
        ↓    ↓   ↓   ↓   ↓
       [ 11, 12, 13, 14, 15]

li = [x for x in range(1, 20)]
li = list(map(lambda x:x+10, li))
print(li)

data = list(map(int, input().split()))
print(data)

data = map(int, '1 2 3 4 555 6'.split())
for e in data:
    print(e)



# Функция filter
# Функция filter() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для
# которых функция вернула True.
f(x) ⇒ x - чётное
filter(f, [ 1, 2, 3, 4,5])
                    ↓
          [    2,    4 ]

data = [x for x in range(10)]

res = list(filter(lambda x: not x%2, data))
print(res) #just chet numbers



# Функция zip
# Функция zip() применяется к набору итерируемых
# объектов и возвращает итератор с кортежами из
# элементов входных данных.
# Количество элементов в результате равно минимальному количеству элементов входного набора
zip ([1, 2, 3], [ ‘о‘, ‘д‘, ‘т‘], [‘f’,’s’,’t’])
                        ↓
[(1, 'о', 'f'), (2, 'д', 's'), (3, 'т', 't')]

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
#salsary = [200, 300, 400]

data = list(zip(user, ids)) # data = list(zip(user, ids, salary))
print(data) # если передать аргумент salary то выведет первые 3 элемента всех списков из-за длины salary




# Функция enumerate
# Функция enumerate() применяется к итерируемому
# объекту и возвращает новый итератор с кортежами
# из индекса и элементов входных данных.
enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])
                            ↓
[(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]
# Нельзя пройтись дважды

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
#salsary = [200, 300, 400]

data = list(enumerate(users))
print(data) # (0, user1) (1, user2) (2, user3)...



