"""
💡PEP-8! Имя self не является зарезервированным. Вместо него можно
использовать любое. Но соглашение о написании кода требует писать
self. Так ваш код поймут другие разработчики, а IDE верно его
проанализируют.

В некоторых языках при написании кода используется запись this.name.
"""


class Person:
    max_up = 3

    def __init__(self):
        self.level = 1
        self.health = 100


p1 = Person()
p2 = Person()

# 💡 сам класс не имеет доступа к параметрам level и health
# print(f'{Person.level = }')
# AttributeError: type object 'Person' has no attribute 'level'
# print(f'{Person.max_up = }, {Person.level = }, {Person.health = }')
# AttributeError: type object 'Person' has no attribute 'level'

# 💡 экземпляры класса имеют доступ к параметрам level и health
print(f'{p1.max_up = }, {p1.level = }, {p1.health = }')
# p1.max_up = 3, p1.level = 1, p1.health = 100
print(f'{p2.max_up = }, {p2.level = }, {p2.health = }')
# p2.max_up = 3, p2.level = 1, p2.health = 100

Person.level = 100
print(f'{Person.level = }, {p1.level = }, {p2.level = }')
# Person.level = 100, p1.level = 100, p2.level = 100
