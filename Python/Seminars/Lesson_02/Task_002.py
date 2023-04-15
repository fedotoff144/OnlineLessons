# Task 2
# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Пример:
# Для n = 6: 4, 7, 10, 13, 16, 19


# result = {}
# n = int(input())

# for i in range(1, n + 1):
#     result[i] = 3 + n + 1
# print(result)

n = int(input())
i = 1
while i <= n:
    print(3*i+1, end=', ')
    i += 1

