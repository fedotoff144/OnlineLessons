print("Hello world!".__doc__) # (thunder method) просим документацию по значению
print(str.__doc__) # просим документацию по типу str


print("Hello world!".upper()) # HELLO WORLD
print("Hello world!".count('l')) # 3


# dir(object) - попытается вернуть список допустимых атрибутов для объекта
print(dir("Hello world!"))
# help(object) - страница справки по объекту
help(str)
help() # интерактивная справка, позволяет в терминале вводить запросы и читать документацию о них




