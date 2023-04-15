# Task 2

# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число. 
# ['213213', 'dsf653', 'dsf', 'fdh76']
# num = 3
# Вывод: '213213', 'dsf653'


def FindNum(list: list, num):
    for i in range(len(list)):
        if num in list[i]:
            print(list[i])

lst = ['213213', 'dsf653', 'dsf', 'fdh76']
num = input('Enter number: ')

FindNum(lst, num)