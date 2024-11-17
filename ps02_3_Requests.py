import requests
import pprint

params = {'title': 'foo', 'body': 'bar', 'userId': 1}

response = requests.post( 'https://jsonplaceholder.typicode.com/posts', data=params)

print(response.status_code)

if response.ok:
    print('Запрос успешно выполнен')
else:
    print('Произошла ошибка')

#pprint.pprint(response.json())
print(f"Ответ - {response.json()}")