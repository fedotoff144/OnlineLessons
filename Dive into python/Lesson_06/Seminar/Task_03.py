"""
Создайте модуль с функцией внутри. Функция получает на вход загадку,
список с возможными вариантами отгадок и количество попыток на угадывание.
Программа возвращает номер попытки, с которой была отгадана загадка или ноль,
если попытки исчерпаны.
"""
from pack_of_modules.puzzle_module import game_guess_two

print(game_guess_two(riddle_number=1, variants=[1, 2, 3, 4], number_of_attempts=10))