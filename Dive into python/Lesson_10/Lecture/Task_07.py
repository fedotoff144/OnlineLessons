"""
💡PEP-8! Между методами класса оставляется по одной пустой строке до и
после. Как вы помните в модуле до и после функции оставляют по две
пустые строки.
"""


class Person:
    max_up = 3

    def __init__(self, name, race='unknown'):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100


p1 = Person('Сильвана', 'Эльф')
p2 = Person('Иван', 'Человек')
p3 = Person('Грогу')

print(f'{p1.name = }, {p1.race = }')
# p1.name = 'Сильвана', p1.race = 'Эльф'
print(f'{p2.name = }, {p2.race = }')
# p2.name = 'Иван', p2.race = 'Человек'
print(f'{p3.name = }, {p3.race = }')
# p3.name = 'Грогу', p3.race = 'unknown'
