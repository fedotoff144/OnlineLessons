"""
Замыкание (англ. closure) в программировании — функция первого класса,
в теле которой присутствуют ссылки на переменные, объявленные вне тела
этой функции в окружающем коде и не являющиеся её параметрами.
"""
from typing import Callable


def add_one_str(a: str) -> Callable[[str], str]:
    def add_two_str(b: str) -> str:
        return a + ' ' + b

    return add_two_str


print(add_one_str('Hello')('world!'))
