import telebot
from telebot import types

import src.menu as menu
import src.logic as logic
import config


token = config.token
try:
    if token == '':
        print("НУЖНО ВСТАВИТЬ ТОКЕН")
        raise Exception
    bot = telebot.TeleBot(token)
except Exception as exc:
    print("Что-то не так с твоим токеном :(")


@bot.message_handler(commands=['start'])
def start_commands(message):
    """
    С помощью команды start/help начинается работа бота, отображение меню
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton(menu.menu['button_1'])
    button_2 = types.KeyboardButton(menu.menu['button_2'])
    button_3 = types.KeyboardButton(menu.menu['button_3'])
    button_4 = types.KeyboardButton(menu.menu['button_4'])
    button_5 = types.KeyboardButton(menu.menu['button_5'])
    button_6 = types.KeyboardButton(menu.menu['button_6'])

    markup.add(button_1)
    markup.add(button_2)
    markup.add(button_5, button_6)
    markup.add(button_3, button_4)

    bot.send_message(message.chat.id, "Добро пожаловать в КонвертерБот.", reply_markup=markup)


@bot.message_handler(commands=['help'])
def help_commands(message):
    bot.send_message(message.chat.id, menu.message_about_me)


@bot.message_handler(content_types=['text'])
def check_next_step(message):
    """
    Указатель на следующие шаги
    """
    if message.text == menu.menu['button_1']:
        string = "Введите сокращённое имя валюты(пример: USD):\n"
        bot.send_message(message.chat.id, string)
        bot.register_next_step_handler(message, get_short_name_of_currency)

    elif message.text == menu.menu['button_2']:
        string = "Введите сокращённое имя пары валют(пример: USD/EUR):\n"
        bot.send_message(message.chat.id, string)
        bot.register_next_step_handler(message, get_two_short_name_of_currency)

    elif message.text == menu.menu['button_3']:
        result_string = logic.return_all_currency()
        bot.send_message(message.chat.id, result_string)

    elif message.text == menu.menu['button_4']:
        bot.send_message(message.chat.id, menu.message_about_me)

    elif message.text == menu.menu['button_5']:
        string = "Введите дату и сокращённое имя валюты\n(пример: 28/04/2015 USD):\n"
        bot.send_message(message.chat.id, string)
        bot.register_next_step_handler(message, get_past_date)

    elif message.text == menu.menu['button_6']:
        string = "Введите дату и сокращённую валютную пару\n(пример: 28/04/2015 USD/EUR):\n"
        bot.send_message(message.chat.id, string)
        bot.register_next_step_handler(message, get_two_past_date)

    else:
        bot.send_message(message.chat.id, menu.menu['none'])


@bot.message_handler(content_types=['text'])
def get_short_name_of_currency(message):
    result_string = logic.return_price_of_currency(message.text)
    bot.send_message(message.chat.id, result_string)


@bot.message_handler(content_types=['text'])
def get_two_short_name_of_currency(message):
    result_string = logic.return_two_price_of_currency(message.text)
    bot.send_message(message.chat.id, result_string)


@bot.message_handler(content_types=['text'])
def get_past_date(message):
    result_string = logic.return_past_price_of_currency(message.text)
    bot.send_message(message.chat.id, result_string)


@bot.message_handler(content_types=['text'])
def get_two_past_date(message):
    result_string = logic.return_two_past_price_of_currency(message.text)
    bot.send_message(message.chat.id, result_string)


bot.polling()
