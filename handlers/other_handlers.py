from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU


router = Router()


@router.message()
async def error_message(message: Message):
    await message.reply(text=LEXICON_RU['no_echo'])
