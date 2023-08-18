# Задача №3
# Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление. Функции bin и oct используйте для проверки своегорезультата, а не для решения. Дополнительно: Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления. Избегайте магических чисел. Добавьте аннотацию типов где это возможно

num = 10
process_num = num
res = ''
BIN_DIV = 2
OCT_DIV = 8

while process_num > 0:
    res += str(process_num % BIN_DIV)
    process_num //= BIN_DIV

res = res[::-1]
print(res, bin(num))


# while process_num > 0:
#     res += str(process_num % OCT_DIV)
#     process_num //= OCT_DIV
#
# res = res[::-1]
# print(res, oct(num))