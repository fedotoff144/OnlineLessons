# Task 3
# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

#s1 = input()
#s2 = input()
# print(s1.count(s2))

# s1 = 'Я люблю Python'
# s2 = 'лю'
# cnt = 0
# while s2 in s1:
#     s1 = s1.replace(s2, ' ', 1)
#     print(s1)
#     cnt += 1
# print(cnt)


# s1 = 'Я люблю люблюлюблюPython'
# s2 = 'люблю'
# res = s1.split(s2)
# print(len(res) - 1)


s1 = 'Я люблю Python'
s2 = 'лю'
i = 0
cnt = 0
while i < len(s1) - 1:
    if s1[i: len(s2) + i] == s2:
        cnt += 1
    i += 1
print(cnt)
