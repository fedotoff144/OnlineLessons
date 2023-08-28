"""
== Запись и добавление в файл ==

💡 res = f.write(text)
Запись методом write
💡 f.writelines('\n'.join(text))
Запись методом writelines
💡 print(text, file=f)
print в файл

💡 w
создаём новый пустой файл для записи.
Если файл существует, открываем его для
записи и удаляем данные, которые в нём
хранились
💡 x
создаём новый пустой файл для записи.
Если файл существует, вызываем ошибку
💡 a
открываем существующий файл для записи
в конец, добавления данных. Если файл
не существует, создаём новый файл
и записываем в него

"""
text = 'Some long and not interesting text'
with (open('new_file.txt', 'a', encoding='utf-8')) as f:
    res = f.write(text)
    print(f'{res = }\n{len(text) = }')

text = ['1. Some long and not interesting text', '2. Some long and not interesting text',
        '3. Some long and not interesting text']
with (open('new_file.txt', 'a', encoding='utf-8')) as f:
    for line in text:
        f.write(f'{line}\n')
        print(f'{res = }\n{len(text) = }')


with(open('new_file.txt', 'a', encoding='utf-8')) as f:
    f.writelines('\n'.join(text))


with(open('new_file.txt', 'a', encoding='utf-8')) as f:
    for line in text:
        print(line, file=f)


with(open('new_file.txt', 'a', encoding='utf-8')) as f:
    for line in text:
        print(line, end='***\n##', file=f)

