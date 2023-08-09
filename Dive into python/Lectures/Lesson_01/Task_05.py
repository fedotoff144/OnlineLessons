# break
min_limit = 0
max_limit = 10

while True:
    print('Enter number bitween ', min_limit, 'и ', max_limit)
    num = float(input())

    if num < min_limit or num > max_limit:
        print('Incorrect')
    else:
        break

print('Your number is: ', num)