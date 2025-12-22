from aiogram import BaseMiddleware
from aiogram.dispatcher.event.bases import SkipHandler

class BanMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler,
            event,
            data
    ):
        user = data.get("user")
        if user and user.is_banned:
            await event.answer("You are banned.")
            raise SkipHandler()

        return await handler(event, data)
