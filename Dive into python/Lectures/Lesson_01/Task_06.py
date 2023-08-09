count = 3
min_limit = 0
max_limit = 10
num = None

while count != 0:
    print('Trying #', count, ' Enter number: ')
    count -= 1

    print('Enter number bitween ', min_limit, 'и ', max_limit)
    num = float(input())
    if num < min_limit or num > max_limit:
        print('Incorrect')
    else:
        break

else:
    print('Oops... You don\'t have any trying!')
    quit()

print('Number is: ', num)
