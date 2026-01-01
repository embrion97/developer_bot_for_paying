from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


start_kb = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Оплата услуг"),
            KeyboardButton(text="❗️Важно к прочтению❗️")
        ]
    ]
)

back_keyboard = [
    [KeyboardButton(text='Назад')]
]
back_kb = ReplyKeyboardMarkup(keyboard=back_keyboard, resize_keyboard=True, one_time_keyboard=True)

contact_keyboard = InlineKeyboardBuilder()
offer = InlineKeyboardButton(text="Оферта", callback_data='oferta')
contact_keyboard.row(offer)
bak = InlineKeyboardButton(text="Назад", callback_data='back')
contact_keyboard.row(bak)