# Task 01

# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите число.
# Например:
# 1 2 3 4 5 6 8 9 - не хватает 7

# # что сделать и с чем сделать
# numbs = [20, 50, 15]
# res = [item for item in if item > 30] # если поставить () на выводе получится кортеж, если {} получится множество

# numbs = ['20', '50', '15']
# res = tuple(map(int,numbs)) # на выходе получаем кортеж, при list вместо tuple получим список
# res = tuple(filter(int,numbs)) # если возвращается True то элемент попадает в коллекцию, если False то элемент не попадает

string_ = '1 2 3 4 5 6 8 9'
li = set(map(int, string_.split()))
li_1 = set(i for i in range(1, len(li)+1))
dif = li_1-li
print(*dif) # *распаковка


# Var 2
# res = [i for i in s.split() if 'абв' not in i]
# res_filt = filter(lambda item: 'абв' not in item, [i for i in s.split()])