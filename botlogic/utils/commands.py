from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Начало работы'
        ),
        BotCommand(
            command='get_file',
            description='Получить материалы'
        ),
        BotCommand(
            command='about',
            description='Информация о боте'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())