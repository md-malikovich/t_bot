import telebot
import COVID19Py
import requests

covid19 = COVID19Py.COVID19()
latest = covid19.getLatest()
print(latest)



bot = telebot.TeleBot('5240060860:AAHsRsNGwO_538Nv7hD_jQVFuVHxEiwBzP8')



#bot.polling(none_stop=True)












# import telebot
# from telebot import types
#
# bot = telebot.TeleBot('5240060860:AAHsRsNGwO_538Nv7hD_jQVFuVHxEiwBzP8')
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
#     bot.send_message(message.chat.id, mess, parse_mode='html')


# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text == 'Hello':
#         bot.send_message(message.chat.id, 'Hi', parse_mode='html')
#     elif message.text == 'Id':
#         bot.send_message(message.chat.id, f'Your ID is {message.from_user.id}', parse_mode='html')
#     elif message.text == 'Photo':
#         photo = open('icon.jpg', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, "I don't understand you!", parse_mode='html')

#
# @bot.message_handler(content_types=['photo'])
# def get_user_photo(message):
#     bot.send_message(message.chat.id, "It's cool!")
#
#
# @bot.message_handler(commands=['website'])
# def website(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("Посетить сайт", url="https://mypets.kg"))
#     bot.send_message(message.chat.id, "Добро пожаловать на сайт MyPets.kg!", reply_markup=markup)
#
#
# @bot.message_handler(commands=['mypets'])
# def website(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     my_pets_btn = types.KeyboardButton('Website')
#     start_btn = types.KeyboardButton('Start')
#     markup.add(my_pets_btn, start_btn)
#
#     # markup.add(types.InlineKeyboardButton("Посетить сайт", url="https://mypets.kg"))
#     bot.send_message(message.chat.id, "Добро пожаловать на сайт MyPets.kg!", reply_markup=markup)
#
#
# bot.polling(none_stop=True)
