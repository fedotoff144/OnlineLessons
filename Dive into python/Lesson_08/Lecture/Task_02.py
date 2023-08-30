import json

json_text = """
[
    {
      "id": 2,
      "name": "Harry Potter",
      "username": "snake",
      "email": [
        "fedotoff144@gmail.com",
        "fedotoff144@inbox.ru"
      ],
      "address": {
        "street": "Lenina",
        "city": "Vladimir",
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
]
"""

print(f'{type(json_text) = }\n{json_text = }') # type(json_text) = <class 'str'>
json_list = json.loads(json_text)
print(f'{type(json_list) = }\t{len(json_list) = }\n{json_list = }') # type(json_list) = <class 'list'>	len(json_list) = 1
