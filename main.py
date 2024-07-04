from aiogram import Bot, Dispatcher
import asyncio
from core.settings import get_settings
import logging

from core.handlers.basic import basicrouter
from core.handlers.searchmusic import searchrouter

async def start():
    logging.basicConfig(level=logging.INFO)
    settings = get_settings('.env.example')
    bot = Bot(token=settings.bots.token)
    dp = Dispatcher()

    dp.include_router(basicrouter)
    dp.include_router(searchrouter)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())