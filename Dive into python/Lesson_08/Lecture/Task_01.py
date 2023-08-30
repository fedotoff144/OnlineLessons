import json


# JSON (JavaScript Object Notation)

# загрузка JSON из файла и сохранение в dict или list
# ● json_file = json.load(user)

# загрузка JSON из строки и сохранение в dict или list
# ● json_list = json.loads(user)

with(open('user.json', 'r', encoding='utf-8')) as f:
    json_file = json.load(f)

print(f'{type(json_file) = }\n{json_file = }')
print(f'{json_file["name"] = }')
print(f'{json_file["address"] = }')
print(f'{json_file["address"]["geo"] = }')
print(f'{json_file["email"] = }')
