import os
from pathlib import Path


# Path написано с большой буквы это говорит о том что это класс
# cwd - current work dir

# просмотр пути рабочей директории
print(os.getcwd()) # D:\GeekBrains\OnlineLessons\Dive into python\Lesson_07\Lecture
print(Path.cwd()) # D:\GeekBrains\OnlineLessons\Dive into python\Lesson_07\Lecture

os.chdir('../..') # выходим из рабочей директории на уровень выше аналогично 'cd ..'
print(os.getcwd()) # D:\GeekBrains\OnlineLessons\Dive into python
print(Path.cwd()) # D:\GeekBrains\OnlineLessons\Dive into python


# Создание директории
os.mkdir('new_os_dir') # создаем папку в текущей директории спомощью библиотеки os
Path('new_path_dir').mkdir() # создаем папку в текущей директории спомощью библиотеки Path


# Создание директории по определенному пути
os.makedirs('dir1/new_internal_os_dir/new_target_os_dir') # если папка уже существует то ловим ошибку
# Path('dir2/new_internal_path_dir/new_target_path_dir').mkdir() # FileNotFoundError
Path('dir2/new_internal_path_dir/new_target_path_dir').mkdir(parents=True) # если папка уже существует то ловим ошибку


# Удаление директории
os.rmdir('dir1') # OSError: [WinError 145] Папка не пуста: 'dir1'
Path('dir2').rmdir() # OSError: [WinError 145] Папка не пуста: 'dir1'
os.rmdir('dir1/new_internal_os_dir/new_target_os_dir') # удалились только целевые папки new_target_dir
Path('dir2/new_internal_path_dir/new_target_path_dir').rmdir() # удалились только целевые папки new_target_dir


