import os
from pathlib import Path

# Формиррование пути файла до каталога
file_1 = os.path.join(os.getcwd(), 'new_dir1', 'new_file_1.txt')
print(f'{file_1 = }\n{file_1}')

file_2 = Path.cwd()/'new_dir2'/'new_file_2.txt'
print(f'{file_2 = }\n{file_2}')