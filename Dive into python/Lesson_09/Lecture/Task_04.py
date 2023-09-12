from typing import Callable


def add_one_str(a: str) -> Callable[[str], str]:
    text = ''

    def add_two_str(b: str) -> str:
        nonlocal text
        text += ', ' + b
        return a + text

    return add_two_str


hello = add_one_str('Hello')
buy = add_one_str('Good buy')

print(hello('Alex')) # Hello Alex
print(hello('Karina')) # Hello Alex, Karina
print(hello('Marina')) # Hello Alex, Karina, Marina
print(hello('Arina')) # Hello Alex, Karina, Marina, Arina
print(buy('Alina')) # Good buy Alina
print(buy('Malvina')) # Good buy Alina, Malvina