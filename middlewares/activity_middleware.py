from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from config import async_session
from services.user import UserService

class LastActivityMiddlewere(BaseMiddleware):
    async def __call__(self, handler, event: TelegramObject, data: dict):
        user_tg_id = getattr(event, "from_user", None)
        if user_tg_id:
            async with async_session() as session:
                user_service = UserService(session)
                await user_service.update_last_activity(user_tg_id)
        return await handler(event, data)