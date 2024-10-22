import os

from aiogram import Dispatcher
from aiogram import types

from db.crud import UserManager
from localization import get_text
from keyboards.reply import auth_reply_keyboard

from config import load_environment_variables
load_environment_variables()

async def auth(message: types.Message):
    user_id = message.from_user.id
    user_language = message.from_user.language_code
    user = UserManager.get_or_create_user(user_id, user_language)
    
    if user.refresh_token is None:
        auth_link = f'{os.getenv("SPOTIFY_AUTH_URL")}/{user_id}'
        
        await message.answer(get_text(user.language_code, 'auth_button_description'), reply_markup=auth_reply_keyboard(auth_link))
    else:
        await message.answer(get_text(user.language_code, 'already_authorized'))

def register_auth(dp: Dispatcher):
    dp.register_message_handler(auth, commands=["auth"], state="*")