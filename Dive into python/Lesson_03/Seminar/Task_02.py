# Полльзователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# - целое положительное число
# - вещественное положительное или отрицательное число
# - в строку в нижнем регистре, если в строке есть хотя бы
#  одна заглавная буква
# - в строку в верхнем регистре во всех остальных случаях


atributes = ['qwqw', '1221', '12.01', 'amFanf',
             'fafna.jfn11245', '-12']

for attr in atributes:
    if attr.lstrip('-').isdigit():
        res = abs(int(attr))
        print(res, type(res))

    elif attr.count('.') == 1:
        if attr.replace('.', '', 1).isdigit():
            res = float(attr)
            print(res, type(res))

    elif attr != attr.lower():
        print((attr.lower()))

    else:
        print(attr.upper())