import requests
import pprint

params = {
    'userId': '1'
}

response = requests.get( 'https://jsonplaceholder.typicode.com/posts', params=params)

print(response.status_code)

if response.ok:
    print('Запрос успешно выполнен')
else:
    print('Произошла ошибка')

#pprint.pprint(response.json())
print(response.text)