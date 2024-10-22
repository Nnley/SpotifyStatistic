from aiogram import types
from aiogram import Dispatcher

from db.crud import UserManager
from handlers.user.auth import auth
from localization import get_text

async def stats(message: types.Message):   
    user_id = message.from_user.id
    user_language = message.from_user.language_code
    user = UserManager.get_or_create_user(user_id, user_language)
    
    await message.answer(get_text(user.language_code, 'stats')) 


def register_stats(dp: Dispatcher):
    dp.register_message_handler(stats, commands=["stats"], state="*")