from dataclasses import dataclass
from aiogram import Bot

@dataclass
class Secrets:
    token: str = '8370174272:AAHL6vWAw_THx1jigEflITs2MoMWpGAbk1I'
    admin_id: int = 7892272095

bot = Bot(token = Secrets.token)