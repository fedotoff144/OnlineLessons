# Менеджер контекста with open
#
# with open('text_data.txt', 'r+', encoding='utf-8') as f:
# print(list(f))
# ✔ with гарантирует закрытие файла и сохранение информации


with open('text_file.txt', 'r+', encoding='utf-8') as f:
    print(list(f))
print(f.write('Пока!')) # ValueError: I/O operation on closed file.

