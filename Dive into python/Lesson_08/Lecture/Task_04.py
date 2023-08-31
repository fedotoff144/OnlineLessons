import json


# Дополнительные параметры dump и dumps
#
# res = json.dumps(my_dict, indent=2,
# separators=(',', ':'),
# sort_keys=True)
#
# ● Параметр indent отвечает за форматирование с отступами
# ● Параметр separators принимает на вход кортеж из двух строковых элементов.
# Первый — символ разделитель элементов.
# Второй — разделитель ключа и значения.
# ● Параметр sort_keys отвечает за сортировку ключей по алфавиту


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

res = json.dumps(my_dict, ensure_ascii=False, indent=2, separators=(',', ': '), sort_keys=True)
print(res)

# with(open('task_4.json', 'w', encoding='utf-8')) as f:
#     json.dumps(my_dict, f, ensure_ascii=False, indent=2, separators=(',', ': '), sort_keys=True)