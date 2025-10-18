# import telebot
# import webbrowser
# from telebot import types

# bot = telebot.TeleBot('8327887897:AAFvap9nzXkFUgc46ao6Zgc5PZCpEHL09dw')

# @bot.message_handler(commands=['site', 'website'])
# def site (message):
#     webbrowser.open('https://www.google.com')
#
#
#
# @bot.message_handler(commands=['start', 'help', 'main'])
# def send_welcome(message):
#     bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
#
#
# @bot.message_handler(commands=['help'])
# def send_welcome(message):
#     bot.send_message(message.chat.id, '<b>Помоги мне</b>', parse_mode='html')
#
#
#
# @bot.message_handler(commands=['hello'])
# def send_welcome(message):
#     bot.send_message(message.chat.id, 'Привет, я всего лишь маленькая кошечка')
#
# @bot.message_handler()
# def echo(message):
#     if message.text.lower() == 'hello':
#         bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
#     elif message.text.lower() == 'id':
#         bot.reply_to(message, f'ID: {message.from_user.id}')


# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup()
#     btn1 = types.KeyboardButton('Перейти на сайт')
#     markup.row(btn1)
#     btn2 = types.KeyboardButton('Удалить фото')
#     btn3 = types.KeyboardButton('Изменить текст')
#     markup.row(btn2, btn3)
#     file = open('./main1.jpg', 'rb')
#     bot.send_photo(message.chat.id, file, reply_markup=markup)
#     # bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
#     bot.register_next_step_handler(message, on_click)
#
# def on_click(message):
#     if message.text == 'Перейти на сайт':
#         bot.send_message(message.chat.id, 'Website is open')
#     elif message.text == 'Удалить фото':
#         bot.send_message(message.chat.id, 'Photo is delete')
#
#
# @bot.message_handler(content_types=['photo', 'audio'])
# def get_photo(message):
#     markup = types.InlineKeyboardMarkup()
#     btn1= types.InlineKeyboardButton('Перейти на сайт', url='https://google.com')
#     markup.row(btn1)
#     btn2= types.InlineKeyboardButton('Удалить фото', callback_data="delete")
#     btn3=types.InlineKeyboardButton('Изменить текст', callback_data="edit")
#     markup.row(btn2 , btn3)
#     bot.reply_to(message, 'Какое красивое фото', reply_markup=markup)
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     if call.data == 'delete':
#         bot.delete_message(call.message.chat.id, call.message.message_id - 1)
#     elif call.data == 'edit':
#         bot.edit_message_text('Edit text', call.message.chat.id, call.message.message_id)
#
#
#
# bot.polling(none_stop=True)


# import telebot
# import sqlite3
#
# bot = telebot.TeleBot('8327887897:AAFvap9nzXkFUgc46ao6Zgc5PZCpEHL09dw')
# name = None
#
#
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     conn = sqlite3.connect('user.sql')
#     cur = conn.cursor()
#
#     cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, password TEXT)')
#     conn.commit()
#     cur.close()
#     conn.close()
#
#     bot.send_message(message.chat.id, 'Привет, сейчас тебя зарегистрируем! Введите ваше имя')
#     bot.register_next_step_handler(message, user_name)
#
# def user_name(message):
#     global name
#     name = message.text.strip()
#     bot.send_message(message.chat.id, 'Введите пароль')
#     bot.register_next_step_handler(message, user_password)
#
#
# def user_password(message):
#     password = message.text.strip()
#     conn = sqlite3.connect('user.sql')
#     cur = conn.cursor()
#
#     cur.execute("INSERT INTO users (name, password) VALUES (?, ?)", (name, password))
#     conn.commit()
#     cur.close()
#     conn.close()
#
#     markup = telebot.types.InlineKeyboardMarkup()
#     markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='users'))
#
#     bot.send_message(message.chat.id, 'Пользователь зарегистрирован ✅', reply_markup=markup)
#
# @bot.callback_query_handler(func=lambda call: call.data == 'users')
# def callback(call):
#     conn = sqlite3.connect('user.sql')
#     cur = conn.cursor()
#
#     cur.execute('SELECT * FROM users')
#     users = cur.fetchall()
#
#     info = ''
#     for el in users:
#         info+=f'Имя: {el[1]}, пароль: {el[2]}\n'
#
#     cur.close()
#     conn.close()
#     bot.send_message(call.message.chat.id, info)
#
#     markup = telebot.types.InlineKeyboardMarkup()
#     markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='users'))
#     # bot.send_message(call.message.chat.id, 'Пользователь зарегистрирован', reply_markup=markup)
#
#
# bot.polling(none_stop=True)


