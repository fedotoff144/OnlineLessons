import os
import pickle


# Модуль Pickle
# Модуль pickle не занимается проверкой потока байт на безопасность
# перед распаковкой. Не используйте его с тем набором байт,
# безопасность которого не можете гарантировать.


# передает в консоль команду os.system('echo Hello world!')
res = pickle.loads(b"cos\nsystem\n(S'echo Hello world!'\ntR.")
print(f'{res = }')

# пример переданной в консоль команды напрямую
os.system('echo Hello world!')

