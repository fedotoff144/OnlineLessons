# Генераторы
# генераторы словарей

my_dictcomp = {i: chr(i) for i in range(97, 123)}
print(my_dictcomp)
# {97: 'a', 98: 'b', 99: 'c', 100: 'd',... 120: 'x', 121: 'y', 122: 'z'}

for number, char in my_dictcomp.items():
    print(f'dict[{number}]={char}')
# dict[97]=a
# dict[98]=b
# dict[99]=c
# dict[100]=d
# dict[101]=e
# ...