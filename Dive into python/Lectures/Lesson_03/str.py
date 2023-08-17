# Квадратные скобки [ ]
# ✔ доступ к элементу по индексу
# ✔ срезы строк
# ✔ реверс строк
# - Метод count()
# Подсчёт вхождения элемента
# - Метод index()
# Индекс первого вхождения элемента
# - Метод find()
# Индекс первого вхождения элемента

text = 'Hello world!'
print(text[4])  # o
print(text[3:7])  # lo w

new_text = text.replace('l', 'L', 2)  # HeLLo world!
print(new_text)

print(text.count('l'))  # 3
print(text.index('l'))  # 2
print(text.find('l'))  # 2
print(text.find('x'))  # -1 (False)

print(text[::-1])  # !dlrow olleH (reverse)


# format strings
# Format Specification Mini-Language
# https://docs.python.org/3/library/string.html#format-specification-mini-language

name = 'Alex'
age = 20
text = '%s Хочешшь еще съесть этих мягких %d французских булочек?' % (name, age)
print(text)  # Alex Хочешшь еще съесть этих мягких 20 французских булочек?

text_1 = '{} Хочешшь еще съесть этих мягких {} французских булочек?'.format(name, age)
print(text_1)  # Alex Хочешшь еще съесть этих мягких 20 французских булочек?

text_2 = f'{name} Хочешшь еще съесть этих мягких {age} французских булочек?'
print(text_2)  # Alex Хочешшь еще съесть этих мягких 20 французских булочек?

print(f'{{Фигурные скобки}} и {{name}}')  # {Фигурные скобки} и {name}

pi = 3.1415
print(f'Число Пи с точностью два знака кпосле запятой: {pi:.2f}')
# Число Пи с точностью два знака кпосле запятой: 3.14

data = [321, 56444, 7878542, 23480]
for item in data:
    print(f'{item:>10}') # сдвиг всего вывода к месту 10 символа справа смотр ниже
#        321
#      56444
#    7878542
#      23480

num = 2 * pi * data[1]
print(f'{num = :_}') # num = 354_637.652

# - Метод split()
# Разбивает строку на отдельные элементы
# - Метод join()
# Формирует строку из отдельных элементов
# - Методы upper(), lower(), title(), capitalize()
# Изменение регистра
# - Методы startswith() и endswith()
# Проверка на совпадение с началом или концом строки

a, b, c = input('Введите 3 числа через пробел: ').split()
print(a,b,c)

d, e, f, *_ = input('Введите 3 числа через пробел: ').split()
# если введут больше чем 3 числа через пробел все остальное запишется в переменную _

data = ['http', 'www', 'geekbrains', 'ru']
url = '/'.join(data) # http/www/geekbrains/ru
print(url)

text_3 = 'HeLLo WoRlD!'
print(text_3.upper()) # HELLO WORLD!
print(text_3.lower()) # hello world!
print(text_3.title()) # Hello World!
print(text_3.capitalize()) # Hello world!


text_4 = 'Однажды в студеную зимнюю пору!'
print(text_4.startswith('Однажды')) # True
print(text_4.endswith('зимнюю', 0, -5)) # True (word, start, stop)

