import telebot
import random

from telebot import types
from random import choice

#Токен телеграм-бота
bot = telebot.TeleBot('1802145216:AAHgiNmQvIpM9IdsWA3_Wpw1drPe3HKCBnE')

#Приветственное сообщение при команде '/start'
@bot.message_handler(commands=['start'])
def zdarova(message):
    bot.send_message(message.chat.id, 'Privet', reply_markup=markup )

#Клавиатура
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton('Нажми на кнопку, и я отправлю тебе название фрукта')

markup.add(item1)

fruit = ['яблоко', 'банан', 'груша', 'персик']


@bot.message_handler(content_types=['text', 'photo'])
def messagelist(message):
  if message.text == 'Нажми на кнопку, и я отправлю тебе название фрукта':
    bot.send_message(message.chat.id, random.choice(fruit))
  else:
    bot.send_message(message.chat.id, 'ниче не понял')

#Запуск бота
bot.polling(none_stop=True, interval=0)