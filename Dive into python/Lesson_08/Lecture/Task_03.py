import json


# Преобразование Python в JSON

# сохранение dict или list в файле в виде JSON
# ● json.dump(my_dict, f)

# сохранение dict или list в виде JSON строки
# ● dict_to_json_text = json.dumps(my_dict)

# при попытке сериализовать тип данных который не поддерживается JSON ловим ошибку


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

# в данном способе русские символы удут нечитаемы в формате JSON
print(f'{type(my_dict) = }\n{my_dict}')
with(open('task_3.json', 'w')) as f:
    json.dump(my_dict, f)

# в данном способе русские символы читаются но нельзя использоать ASCII
print(f'{type(my_dict) = }\n{my_dict}')
with(open('task_3.json', 'w', encoding='utf-8')) as f:
    json.dump(my_dict, f, ensure_ascii=False)