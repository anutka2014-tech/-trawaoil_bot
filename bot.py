"""
TRAWA Telegram Bot · bot.py
Точка входа: инициализация бота и запуск polling.
"""

import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

from handlers import router

# Настройка логов — видно что происходит в терминале
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)s  %(name)s — %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


async def main() -> None:
    load_dotenv()

    token = os.getenv("BOT_TOKEN")
    if not token:
        logger.error("BOT_TOKEN не найден в .env — бот не запустится")
        return

    bot = Bot(token=token)
    dp  = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)

    logger.info("TRAWA Bot запущен 🌿")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
