import csv


# CSV (Comma-Separated Value)

# параметр newline='' для работы с CSV
# ● with open('biostats.csv', 'r', newline='') as f:

# csv_file позволяет построчно читать csv файл в список list
# ● csv_file = csv.reader(f)


# при данном подходе все цифры записываются в формате str
with open('new_file.csv', 'r', newline='') as f:
    csv_file = csv.reader(f)
    for line in csv_file:
        print(line)
        print(type(line))

# use ',' as separator


# при данном подходе все цифры записываются в формате int
with open('new_file_1.csv', 'r', newline='') as f:
    csv_file = csv.reader(f, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    for line in csv_file:
        print(line)
        print(type(line))

# dialect='excel-tab' - use tab as separator
# quoting=csv.QUOTE_NONNUMERIC - если значение в "" то принимается как str,
# если без "" то как int