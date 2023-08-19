# Три друга взяли вещи в поход. Сформируйте словарь,
# где ключ - имя друга, а значение - кортеж вещей.
#
# Ответьте на вопросы:
# - какие вещи взяли все три друга
# - какие вещи уникальны, есть только у одного из друзей.
# - какие вещи есть у всех друзей кроме одного и имя того,
# у кого данная вещь отсутствует
# - для решения используйте операции с множествами.
# Код должен расширяться на любое количество друзей.

item_dict = {'Vasya':{'backpack', 'tent', 'rope', 'pan'},
             'Petya':{'backpack', 'tent', 'lamp', 'pan'},
             'Fedya':{'backpack', 'tent', 'lamp', 'bike'}}

# for key, value in item_dict.items():

res_1 = (item_dict['Vasya'] & item_dict['Petya'] & item_dict['Fedya'])

res_2 = (item_dict['Vasya'] - item_dict['Petya'] - item_dict['Fedya'])
print(f'{res_1}\n{res_2}')


