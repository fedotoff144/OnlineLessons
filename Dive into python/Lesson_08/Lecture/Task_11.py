import pickle


# Сериализация
# ● pickle.dump(my_dict, f)
# сохранение объекта в бинарном файле
# ● result = pickle.dumps(my_dict)
# сохранение объекта в строку байт


my_dict = {
      "id": 2,
      "name": "Harry Potter",
      "username": "snake",
      "email": [
        "fedotoff144@gmail.com",
        "fedotoff144@inbox.ru"
      ],
      "address": {
        "street": "Ленина",
        "city": "Владимир",
        "zipcode": 601901,
        "geo": {
          "lat": "-43.9522",
          "lng": "-50.5050"
        }
      },
      "phone": "89109004567",
      "company": {
        "name": "VKU",
        "phone": "88005552233"
      }
    }
print(f'{my_dict = }')
res = pickle.dumps(my_dict, protocol=pickle.DEFAULT_PROTOCOL)
print(f'{res = }')
print(f'{pickle.DEFAULT_PROTOCOL}')
