import pickle


# Десериализация
# ● new_dict = pickle.load(f)
# загрузка из бинарного файла и сохранение в объекта
# ● new_dict = pickle.loads(data)
# получение объекта из бинарной строки


# func необходима для того чтобы выгрузить бинарный файл
def func(a, b, c):
    return a * b * c


data = b'\x80\x04\x95x\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x07numbers\x94]\x94(K*KdK\x01KXe\x8c\tfunctions\x94\x8c\x08__main__\x94\x8c\x04func\x94\x93\x94\x8c\x08builtins\x94\x8c\x03sum\x94\x93\x94h\x07\x8c\x03max\x94\x93\x94\x87\x94\x8c\x06others\x94\x8f\x94(\x89\x88\x8c\x0cHello world!\x94\x90u.'

new_dict = pickle.loads(data)
print(f'{new_dict = }')
