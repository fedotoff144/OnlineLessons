import os
from pathlib import Path


# ПЕРЕИМЕНОВАНИЕ ФАЙЛОВ
# файл обязательно должен существовать иначе ловим ошибку
os.rename('old_name.txt', 'old_name.txt')

p = Path('old_name.txt')
p.rename('new_name.txt')

Path('new_file_ex.txt').rename('newest_file_ex.txt')