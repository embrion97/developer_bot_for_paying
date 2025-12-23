import asyncio
import sqlite3
from aiogram import Dispatcher
import logging
from botlogic.settings import bot
from botlogic.handlers.events import start_bot, stop_bot





async def start():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    )
    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()






if __name__ == "__main__":
    asyncio.run(start())
