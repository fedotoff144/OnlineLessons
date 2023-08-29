import shutil

# КОПИРОВАНИЕ ФАЙЛОВ
# НЕ КОПИРУЕТ метаданные
shutil.copy('shutill_file.txt', 'dir')

# КОПИРУЕТ метаданные
shutil.copy2('shutill_file_1.txt', 'dir/shutill_file_1_copy.txt')

# копирование папки (с созданием) вместе со всем ее содержимым
shutil.copytree('dir', 'new_os_dir/new_dir')