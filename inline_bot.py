import asyncio

from aiogram import Bot, Dispatcher
from config import TOKEN_BOT_WITH_KEYBOARD
from handlers import router

bot = Bot(TOKEN_BOT_WITH_KEYBOARD)
disp = Dispatcher()


async def main():
    disp.include_router(router)
    await disp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())
