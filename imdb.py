import requests
import json


movie = input('Search the movie: ')

url = f'http://www.omdbapi.com/?t={movie}&y=&plot=full&r=json'

response = requests.get(url)
values = json.loads(response.text)

for i, y in values.items():
    print(i, ':', y)
