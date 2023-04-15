# Task 1

# Реализуйте алгоритм задания случайных чисел без использования
# встроенного генератора псевдослучайных чисел (time).

import time


def my_rand(start_num=1, finish_num=1):
    while True:
        num = int(round(time.time() % 1, 1) * 10)
        if start_num <= finish_num:
            return num


print(my_rand())


# from datetime import datetime


# def get_random_number(n):
#     now = datetime.now()
#     random_number = now.time().second ** now.time().minute * now.time().microsecond
#     return random_number % 10**n


# print(get_random_number(3))
