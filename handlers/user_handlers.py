from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.keyboards import keyboard

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=keyboard.as_markup(resize_keyboard=True))


@router.callback_query(F.data == 'big_button_1_pressed')
async def process_button_2_press(callback: CallbackQuery):
    await callback.answer(text='Нажата кнопка')
