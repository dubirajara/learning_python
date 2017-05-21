import re
from bs4 import BeautifulSoup
import requests
# from datetime import datetime
# from threading import Timer


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


def get_packpub():
    div = soup.find('div', class_='dotd-main-book-summary float-left')
    words = div.find_all(text=re.compile('Python'))

    if words:
        thumbnails = soup.select('div.dotd-main-book-image.float-left img')
        thumb = 'http:' + thumbnails[0].get('src')
        print(thumb)
        print(soup.h2.get_text().strip())

        for word in words:
            print(word)

    else:
        print('no match')
#     cron_task()


# def cron_task():

#     dt1 = datetime.today()
#     dt2 = dt1.replace(day=dt1.day+1, hour=13, minute=27, second=0, microsecond=0)
#     delta_t = dt2 - dt1
#     secs = delta_t.seconds + 1

#     task = Timer(secs, get_packpub)
#     task.start()


get_packpub()
