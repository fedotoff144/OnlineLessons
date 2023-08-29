"""
Улучшаем задачу 2.
Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
Для преобразования строковых аргументов командной строки в числовые параметры
используйте генераторное выражение.
"""
from sys import argv
from random import randint

__all__ = ['game']


def game(start: int = 0, end: int = 1000, tries: int = 5) -> bool:
    num = randint(start, end)
    for _ in range(tries):
        enter = int(input("Отгадайте заданное число: "))
        if num > enter:
            print("больше")
        elif num < enter:
            print("меньше")
        else:
            break
    return enter == num


if __name__ == '__main__':
    arguments = map(int, argv[1:])
    print(game(*arguments))
