# Зарезервированное слово in позволяет сделать
# проверку на вхождение элемента в коллекцию.
# Возвращает True or False

# Линейное время проверки вхождения:
# ✔ obj in list
# ✔ obj in tuple
# ✔ sub_str in str

# Константное время проверки вхождения:
# ✔ key in dict
# ✔ obj in set
# ✔ obj in frozenset

my_set = {1, 2, 3, 4, 2, 5, 6, 7}
print(42 in my_set) # False
print(3 in my_set) # True