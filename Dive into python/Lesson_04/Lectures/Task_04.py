def mutable(data: list[int]):
    for i, item in enumerate(data):
        data[i] = item + 1
    print((f'in function {data = }'))
    # return None


my_list = [2, 4, 6, 8]
print(f'in main {my_list = }')  # in main my_list = [2, 4, 6, 8]
new_list = mutable(my_list)
print(f'{my_list = }\n{new_list = }')
# my_list = [3, 5, 7, 9]
# new_list = None
