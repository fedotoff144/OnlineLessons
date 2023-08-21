# Генераторы

"""
Общий вид выражения:
gen = (expression for expr in sequense1 if condition1
    for expr in sequense2 if condition2
    for expr in sequense3 if condition3
    ...
    for expr in sequenseN if conditionN)
"""

"""
Аналог на Python:
for expr in sequense1:
    if not condition1:
        continue
    for expr in sequense2:
        if not condition2:
            continue
    ...
        for expr in sequenseN:
            if not conditionN:
                continue
"""

my_gen = (chr(i) for i in range(97, 123))
print(my_gen)

for char in my_gen:
    print(char)