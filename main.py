import random
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from conf import token, dzen
from parse_book import find_books

bot = Bot(token=token)  # bot initialization.
dp = Dispatcher(bot)  # dispatcher initialization

logging.basicConfig(filename='log.txt', level=logging.INFO)  # create logging

info_menu = ReplyKeyboardMarkup(resize_keyboard=True)  # create the keyboard for choice action
lit_button = KeyboardButton('Useful literature')  # create button
info_button = KeyboardButton('Information')  # create button
info_menu.add(info_button, lit_button)  # add buttons to the keyboard

change_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)  # create the keyboard for change book
change_button = KeyboardButton('Already read this')  # create button
change_keyboard.add(change_button)  # add buttons to the keyboard


@dp.message_handler(commands='start')
async def start_contact(message: types.Message):
    """function to process the start command"""
    await message.answer('Привет. Зачем пришел? Тебе нужна информация или просто ищешь литературу?',
                         reply_markup=info_menu)  # greeting


@dp.message_handler(content_types=['text'])
async def get_info(message: types.Message):
    """
    The function handles user's choice. Instructs telegram bot to send information or suggest a book for study.
    """
    if message.text == 'Information':
        await message.answer(f'Вот основы:\n{dzen}')
    elif message.text == 'Useful literature':
        await message.answer('Да. Тебе еще много нужно узнать. Сейчас подберу что-нибудь', reply_markup=change_keyboard)
        books = find_books()
        choice = random.choice(list(books.keys()))
        await message.answer(f'Попробуем эту? {choice} - {books[choice]}')
    elif message.text == 'Already read this':
        await message.answer('Ладно. Как на счет этой книги?', reply_markup=change_keyboard)
        books = find_books()
        choice = random.choice(list(books.keys()))
        await message.answer(f'Попробуем эту? {choice} - {books[choice]}')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
