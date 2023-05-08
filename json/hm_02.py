import random
import requests
import json

# Получаем данные с сайта
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
data = response.json()

# Создаем файл и записываем в него данные в формате JSON
with open("data.json", "w") as f:
    json.dump(data, f)



# Получаем данные с сайта
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
data = response.json()

# Создаем файл и записываем в него данные в формате JSON
with open("data.json", "w") as f:
    json.dump(data, f)



# Генерируем 100 словарей
data = []
for i in range(100):
    d = {
        "id": i+1,
        "name": f"Item {i+1}",
        "value": random.randint(1, 100)
    }
    data.append(d)

# Записываем словари в JSON файл
with open("data.json", "w") as f:
    json.dump(data, f)
