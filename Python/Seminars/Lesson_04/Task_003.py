# Task 3

# Задайте два числа. Напишите программу,
# которая найдет НОК (наименьшее общее кратное) этих двух чисел.



def nok(a, b):
    k = 1
    while True:
        if a % k == 0 and b % k == 0:
            return k
        k += 1


print(nok(27, 9))



# rom sympy.solvers


# def fun(a, b, c):
#     x = Symbol('x')
#     return solve(f'{a}*x**2+{b}*x+{c}', x)


# print('Корни уравнения:', *fun(1, -16, 28))
