import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import user_handlers, other_handlers, admin_handlers
from keyboards.set_main_menu import set_main_menu


async def main() -> None:
    logging.basicConfig(level=logging.INFO)

    config: Config = load_config('.env')

    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher()

    await set_main_menu(bot)

    dp.include_routers(user_handlers.router, admin_handlers.router, other_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
