from typing import Callable


def add_one_str(a: str) -> Callable[[str], str]:
    def add_two_str(b: str) -> str:
        return a + ' ' + b

    return add_two_str


hello = add_one_str('Hello')
buy = add_one_str('Good buy')


print(hello('world!'))
print(hello('friends!'))
print(buy('wonderful world!'))

print(f'{type(add_one_str) = }, {add_one_str.__name__ = }, {id(add_one_str) = }')
print(f'{type(hello) = }, {hello.__name__ = }, {id(hello) = }')
print(f'{type(buy) = }, {buy.__name__ = }, {id(buy) = }')
# type(add_one_str) = <class 'function'>, add_one_str.__name__ = 'add_one_str', id(add_one_str) = 3075569615200
# type(hello) = <class 'function'>, hello.__name__ = 'add_two_str', id(hello) = 3075577709760
# type(buy) = <class 'function'>, buy.__name__ = 'add_two_str', id(buy) = 3075578010784