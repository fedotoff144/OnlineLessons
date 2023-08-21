# lambda parameters: action
# Анонимные функции, они же лямбда функции — синтаксический сахар для
# обычных питоновских функций с рядом ограничений. Они позволяют задать
# функцию в одну строку кода без использования других ключевых слов.

def add_to_def(a, b):
    return a + b


add_to_lambda = lambda a, b: a + b # функция анонимная поэтому ее присваивать ее переменной дурной тон

print(add_to_def(42, 3.14))
print(add_to_lambda(42, 3.14))

my_dict = {'two': 2, 'one': 1, 'four': 4, 'six': 6}
s_key = sorted(my_dict.items())
s_value = sorted(my_dict.items(), reverse=True, key=lambda x: x[1])
print(f'{s_key = }\n{s_value = }')
