# bot/keyboards/menu.py

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu(lang: str = "en") -> ReplyKeyboardMarkup:
    if lang == "hi":
        buttons = [
            ["🛏️ कमरा बुक करें", "📖 मेरी बुकिंग"],
            ["🎁 ऑफ़र", "ℹ️ हमारे बारे में"],
            ["📞 सहायता", "🌐 भाषा बदलें"]
        ]
    else:
        buttons = [
            ["🛏️ Book a Room", "📖 View Bookings"],
            ["🎁 Offers", "ℹ️ About Us"],
            ["📞 Support", "🌐 Change Language"]
        ]
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=b) for b in row] for row in buttons], resize_keyboard=True)
