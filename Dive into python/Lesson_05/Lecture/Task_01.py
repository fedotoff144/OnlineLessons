a = 5
b = 10
a, b = b, a
print(f'{a = }\t{b = }')

a, b, c = input('Enter number: ')  # 123
print(f'{a=} {b=} {c=}')  # a='1' b='2' c='3'

# a,b,c = input('Enter number: ') # 1234
# print(f'{a=} {b=} {c=}') # ValueError: too many values to unpack (expected 3)

data = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']

a, b, c, *d = data
print(f'{a=} {b=} {c=} {d=}') # a='one' b='two' c='three' d=['four', 'five', 'six', 'seven']

a, b, *c, d = data
print(f'{a=} {b=} {c=} {d=}') # a='one' b='two' c=['three', 'four', 'five', 'six'] d='seven'

a, b, c, d = data
print(f'{a=} {b=} {c=} {d=}') # a='one' b=['two', 'three', 'four', 'five'] c='six' d='seven'

# * МОЖНО УКАЗЫВАТЬ ТОЛЬКО У ОДНОЙ ПЕРЕМЕННОЙ!
