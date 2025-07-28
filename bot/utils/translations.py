# bot/utils/translations.py

translations = {
    "en": {
        "welcome": "🏨 Welcome to *Yash Palace Hotel Booking Bot*!",
        "menu": "📋 Main Menu",
        "booking": "🛏️ Book a Room",
        "view_bookings": "📖 View My Bookings",
        "offers": "🎁 Offers",
        "about": "ℹ️ About Us",
        "support": "📞 Contact Support",
        "send_payment_proof": "📤 Please send your payment proof.",
        "booking_confirmed": "✅ Your booking has been *confirmed*!",
        "waiting_approval": "⏳ Waiting for admin approval...",
    },
    "hi": {
        "welcome": "🏨 *यश पैलेस होटल बुकिंग बॉट* में आपका स्वागत है!",
        "menu": "📋 मुख्य मेनू",
        "booking": "🛏️ कमरा बुक करें",
        "view_bookings": "📖 मेरी बुकिंग देखें",
        "offers": "🎁 ऑफ़र",
        "about": "ℹ️ हमारे बारे में",
        "support": "📞 सहायता से संपर्क करें",
        "send_payment_proof": "📤 कृपया अपना भुगतान प्रमाण भेजें।",
        "booking_confirmed": "✅ आपकी बुकिंग *पुष्ट* हो गई है!",
        "waiting_approval": "⏳ व्यवस्थापक की स्वीकृति की प्रतीक्षा कर रहे हैं...",
    }
}


def t(lang: str, key: str) -> str:
    return translations.get(lang, translations["en"]).get(key, key)
