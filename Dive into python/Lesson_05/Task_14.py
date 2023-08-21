# Генераторы
# генераторы множеств

my_setcomp = {chr(i) for i in range(97, 123)}
print(my_setcomp)
# {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
for char in my_setcomp:
    print(char)


x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')

res = {i + j for i in x if i % 2 != 0 for j in y if j != 1}
print(f'{len(res)=}\n{res}')
# len(res)=19
# {3, 5, 133, 7, 9, 11, 15, 19, 25, 27, 29, 37, 721, 723, 725, 733, 121, 123, 125}