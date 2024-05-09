import config
import telebot
import requests
from bs4 import BeautifulSoup as BS

r = requests.get('https://world-weather.ru/pogoda/russia/moscow/7days')
html = BS(r.content, 'html.parser')
bot = telebot.TeleBot(config.token)

for el in html.select('#content'):
    t_night = el.select('.night.weather-day')[0].text
    print("Температура ночью равна: ", t_night)
    t_morning = el.select('.morning.weather-day')[0].text
    print("Температура утром равна: ", t_morning)
    t_day = el.select('.day.weather-day')[0].text
    print("Температура днём равна: ", t_day)
    t_evening = el.select('.evening.weather-day')[0].text
    print("Температура вечером равна: ", t_evening)


@bot.message_handler(commands=['start', 'help'])
def main(message):
    bot.send_message(message.chat.id, "Приветствую тебя, странник!")


if __name__== '__main__':
    bot.polling(none_stop=True)
