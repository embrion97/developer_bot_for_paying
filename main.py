import asyncio
import sqlite3
from aiogram import Dispatcher, F
from aiogram.filters import Command
import logging
from botlogic.settings import bot
from botlogic.handlers.events import start_bot, stop_bot
from botlogic.utils.statesform import SendFileSteps
from botlogic.handlers.get_menu import start_menu, next_menu, contact_menu, send_fail



async def start():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    )
    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(start_menu, Command(commands='start'))
    dp.message.register(next_menu, F.text == "Оплата услуг", SendFileSteps.mainmenu)
    dp.message.register(contact_menu, F.text == "❗️Важно к прочтению❗", SendFileSteps.mainmenu)
    dp.callback_query.register(send_fail, F.data == "oferta", SendFileSteps.contactmenu)
    dp.callback_query.register(start_menu, F.data == 'back', SendFileSteps.contactmenu)
    dp.message.register(start_menu, F.text == 'Назад', SendFileSteps.offer)
    dp.message.register(start_menu, F.text == 'Назад', SendFileSteps.pays)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()






if __name__ == "__main__":
    asyncio.run(start())
