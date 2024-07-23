import asyncio
from aiogram import Bot, Dispatcher


import logging
import sys


# Запуск бота
async def main():
    bot = Bot(token=" YOUR TOKEN")
    dp = Dispatcher()

    # dp.include_routers()  # Импорты роутеров из hendlers

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
