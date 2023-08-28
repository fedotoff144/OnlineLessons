import os
from pathlib import Path


# Перечисление всех каталогов и файлов в рабочей директории
print(os.listdir())

p = Path(Path().cwd())
for obj in p.iterdir():
    print(obj)