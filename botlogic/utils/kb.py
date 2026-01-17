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

inline_back = InlineKeyboardBuilder()
inline_back.button(
        text="Назад",
        callback_data="back"
    )
inline_back.adjust(1)

contact_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Контакты"),
            KeyboardButton(text="Условия возврата"),
            KeyboardButton(text="Оферта")
        ],[
            KeyboardButton(text="В главное меню")
        ]
    ]
)