from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import TOKEN
from midlewares.auth import AuthMiddleware
from midlewares.logging import LogingMidleware

from routers.psychologist import router as psychologist_router
from routers.client import router as client_router
from routers.start import router as start_router
from routers.admin import router as admin_router


properties = DefaultBotProperties(
    parse_mode=ParseMode.HTML,
)

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.update.middleware(LogingMidleware())
dp.update.middleware(AuthMiddleware())


dp.include_router(start_router)

dp.include_router(psychologist_router)
dp.include_router(client_router)
dp.include_router(admin_router)


