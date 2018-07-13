import requests
import json


# movie = input('Search the movie: ')
# apikey = ''


class MovieSearch:
    def __init__(self, key):
        self.key = key

    def get_movie(self, title, plot=None):
        self.url = f'http://www.omdbapi.com/?t={title}&y=&plot={plot}&r=json&apikey={self.key}'
        self.response = requests.get(self.url)
        self.values = json.loads(self.response.text)
        # return self.values

    def all(self):
        for k, v in self.values.items():
            print(k, ':', v)

    def get(self, item):
        return self.values[item.title()]
