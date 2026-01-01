import os
from dataclasses import dataclass
from aiogram import Bot
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Secrets:
    token: str = os.environ.get("TOKEN")
    admin_id: int = int(os.environ.get("ADMIN_ID"))

bot = Bot(token = Secrets.token)