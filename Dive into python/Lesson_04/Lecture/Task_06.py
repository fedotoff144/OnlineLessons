def from_one_to_n(n, data=[]):
    for i in range(1, n+1):
        data.append(i)
    return data

new_list = from_one_to_n(5)
print(f'{new_list = }') # new_list = [1, 2, 3, 4, 5]
other_list = from_one_to_n(7)
print(f'{other_list = }') # other_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7]


def from_one_to_n(n, data=None):
    if data is None:
        data = []
    for i in range(1, n+1):
        data.append(i)
    return data

new_list = from_one_to_n(5)
print(f'{new_list = }') # new_list = [1, 2, 3, 4, 5]
other_list = from_one_to_n(7)
print(f'{other_list = }') # other_list = [1, 2, 3, 4, 5, 6, 7]