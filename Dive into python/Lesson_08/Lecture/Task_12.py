import pickle


def func(a, b, c):
    return a + b + c


my_dict = {
    "numbers": [42, 100, 1, 88],
    "functions": (func, sum, max),
    "others": {True, False, 'Hello world!'}
}

res = pickle.dumps(my_dict)
print(f'{res = }')

with open('my_dict.pickle', 'wb') as f:
    pickle.dump(my_dict, f)
