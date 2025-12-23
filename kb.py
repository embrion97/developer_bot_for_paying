from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

start_keyboard = [
    [KeyboardButton(text='Оплата услуг')],
    [KeyboardButton(text='Важно к прочтению')]
]
start_kb = ReplyKeyboardMarkup(keyboard=start_keyboard, resize_keyboard=True, one_time_keyboard=True)

back_keyboard = [
    [KeyboardButton(text='Назад')]
]
back_kb = ReplyKeyboardMarkup(keyboard=start_keyboard, resize_keyboard=True, one_time_keyboard=True)