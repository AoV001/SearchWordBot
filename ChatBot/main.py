import asyncio
from aiogram import Bot, Dispatcher
from aiogram.utils import executor

from app.handlers import router


async def main():
    bot = Bot(token='6621781130:AAFGIBRTBYDTwARzG2Y-oTSn2Dj1EX-6Lgg')
    dp = Dispatcher()

    dp.include_router(router)

    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.create_task(main())
        loop.run_forever()
    except KeyboardInterrupt:
        print('The Bot is off')
    finally:
        loop.close()
