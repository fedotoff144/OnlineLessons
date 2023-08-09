year = int(input('Enter year: '))

if year % 4 != 0:
    print('Обычный год')
elif year % 100 == 0:
    if year % 400 == 0:
        print('Високосный год')
    else:
        print('Обычный год')
else:
    print('Високосный год')


# same code bottom
if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
    print('Обычный год')
else:
    print('Високосный год')

