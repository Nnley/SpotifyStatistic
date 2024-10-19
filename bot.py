import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from db.crud import get_or_create_user

from config import load_environment_variables
load_environment_variables()

BOT_API_TOKEN = os.getenv('BOT_API_TOKEN')
if not BOT_API_TOKEN:
    raise ValueError('BOT_API_TOKEN is not set')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    user = get_or_create_user(user_id)
    await message.answer(str(user.id))

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)