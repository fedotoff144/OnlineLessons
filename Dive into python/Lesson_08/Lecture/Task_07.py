import csv

# Чтение CSV в словарь
#
# csv_file = csv.DictReader(f, fieldnames=["name", "sex", "age",
# "height", "weight", "office"], restkey="new", restval="Main Office")
#
# ● fieldnames — список заголовков столбцов, ключей словаря
# ● restkey — значение ключа для столбцов, которых нет в fieldnames
# ● restval — значение поля для ключей fieldnames, которых нет в файле CSV

with open('new_file_1.csv', 'r', newline='') as f:
    csv_file = csv.DictReader(f, fieldnames=["name", "sex", "age", "height", "weight", "office"], restkey="new",
                              restval="empty", dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    for line in csv_file:
        print(f'{line = }') # line = {'name': 'Alex', 'sex': 'M', 'age': 42.0, 'height': 70.0, 'weight': 15.0, 'office': 'empty'}
        print(f'{line["name"] = }\t{line["age"] = }') # line["name"] = 'Alex'	line["age"] = 42.0
