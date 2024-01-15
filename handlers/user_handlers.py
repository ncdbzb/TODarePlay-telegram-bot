import os
from random import choice
from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart, StateFilter

from config_data.config import Config, load_config
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.keyboards import start_keyboard, about_keyboard, channel_keyboard, que_keyboard, further_keyboard
from database.database import Database
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from utils.choose_option import get_que_act


router = Router()
db = Database()
storage = MemoryStorage()
config: Config = load_config('.env')


class FSMGame(StatesGroup):
    in_game = State()


@router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    first_name = message.from_user.first_name
    user_id = message.from_user.id
    username = message.from_user.username

    if not db.user_exists(user_id):
        db.add_user(user_id, username)

    await message.answer(text=LEXICON_RU['/start'].format(first_name),
                         reply_markup=start_keyboard.as_markup(resize_keyboard=True))
    await state.clear()


@router.message(Command(commands='stop'), StateFilter(default_state))
async def process_stop_without_state(message: Message):
    await message.answer(text=LEXICON_RU['process_stop_without_state'])


@router.message(Command(commands='stop'), ~StateFilter(default_state))
async def process_stop(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_RU['process_stop'])
    await state.clear()


@router.callback_query(F.data == 'begin_button_pressed')
async def process_begin_button(callback: CallbackQuery, state: FSMContext, bot: Bot):
    user_channel_status = await bot.get_chat_member(config.channel.channel_id, callback.from_user.id)

    if user_channel_status.status == 'left':
        await callback.message.answer(text=LEXICON_RU['sub'],
                                      reply_markup=channel_keyboard.as_markup(resize_keyboard=True))
    else:
        await callback.message.answer(text=LEXICON_RU['question'],
                                      reply_markup=que_keyboard.as_markup(resize_keyboard=True))
        await state.set_state(FSMGame.in_game)

button_list = ['que.txt', 'que16.txt', 'act.txt', 'act16.txt', 'rnd']


@router.callback_query(F.data.in_(button_list), StateFilter(FSMGame.in_game))
async def process_truth_button(callback: CallbackQuery):
    name = choice(button_list[:-1]) if callback.data == 'rnd' else callback.data
    path = os.path.join('data', name)

    something = get_que_act(path)
    mode = LEXICON_RU[name]

    await callback.message.edit_text(text=f'{mode}\n\n{something}',
                                     reply_markup=further_keyboard.as_markup(resize_keyboard=True))


@router.callback_query(F.data == 'further', StateFilter(FSMGame.in_game))
async def process_truth_button(callback: CallbackQuery, bot: Bot):
    user_channel_status = await bot.get_chat_member(config.channel.channel_id, callback.from_user.id)

    if user_channel_status.status == 'left':
        await callback.message.answer(text=LEXICON_RU['sub1'],
                                      reply_markup=channel_keyboard.as_markup(resize_keyboard=True))
    else:
        await callback.message.answer(text=LEXICON_RU['question'],
                                      reply_markup=que_keyboard.as_markup(resize_keyboard=True))


@router.callback_query(F.data == 'about_button_pressed')
async def process_about_button(callback: CallbackQuery):
    await callback.message.answer(text=LEXICON_RU['about'],
                                  reply_markup=about_keyboard.as_markup(resize_keyboard=True))
