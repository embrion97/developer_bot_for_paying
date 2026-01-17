from botlogic.settings import bot, Secrets
from botlogic.views import start_bot_msg, stop_bot_msg
from botlogic.utils.commands import set_commands


async def start_bot():
    await set_commands(bot)
#    await bot.send_message(Secrets.admin_id, start_bot_msg())


async def stop_bot():
    await bot.send_message(Secrets.admin_id, stop_bot_msg())
