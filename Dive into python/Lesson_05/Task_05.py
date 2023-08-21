a = b = c = 42

# if a == b and b == c:
if a == b == c:
    print('elments are equals')

if a < b < c:
    print('b is bigger a and less c')


"""worst code"""
a = 12; b = 42; c = 73
if a < b < c: b = None; print('worst code ever!')