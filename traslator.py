import requests
import json

text ="""
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
"""

url = f'http://api.mymemory.translated.net/get?q={text}&langpair=en|es'

response = requests.get(url)
values = json.loads(response.text)

print(values['responseData']['translatedText'])
