# Работа сразу с несколькими файлами

# Старая запись
# with (open('text_file.txt', 'r+', encoding='utf-8') as f1, \
#       open('bin_data', 'rb') as f2, \
#       open('data.txt', 'r', encoding='utf-8', errors='backslashreplace') as f3):
#     print(list(f1))
#     print(list(f2))
#     print(list(f3))

with (
    open('text_file.txt', 'r+', encoding='utf-8') as f1,
    open('bin_data', 'rb') as f2,
    open('data.txt', 'r', encoding='utf-8', errors='backslashreplace') as f3
):
    print(list(f1))
    print(list(f2))
    print(list(f3))