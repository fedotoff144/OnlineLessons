# изменяемый объект

# сожержит неизменяемый ключ
# ключи должны быть уникальными

# - dict(x) — создаём словарь
# - {key: value} — тоже создаём словарь
# - dict[key] — доступ через квадратные скобки []
# - dict.get(key[, default]) — доступ через метод get()


a = {'one': 42, 'two': 15, 'three': 'hello'}
b = dict(one=42, two=15, three='hello')
c = ([('one', 42), ('two', 3.14), ('ten', 'hello')])
print(a == b == c)

my_dict = {'one': 1, 'two': 2, 'three': 3}
x = 10
my_dict['ten'] = x
print(my_dict)  # {'one': 1, 'two': 2, 'three': 3, 'ten': 10}

print(my_dict['two'])  # 2
# print(my_dict[1]) # KeyError: 1

print(my_dict.get('two'))  # 2
print(my_dict.get('five'))  # None
print(my_dict.get('five', 5))  # 5
print(my_dict.get('ten', 5))  # 10

# - Метод setdefault() - Возвращает значение и добавляет ключ в словарь
# - Метод keys() - возвращает объект-итератор dict_keys
# - Метод values() - возвращает объект-итератор dict_values
# - Метод items() - возвращает объект-итератор dict_items
# - Метод popitem() - Удаляет последнюю пару ключ-значение
# - Метод pop() - Удаляет пару ключ-значение по ключу
# - Метод update() - Расширяет исходный словарь новыми парами


# Метод setdefault():
my_dict = {'one': 1, 'two': 2, 'three': 3}
value = my_dict.setdefault('four', 4)
print(my_dict)  # {'one': 1, 'two': 2, 'three': 3, 'four': 4}
print(value)  # 4
# В этом примере, метод setdefault() добавляет ключ 'four' со значением 4
# в словарь my_dict, так как ключа 'four' ранее не было в словаре.
# Метод также возвращает значение, которое было установлено для ключа 'four'
# в случае если начение присутствует, тогда выводится настоящее значение


# Метод keys():
my_dict = {'one': 1, 'two': 2, 'three': 3}
keys = my_dict.keys()
print(keys)  # dict_keys(['one', 'two', 'three'])

for key in my_dict.keys(): # keys() можно не указывать используется по дефолту
    print(key) # one two three
# В этом примере, метод keys() возвращает объект-итератор dict_keys,
# который содержит все ключи словаря my_dict.


# Метод values():
my_dict = {'one': 1, 'two': 2, 'three': 3}
values = my_dict.values()
print(values)  # dict_values([1, 2, 3])
# В этом примере, метод values() возвращает объект-итератор dict_values,
# который содержит все значения словаря my_dict.
for value in my_dict.values():
    print(value) # 1 2 3


# Метод items():
my_dict = {'one': 1, 'two': 2, 'three': 3}
items = my_dict.items()
print(items)  # dict_items([('one', 1), ('two', 2), ('three', 3)])
# В этом примере, метод items() возвращает объект-итератор dict_items,
# который содержит все пары ключ-значение словаря my_dict.

for tuple_data in my_dict.items(): # BAD CODE
    print(tuple_data) # BAD CODE

for key, value in my_dict.items(): # GOOD CODE
    print(f'{key = } value before 100 - {100 - value}') # GOOD CODE


# Метод popitem():
my_dict = {'one': 1, 'two': 2, 'three': 3}
item = my_dict.popitem()
print(f'{item = }\t{my_dict = }')  # item = ('three', 3)	my_dict = {'one': 1, 'two': 2}
# В этом примере, метод popitem() удаляет последнюю пару ключ-значение из словаря
# my_dict и возвращает её в виде кортежа.


# Метод pop():
my_dict = {'one': 1, 'two': 2, 'three': 3}
value = my_dict.pop('two')
print(f'{value = }\t{my_dict = }') # value = 2	my_dict = {'one': 1, 'three': 3}
# err = my_dict.pop('six') # KeyError: 'six'
# В этом примере, метод pop('two') удаляет пару ключ-значение с ключом 'two'
# из словаря my_dict и возвращает значение, которое было связано с этим ключом.


# Метод update():
my_dict = {'one': 1, 'two': 2}
new_dict = {'three': 3, 'four': 4}
my_dict.update(new_dict)
print(my_dict)  # {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = my_dict | {'five': 5, 'two': 2} | dict(six=6)
print(new_dict) # {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6}
# В этом примере, метод update() расширяет словарь my_dict
# новыми парами ключ-значение из словаря new_dict.


