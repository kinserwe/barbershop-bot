import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from app.bot.handlers.admin import router as admin_router
from app.bot.handlers.client import router as client_router
from app.config import settings


async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=settings.bot_token)
    dp = Dispatcher(storage=RedisStorage.from_url(settings.redis_url))

    dp.include_router(client_router)
    dp.include_router(admin_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
