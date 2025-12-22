from aiogram import BaseMiddleware

class AnonymousMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler,
            event,
            data
    ):
        user = data.get("user")
        if not user:
            return await handler(event, data)
        if user.role == "student" and not user.is_confirmed:
            data["display_name"] = "Anonym client"
        else:
            data["display_name"] = user.full_name

        return await handler(event, data)
