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
    if user.refresh_token is None:
        await message.answer('Привет! Чтобы получить статистику, Вам необходимо авторизоваться через Spotify.')
    else: 
        await message.answer('Список команд можно увидеть, написав /help.')      

  
@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply("Доступные команды: /stats, /auth")


@dp.message_handler(commands=['auth'])
async def auth(message: types.Message):
    pass


@dp.inline_handler()
async def inline_handler(query: types.InlineQuery):
    user_id = query.from_user.id
    user = get_or_create_user(user_id)
    if user.refresh_token is None:
        results = []
        results.append(
            types.InlineQueryResultArticle(
                id='1',
                title='Моя статистика',
                description='Чтобы получить статистику, Вам необходимо авторизоваться в боте через Spotify.',
                input_message_content=types.InputTextMessageContent(
                    message_text='Чтобы получить статистику, Вам необходимо авторизоваться в боте через Spotify.',                  
                ),
                reply_markup=types.InlineKeyboardMarkup().add(
                    types.InlineKeyboardButton(
                        text='Авторизоваться',
                        callback_data='auth',
                    ) # type: ignore
                )
            )
        )
        await query.answer(results, cache_time=1, is_personal=True)
    else:
        results = []
        results.append(
            types.InlineQueryResultArticle(
                id='1',
                title='Моя статистика',
                description='Посмотреть топ моих самых прослушиваемых треков',
                input_message_content=types.InputTextMessageContent(
                    message_text=''
                ),
            )
        )
        await query.answer(results, cache_time=1, is_personal=True)


if __name__ == '__main__':
    from aiogram import executor
    from services import spotify_auth
    
    spotify_auth.main()
    # executor.start_polling(dp, skip_updates=True)