# bot/middleware/locale.py

from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Dict, Any, Awaitable

class LanguageMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        lang = "en"
        if event.from_user.language_code == "hi":
            lang = "hi"
        data["lang"] = lang
        return await handler(event, data)
