import requests


params = {
    'q': 'python'
}

response = requests.get( 'https://api.github.com/search/repositories', params=params)