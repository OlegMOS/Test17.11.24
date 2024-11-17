import requests
import pprint

params = {
    'q': 'html'
}

response = requests.get( 'https://api.github.com/search/repositories', params=params)

print(response.status_code)

if response.ok:
    print('Запрос успешно выполнен')
else:
    print('Произошла ошибка')

pprint.pprint(response.json())