from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import TOKEN
from enums.role import RoleType

# from middlewares.role_middleware import RoleMiddleware
# from middlewares.ban_middleware import BanMiddleware
# from middlewares.anonymous_middleware import AnonymousMiddleware
# from middlewares.activity_middleware import LastActivityMiddlewere
# from middlewares.logging_middleware import LoggingMiddleware


from routers.psychologist import router as psychologist_router
from routers.client import router as client_router




properties = DefaultBotProperties(
    parse_mode=ParseMode.HTML,
)

bot = Bot(token=TOKEN)
dp = Dispatcher()

# from middlewares.auth import AuthMiddleware
# from middlewares.logging import LogingMidleware

# dp.update.middleware(LoggingMiddleware())
# dp.update.middleware(
#     RoleMiddleware([RoleType.client, RoleType.admin, RoleType.psychologist, RoleType.administrator])
# )
# dp.update.middleware(AnonymousMiddleware())
# dp.update.middleware(BanMiddleware())
# dp.update.middleware(LastActivityMiddlewere())

# dp.update.middleware(LogingMidleware())
# dp.update.middleware(AuthMiddleware())


dp.include_router(psychologist_router)
dp.include_router(client_router)


