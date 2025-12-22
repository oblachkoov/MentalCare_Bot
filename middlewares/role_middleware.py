from aiogram import BaseMiddleware
from aiogram.dispatcher.event.bases import SkipHandler

from enums.role import RoleType


class RoleMiddleware(BaseMiddleware):
    def __init__(self, allowed_roles: list[RoleType]):
        self.allowed_roles = allowed_roles

    async def __call__(self, handler, event, data):
        user = data.get("user")

        if not user:
            return

        if user.role not in self.allowed_roles:
            raise SkipHandler()

        return await handler(event, data)