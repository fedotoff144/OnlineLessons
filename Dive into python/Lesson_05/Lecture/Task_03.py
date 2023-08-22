data = [1, 2, 3, 4, 5, 6]
for i in data:
    print(i, end='\t') # 1	2	3	4	5	6

print()

data = [1, 2, 3, 4, 5, 6]
print(*data, sep='\t') # 1	2	3	4	5	6
