# Генераторы
# генераторы списков

# Listcomprehentions
data = [2, 5, 1, 42, 65, 76, 24, 77]
res = [item for item in data if item % 2 == 0]
print(f'{res = }') # res = [2, 42, 76, 24]


data = [2, 5, 1, 42, 65, 76, 24, 77]
res = []
for item in data:
    if item % 2 == 0:
        res.append(item)

print(f'{res = }') # res = [2, 42, 76, 24]