# import telebot
# import requests
# import json
#
# bot = telebot.TeleBot('8327887897:AAFvap9nzXkFUgc46ao6Zgc5PZCpEHL09dw')
# API = 'd319b58e7b8c1b1e73e5824747b38553'
#
#
#
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.send_message(message.chat.id, 'Привет, рад тебя видеть. Напиши название городе.')
#
# @bot.message_handler(content_types=['text'])
# def get_weather(message):
#     city = message.text.strip().lower()
#     res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
#     # bot.reply_to(message, f'Сейчас погода: {res.json()}')
#
#     if res.status_code == 200:
#
#         data = json.loads(res.text)
#         templ = data['main']['temp']
#         bot.reply_to(message, f'Сейчас погода: {templ} ')
#
#         image = 'i.png' if templ >5.0 else 'i2.png'
#         file = open('./' +image, 'rb')
#         bot.send_photo(message.chat.id, file)
#     else:
#         bot.reply_to(message, f'Город указан неверно!')
#
# bot.polling(none_stop=True)





# import telebot
# from currency_converter import CurrencyConverter
# from telebot import types
#
# bot = telebot.TeleBot('8327887897:AAFvap9nzXkFUgc46ao6Zgc5PZCpEHL09dw')
# currency = CurrencyConverter()
# amount = 0
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'Привет, введите сумму: ')
#     bot.register_next_step_handler(message, summa)
#
#
# def summa(message):
#     global amount
#     try:
#         amount = int(message.text.strip())
#     except ValueError:
#         bot.send_message(message.chat.id, 'Неверный формат. Впешите сумму!')
#         bot.register_next_step_handler(message, summa)
#         return
#
#     if amount > 0:
#         markup = types.InlineKeyboardMarkup(row_width=2)
#         btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
#         btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
#         btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')
#         btn4 = types.InlineKeyboardButton('Другое значение', callback_data='else')
#         markup.add(btn1, btn2, btn3, btn4)
#         bot.send_message(message.chat.id, 'Выберите пару валют: ', reply_markup=markup)
#     else:
#         bot.send_message(message.chat.id, 'Число должно быть больше нуля. Впешите сумму!')
#         bot.register_next_step_handler(message, summa)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     if call.data !='else':
#         values = call.data.upper().split('/')
#         res = currency.convert(amount, values[0], values[1])
#         bot.send_message(call.message.chat.id, f'Получается: {res:.2f}. Можете заново написать сумму.')
#         bot.register_next_step_handler(call.message, summa)
#     else:
#         bot.send_message(call.message.chat.id, 'Введите пару значений через слеш: ')
#         bot.register_next_step_handler(call.message, my_currency)
#
#
# def my_currency(message):
#     try:
#         values = message.text.upper().split('/')
#         res = currency.convert(amount, values[0], values[1])
#         bot.send_message(message.chat.id, f'Получается: {res:.2f}. Можете заново написать сумму.')
#         bot.register_next_step_handler(message, summa)
#     except ValueError:
#         bot.send_message(message.chat.id, f'Что-то не так. Впишите значения заново: ')
#         bot.register_next_step_handler(message, my_currency)
#
#
#
# bot.polling(none_stop=True)


# import asyncio
# import logging
# from aiogram import Bot, Dispatcher, types
# from aiogram.filters import Command
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
#
# # Логирование — чтобы видеть ошибки в консоли
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
#
# TOKEN = "8327887897:AAFvap9nzXkFUgc46ao6Zgc5PZCpEHL09dw"
#
# bot = Bot(token=TOKEN)
# dp = Dispatcher()
#
#
# @dp.message(Command("start"))
# async def cmd_start(message: types.Message):
#     await message.reply("Привет! Бот работает 👋")
#
#
# @dp.message()
# async def any_message(message: types.Message):
#     markup = InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(text="Site 🌐", url="https://google.com")],
#         [InlineKeyboardButton(text="Hello 👋", callback_data="hello")]
#     ])
#     await message.reply("Выбери:", reply_markup=markup)
#
#
# @dp.callback_query(lambda c: c.data == "hello")
# async def cb_hello(callback: types.CallbackQuery):
#     # обязательно ответить на callback_query, чтобы убрать "крутилку" у кнопки
#     await callback.answer("Нажал!")
#     await callback.message.answer("Ты нажал кнопку Hello")
#
# @dp.message(Command("hello"))
# async def reply(message: types.Message):
#     markup = ReplyKeyboardMarkup(
#         keyboard=[
#             [KeyboardButton(text="Site")]
#         ],
#         one_time_keyboard=True,
#         resize_keyboard=True
#     )
#
#     await message.answer("Hello", reply_markup=markup)
#
#
#
# async def main():
#     try:
#         logger.info("Запуск polling...")
#         # старт поллинга с ботом
#         await dp.start_polling(bot)
#     except Exception:
#         logger.exception("Ошибка в polling")
#     finally:
#         # закрываем сессию aiohttp
#         await bot.session.close()
#         logger.info("Сессия бота закрыта")
#
#
# if __name__ == "__main__":
#     asyncio.run(main())

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo


TOKEN = "8327887897:AAFvap9nzXkFUgc46ao6Zgc5PZCpEHL09dw"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_command(message: types.Message):
    # Кнопка с web_app — параметр называется web_app, а не web_add/webApp и т.п.
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="Открыть веб-страницу",
                    web_app=WebAppInfo(url="https://choogix.github.io/index.html/")  # лучше https
                )
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await message.answer("Привет. Бот работает корректно ✅", reply_markup=kb)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())






