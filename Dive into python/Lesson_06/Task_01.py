import sys  # встроенный модуль <module 'sys' (built-in)>

print(sys)  # <module 'sys' (built-in)>
print(sys.builtin_module_names)  # ('_abc', '_ast', '_bisect',.....'xxsubtype', 'zlib')

# Содержимое переменной sys.path формируется динамически.
# PYTHONPATH - переменная с путями до мест расположения модулей

print(*sys.path, sep='\n')  # команда начинает искать модуль по следующим расположениям:
# D:\GeekBrains\OnlineLessons\Dive into python\Lesson_06
# D:\GeekBrains\OnlineLessons\Dive into python\Lesson_06
# C:\Program Files\JetBrains\PyCharm 2023.1.1\plugins\python\helpers\pycharm_display
# C:\Users\fedotoff144\AppData\Local\Programs\Python\Python310\python310.zip
# C:\Users\fedotoff144\AppData\Local\Programs\Python\Python310\DLLs
# C:\Users\fedotoff144\AppData\Local\Programs\Python\Python310\lib
# C:\Users\fedotoff144\AppData\Local\Programs\Python\Python310
# C:\Users\fedotoff144\AppData\Local\Programs\Python\Python310\lib\site-packages
# C:\Program Files\JetBrains\PyCharm 2023.1.1\plugins\python\helpers\pycharm_matplotlib_backend
