import re
import time
from bs4 import BeautifulSoup
import requests
import twitter



url = 'https://www.packtpub.com/packt/offers/free-learning'

header = {}
header['Host'] = 'www.packtpub.com'
header['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0'
header['Accept'] = '*/*'
header['Accept-Language'] = 'en-US,en;q=0.5'
header['Accept-Encoding'] = 'gzip, deflate'
header['Upgrade-Insecure-Requests'] = '1'

r = requests.get(url, headers=header)
soup = BeautifulSoup(r.text, 'lxml')


consumer_key=''
consumer_secret='' 
access_token_key=''
access_token_secret=''


def send_message(message):
    api = twitter.Api(consumer_key=consumer_key,
                consumer_secret=consumer_secret,
                access_token_key=access_token_key,
                access_token_secret=access_token_secret)

    api.PostUpdate(message)


def get_packtpub():
    div = soup.find('div', class_='dotd-main-book-summary float-left')
    title = soup.h2.get_text().strip()
    patterns = 'Python|metaclasses|Django|scikit-learn'
    words = div.find_all(text=re.compile(patterns))

    if words:
        today = time.strftime("%d/%m")

        msg = "Free Ebook today({}): {}: {} #Python #PacktPub".format(today, title, url)

        send_message(msg)


if __name__ == "__main__":
    get_packtpub()
