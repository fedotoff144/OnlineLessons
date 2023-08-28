"""
== Чтение файла ==

💡 list(f)
Чтение в список
💡 res = f.read()
Чтение методом read
💡 res = f.readline()
Чтение методом readline
💡 for line in f:
Чтение циклом for

"""

with(open('text_file.txt', 'r', encoding='utf-8')) as f:
    print(list(f))

print('1 ==============================')
with(open('text_file.txt', 'r', encoding='utf-8')) as f:
    res = f.read()
    print(f'Читаем первый раз\n{res}')
    res = f.read()
    print(f'Читаем второй раз\n{res}') # второй раз не читается

print('2 ==============================')
SIZE = 100
with (open('text_file.txt', 'r', encoding='utf-8')) as f:
    while res:= f.read(SIZE):
        print(res)

print('3 ==============================')
with (open('text_file.txt', 'r', encoding='utf-8')) as f:
    while res:= f.readline():
        print(res, end='')


print('4 ==============================')
with (open('text_file.txt', 'r', encoding='utf-8')) as f:
    while res:= f.readline(SIZE):
        print(res, end='')


print('5 ==============================')
with (open('text_file.txt', 'r', encoding='utf-8')) as f:
    for line in f:
        print(line, end='')


print('6 ==============================')
with (open('text_file.txt', 'r', encoding='utf-8')) as f:
    for line in f:
        print(line[:-1]) # срезы
        print(line.replace('\n', ''))


