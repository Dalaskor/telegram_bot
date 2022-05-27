try:
    import settings
except ImportError:
    exit('DO cp settings.py.default settings.py and set token!')

import logging
from aiogram import Bot, Dispatcher, executor, types

# Config logging
logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.TOKEN)
dp = Dispatcher(bot)

def bot_run(dispatcher, skip_update=True):
    executor.start_polling(dp, skip_updates=skip_update)

if __name__ == "__main__":
    bot_run(dispatcher=dp)