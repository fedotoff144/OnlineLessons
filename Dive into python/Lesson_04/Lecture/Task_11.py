"""Global variable"""

def func(y: int) -> int:
    global x
    x += 100 # not error
    print(f'in func {x = }')
    return y + 1

x = 42
print(f'in main {x = }')
z = func(x)
print(f'{x = }\n{z = }')