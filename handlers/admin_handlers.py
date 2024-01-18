from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU
from filters.admin_filter import IsAdmin
from database.database import Database

db = Database()
router = Router()


@router.message(F.text.startswith('/sendall'), IsAdmin())
async def process_sendall_command(message: Message, bot: Bot):
    sendall_message = message.text[9:]
    for user_id in db.get_all_ids():
        await bot.send_message(user_id, text=sendall_message)
