# bot/keyboards/inline.py

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

def get_language_keyboard() -> InlineKeyboardBuilder:
    kb = InlineKeyboardBuilder()
    kb.row(
        InlineKeyboardButton(text="English 🇬🇧", callback_data="lang_en"),
        InlineKeyboardButton(text="हिंदी 🇮🇳", callback_data="lang_hi")
    )
    return kb
