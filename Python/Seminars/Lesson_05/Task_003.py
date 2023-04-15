# Task 3

# Напишите программу, удаляющую все слова, содержащие "абв"

my_string = 'Я люблю абвЖвау иабв Питон'

my_li = my_string.split()
print(my_li)

my_li = list(filter(lambda el: not "абв" in el, my_li))
print(my_li)

my_string = ' '.join(my_li)
print(my_string)


# def func(a_1, a_2, a_3):
#     return a_1, a_2, a_3

# args = {
# 'a_1': 1,
# 'a_3': 3,
# 'a_2': 2
# }
# print(func(a_1=1, a_2=2, a_3=3))
# print(func(**args))