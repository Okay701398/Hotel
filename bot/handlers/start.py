from aiogram import Router, types
from aiogram.filters import CommandStart
from bot.keyboards.menu import main_menu_kb
from bot.translations import get_text

router = Router()

@router.message(CommandStart())
async def start_handler(message: types.Message):
    user_lang = message.from_user.language_code or "en"
    text = get_text("welcome", user_lang)
    await message.answer(text, reply_markup=main_menu_kb(user_lang))
