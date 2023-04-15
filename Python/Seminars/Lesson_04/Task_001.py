# Task 01

# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа разделителя используйте пробел. 
# Результат запишите в исходный файл (minn maxx)

f_path = 'test.txt'

# f = open('test.txt', 'r') эта конструкция плоха тем что нужно закрывать файл командой close
# 'r' - чтение
# 'w' - перезапись (если файла нет, его создадут)
# 'a' - дозапись
# 'r+' - чтение + запись

with open(f_path, 'r') as f_nums:
    list_nums = f_nums.read().split(' ')

for i in range(len(list_nums)):
    list_nums[i] = int(list_nums[i])

minmax_list = [min(list_nums), max(list_nums)]

with open(f_path, 'a') as min_max:
    min_max.writelines(f"\n {minmax_list} ")






