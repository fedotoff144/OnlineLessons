# Параметры *args и **kwargs
# Имена args и kwargs — общепринятое соглашение
# ✔ def func(*args): — принимает любое число
# позиционных аргументов
# ✔ def func(**kwargs): — принимает любое
# число ключевых аргументов
# ✔ def func(*args, **kwargs): — принимает любое
# число позиционных и ключевых аргументов

def mean(args):
    return sum(args) / len(args)


print(mean([1, 2, 3]))
# print(mean(1, 2, 3))  # TypeError: mean() takes 1 positional argument but 3 were given


def mean(*args):
    return sum(args) / len(args)

print(mean(*[1, 2, 3]))
# args со * превращается в картеж, происходит распковка
print(mean(1, 2, 3))


def school_print(**kwargs):
    for key, value in kwargs.items():
        print(f'По предмету "{key}" получена оценка {value}')

school_print(химия=5, физика=4, математика=90, русский_язык=90)