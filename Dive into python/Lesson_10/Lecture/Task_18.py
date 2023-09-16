"""
Полиморфизм
свойство системы, позволяющее использовать
объекты с одинаковым интерфейсом без информации о типе и
внутренней структуре объекта.
"""

path_1 = '/home/user'
path_2 = '/my_project/workdir'
result = path_1 / path_2 # TypeError: unsupported operand type(s) for /: 'str' and 'str'
