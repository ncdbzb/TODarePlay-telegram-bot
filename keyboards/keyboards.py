from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lexicon.lexicon_ru import LEXICON_RU, URLS


buttons = [InlineKeyboardButton(text=LEXICON_RU['begin_button'], callback_data='begin_button_pressed'),
           InlineKeyboardButton(text=LEXICON_RU['about_button'], callback_data='about_button_pressed')]

start_keyboard = InlineKeyboardBuilder()
start_keyboard.row(*buttons, width=2)

about_keyboard = InlineKeyboardBuilder()
about_keyboard.row(buttons[0], width=1)

channel_button = InlineKeyboardButton(text=LEXICON_RU['t_or_d'], url=URLS['channel'])

channel_keyboard = InlineKeyboardBuilder()
channel_keyboard.row(channel_button, buttons[0], width=2)

buttons1 = [InlineKeyboardButton(text=LEXICON_RU['que.txt'], callback_data='que.txt'),
            InlineKeyboardButton(text=LEXICON_RU['act.txt'], callback_data='act.txt'),
            InlineKeyboardButton(text=LEXICON_RU['que16.txt'], callback_data='que16.txt'),
            InlineKeyboardButton(text=LEXICON_RU['act16.txt'], callback_data='act16.txt'),
            InlineKeyboardButton(text=LEXICON_RU['random'], callback_data='rnd')]

que_keyboard = InlineKeyboardBuilder()
que_keyboard.row(*buttons1, width=2)

further_button = InlineKeyboardButton(text=LEXICON_RU['further'], callback_data='further')

further_keyboard = InlineKeyboardBuilder()
further_keyboard.row(further_button, width=1)
