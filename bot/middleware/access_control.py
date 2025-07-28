# bot/middleware/access_control.py

from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Awaitable, Dict, Any

from bot.config import load_config

config = load_config()
ADMIN_ID = config.admin_id

# In-memory store of approved users
approved_users = set()

class AccessControlMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        user_id = event.from_user.id

        # Allow admin always
        if user_id == ADMIN_ID:
            return await handler(event, data)

        # Allow only if user has been approved
        if user_id in approved_users:
            return await handler(event, data)

        # Otherwise, block access
        await event.answer("⛔ You are not authorized to use this bot. Please wait for admin approval.")
        return
