import re
import requests

header = {'user-agent': 'my-app/0.0.1'}
url = 'https://www.packtpub.com/packt/offers/free-learning'
r = requests.get(url, headers=header)
links = re.findall('"((http|ftp)s?://.*?)"', r.text)

print(links)