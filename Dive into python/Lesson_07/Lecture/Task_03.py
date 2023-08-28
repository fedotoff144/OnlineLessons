# Прочие необязательные параметры функции open
# Погружение в Python | Файлы и файловая система
# ✔ buffering — определяет режим буферизации
# ✔ errors — используется только в текстовом режиме и определяет поведение в случае ошибок
# кодирования или декодирования
# ✔ newline — отвечает за преобразование окончания строки
# ✔ closefd — указывает оставлять ли файловый дескриптор открытым при закрытии файла
# ✔ opener — позволяет передать пользовательскую функцию для открытия файла

f = open('bin_data', 'wb', buffering=64) # запись бинарных файлов
f.write(b'X' * 1200)
f.close()

l = open('data.txt', 'wb')
l.write('Привет, '.encode('utf-8') + 'мир!'.encode('cp1251'))
l.close()

# l = open('data.txt', 'r', encoding='utf-8')
# print(list(l)) # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xec in position 14: invalid continuation byte
# l.close()

l = open('data.txt', 'r', encoding='utf-8', errors='replace')
print(list(l)) # ['Привет, ���!']
l.close()
