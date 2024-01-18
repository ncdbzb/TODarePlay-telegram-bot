from aiogram.filters import BaseFilter
from aiogram.types import Message
from config_data.config import load_config, Config


class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[int] = None) -> None:

        config: Config = load_config('.env')

        if admin_ids is None:
            admin_ids = config.tg_bot.admin_ids
        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids
