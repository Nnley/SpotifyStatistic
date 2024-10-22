from aiogram import types
from aiogram import Dispatcher

from db.crud import UserManager
from handlers.user.auth import auth
from localization import get_text

async def start(message: types.Message):
    if message.get_args() and message.get_args() == 'success':
        return await message.answer(get_text(message.from_user.language_code, 'auth_success'))
    elif message.get_args() and message.get_args() == 'auth':
        return await auth(message)
    
    user_id = message.from_user.id
    user_language = message.from_user.language_code
    user = UserManager.get_or_create_user(user_id, user_language)
    
    if user.refresh_token is None:
        await message.answer(get_text(user.language_code, 'none_auth_start'))
    else: 
        await message.answer(get_text(user.language_code, 'auth_start')) 


def register_start(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"], state="*")