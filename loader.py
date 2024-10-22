import os
import logging

from aiogram.contrib.middlewares.logging import LoggingMiddleware
from middlewares.throttling import ThrottlingMiddleware

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import load_environment_variables
load_environment_variables()

BOT_API_TOKEN = os.getenv('BOT_API_TOKEN')
if not BOT_API_TOKEN:
    raise ValueError('BOT_API_TOKEN is not set')

bot = Bot(token=BOT_API_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

logging.basicConfig(level=logging.INFO)

dp.middleware.setup(LoggingMiddleware())
dp.middleware.setup(ThrottlingMiddleware())