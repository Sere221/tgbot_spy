import telebot
from telebot import types

import _ip
import data
import eye_god as eg
import viki

bot = telebot.TeleBot(data.bot)
print("!ПОЕХАЛИ!")


@bot.message_handler(commands=['start', 'help'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Узнать свой IP')
    btn2 = types.KeyboardButton('Как это работает?')
    markup.row(btn1, btn2)

    bot.send_message(message.chat.id, 'Я к вашим услугам', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


@bot.message_handler(commands=['ph'])
def get_phone(message):
    text = message.text[4:]
    bot.send_message(message.chat.id, eg.get_phone(text))


@bot.message_handler(commands=['ip'])
def get_ip(message):
    text = message.text[4:]
    bot.send_message(message.chat.id, _ip.get_info_by_ip(text))


@bot.message_handler(commands=['hs'])
def get_host(message):
    text = message.text[4:]
    bot.send_message(message.chat.id, _ip.get_ip_by_hostname(text))


def on_click(message):
    if message.text == 'Как это работает?':
        bot.send_message(message.chat.id, 'Для пробитие номеров введите:\n'
                                          '/ph 89999999999\n\n'
                                          'Для пробитие по IP введите:\n'
                                          '/ip 127.12.12.1\n\n'
                                          'Для пробитие сайта по IP введите:\n'
                                          '/hs vk.com\n\n'
                                          'Есть что то нужно в википедии просто введите текст)')
    elif message.text == 'Узнать свой IP':
        bot.send_message(message.chat.id, _ip.get_my_ip())
        bot.register_next_step_handler(message, on_click)
    else:
        print('ОК')


@bot.message_handler(content_types=['text'])
def get_p(message):
        bot.send_message(message.chat.id, viki.viki(message.text))


if __name__ == '__main__':
    bot.polling(none_stop=True)