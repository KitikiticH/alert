import asyncio
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers.routes import router, start
from aiogram.fsm.storage.memory import MemoryStorage
from logs import log

load_dotenv()
token = os.getenv("TOKEN")

bot = Bot(token)
storage = MemoryStorage()
dp = Dispatcher()
dp.include_router(router)

async def main():
    log.start()
    await start()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())