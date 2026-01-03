import asyncio
from aiogram import Dispatcher, F
from aiogram.filters import Command
import logging
from botlogic.settings import bot
from botlogic.handlers.events import start_bot, stop_bot
from botlogic.utils.statesform import SendFileSteps
from botlogic.handlers.get_menu import start_menu, next_menu, contact_menu, send_fail, start_menu_inline
from aiogram.fsm.storage.memory import MemoryStorage



async def start():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    )
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(start_menu, Command(commands='start'))
    dp.message.register(next_menu, F.text == "Оплата услуг", SendFileSteps.mainmenu)
    dp.message.register(contact_menu, F.text == "❗️Важно к прочтению❗️", SendFileSteps.mainmenu)
    dp.callback_query.register(send_fail, F.data == "oferta", SendFileSteps.contactmenu)
    dp.callback_query.register(start_menu_inline, F.data == 'back', SendFileSteps.contactmenu)
    dp.message.register(start_menu, F.text == 'Назад')
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()



if __name__ == "__main__":
    asyncio.run(start())
