num = int(input('Enter number: '))
for i in range(0, num, 2): # range(start, stop, step)
    print(i)

# for i in range(0, num, 2):  -> range(start, end, step)
# for i in range(0, num):  -> range(start, stop)
# for i in range(num):  -> range(stop)