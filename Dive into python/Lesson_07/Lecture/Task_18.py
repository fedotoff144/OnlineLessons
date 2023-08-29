import shutil
import os
from pathlib import Path


# УДАЛЕНИЕ ФАЙЛОВ И ДИРЕКТОРИЙ
shutil.rmtree('dir')

os.remove('new_os_dir/new_dir/newest_file_ex_copy.txt')

Path('new_os_dir/new_dir/shutill_file_1_copy.txt').unlink()