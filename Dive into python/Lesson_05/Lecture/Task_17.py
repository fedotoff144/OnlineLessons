def factorial_yield(n):
    number = 1
    for i in range(1, n+1):
        number *= i
        yield number


my_iter = iter(factorial_yield(4))
print(my_iter)
print(next(my_iter)) # 1
print(next(my_iter)) # 2
print(next(my_iter)) # 6
print(next(my_iter)) # 24
# print(next(my_iter)) # StopIteration