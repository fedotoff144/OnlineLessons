"""
Методы перемещения в файле

f.tell() - Метод tell возвращает текущую
позицию в файле

truncate(size=None) - Метод изменяет размер файла.
Если не передать значение
в параметр size будет удалена
часть файла от текущей позиции
до конца

seek(offset, whence=0) - offset — смещение относительно
опорной точки, whence — способ выбора
опороной точки.

✔ whence=0 — отсчёт
от начала файла
✔ whence=1 — отсчёт от
текущей позиции в файле
✔ whence=2 — отсчёт
от конца файл

"""

# f.tell() - Метод tell возвращает текущую позицию в файле
text = ['1. Some long and not interesting text', '2. Some long and not interesting text',
        '3. Some long and not interesting text']

with(open('new_file_1.txt', 'w', encoding='utf-8')) as f:
    print(f.tell())
    for line in text:
        f.write(f'{line}\n')
        print(f.tell())
    print(f.tell())
# print(f.tell()) # ValueError: I/O operation on closed file.


last = before = 0
with(open('new_file_1.txt', 'r+', encoding='utf-8')) as f:
    while line := f.readline():
        last, before = f.tell(), last
        print(f'{last = }, {before = }')
    print(f'{last}, {before = }')
    print(f'{f.seek(before, 0)}')
    f.write('\n'.join(text))


# truncate(size=None) - Метод изменяет размер файла.
# Если не передать значение
# в параметр size будет удалена
# часть файла от текущей позиции
# до конца
last = before = 0
with(open('new_file_1.txt', 'r+', encoding='utf-8')) as f:
    while line:= f.readline():
        last, before = f.tell(), last
    print(f.seek(before, 0))
    print(f.truncate()) # обрезаем файл


size = 125
with(open('new_file_1.txt', 'r+', encoding='utf-8')) as f:
    print(f.truncate(size)) # обрезает все полсле 125 символов
