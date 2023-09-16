"""
● public — публичный доступ, т.е. возможность обратиться к свойству или
методу из любого другого класса и экземпляра
● protected — защищённый доступ, позволяющий обращаться к свойствам и
методам из класса и из классов наследников.
● private — приватный доступ, т.е. отсутсвие возмодности обратиться к свойству
или методы из другого класса или экземпляра.
"""


class Person:
    __max_up = 3
    _max_level = 80

    def __init__(self, name, race='unknown', speed=100):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100
        self._speed = speed
        self.up = 3

    def _check_level(self):
        return self.level < self._max_level

    def level_up(self):
        if self._check_level():
            self.level += 1

    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity

    def add_up(self):
        self.up += 1
        self.up = min(self.up, self.__max_up)


p1 = Person('Сильвана', 'Эльф', 120)
print(f'{p1.up = }')  # p1.up = 3

p1.up = 1
print(f'{p1.up = }')  # p1.up = 1

for _ in range(5):
    p1.add_up()
print(f'{p1.up = }')  # p1.up = 3

# print(p1.__max_up)  # __max_up is private so we have ERROR AttributeError: 'Person' object has no attribute '__max_up'
print(p1._Person__max_up)  # 3

print(Person._Person__max_up)  # 3
# print(Person.__max_up)  # __max_up is private so we have ERROR AttributeError: type object 'Person' has no attribute '__max_up'
