# GOOD PRACTICE
a = b = c = 0
a += 42
print(f'{a=} {b=} {c=}')  # a=42 b=0 c=0

# BAD PRACTICE
a = b = c = {1, 2, 3}
a.add(42)
print(f'{a=} {b=} {c=}')  # a={1, 2, 3, 42} b={1, 2, 3, 42} c={1, 2, 3, 42}

a, b, c = 1, 2, 3
print(f'{a=} {b=} {c=}') # a=1 b=2 c=3

t = 1, 2, 3
print(f'{t=}\t{type(t)}') # t=(1, 2, 3)	<class 'tuple'>
