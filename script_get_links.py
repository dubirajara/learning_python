import re
import requests

header = {'user-agent': 'my-app/0.0.1'}
url = 'https://www.packtpub.com/packt/offers/free-learning'
r = requests.get(url, headers=header)
links = re.findall('"((http|ftp)s?://.*?)"', r.text)

print(links)

# from bs4 import BeautifulSoup

# soup = BeautifulSoup(r.content, 'lxml')

# for link in soup.find_all('a', href=True):
#   print(link['href'])
