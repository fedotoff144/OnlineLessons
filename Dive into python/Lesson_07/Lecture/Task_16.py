import os
from pathlib import Path

# ПЕРЕНОС ФАЙЛОВ
# replace and rename file
# os.replace('newest_file_ex.txt', os.path.join(os.getcwd(), 'dir', 'newest_file_ex_copy.txt'))


# replace file
old_file = Path('new_file_1.txt')
new_file = old_file.replace(Path.cwd()/'new_os_dir'/old_file)