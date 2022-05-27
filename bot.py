try:
    import settings
except ImportError:
    exit('DO cp settings.py.default settings.py and set token!')

import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types
from kino import get_random_film

# Config logging
logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.TOKEN)
dp = Dispatcher(bot)

def bot_run(dispatcher, skip_updates=True):
    executor.start_polling(dp, skip_updates=skip_updates)

@dp.message_handler(commands=['start'])
async def send_welcom(message: types.Message):
    await message.reply("Привет!\nЯ могу скинуть рандомный фильм, напиши команду /film.")

@dp.message_handler(commands=['film'])
async def send_random_film(message: types.Message):
    film = get_random_film()

    await asyncio.sleep(1)
    await types.ChatActions.upload_photo()
    media = types.MediaGroup()
    media.attach_photo(film.poster_url)
    await message.answer_media_group(media=media)
    await message.answer(film.output_film(), parse_mode=types.ParseMode.HTML)

if __name__ == "__main__":
    bot_run(dispatcher=dp)