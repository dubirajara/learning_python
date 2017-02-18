from telegram.ext import Updater, CommandHandler
from time import strftime
from bs4 import BeautifulSoup
import requests

up = Updater('TOKEN')


def start(bot, update):

    msg = f'Hola {update.message.from_user.first_name}, Bienvenido al Bot Test: '

    bot.sendMessage(cat_id=update.message.chat_id, text=msg)


def hola_mundo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='¡Hello World!')


def image(bot, update):
    bot.sendPhoto(
        chat_id=update.message.chat_id,
        photo=open('python.png', 'rb'))


def clima(bot, update):
    url = 'http://www.timeanddate.com/weather/spain/madrid'
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'lxml')
    temp = soup.find_all('div', class_='h2')
    term = soup.find_all('div', class_='clear')
    thour = soup.find_all(id='wtct')

    bot.sendMessage(chat_id=update.message.chat_id,
                    text=f'La temperatura en Madrid: {temp[0].text}\
                            \nLa sensacion termica: {term[1].text}\
                            \n{thour[0].text}')


def horas(bot, update):
    msg = f'Hola {update.message.from_user.first_name}, ahora son las: {strftime('%H:%M')}'

    bot.send_message(chat_id=update.message.chat_id, text=msg)


up.dispatcher.add_handler(CommandHandler('start', start))
up.dispatcher.add_handler(CommandHandler('holamundo', hola_mundo))
up.dispatcher.add_handler(CommandHandler('img', image))
up.dispatcher.add_handler(CommandHandler('clima', clima))
up.dispatcher.add_handler(CommandHandler('horas', horas))

up.start_polling()
