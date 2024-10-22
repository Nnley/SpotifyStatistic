import os

from aiogram import Dispatcher
from aiogram import types

from loader import bot 
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
    
async def auth_callback(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    
    user_id = callback_query.from_user.id
    user_language = callback_query.from_user.language_code
    user = UserManager.get_or_create_user(user_id, user_language)
    
    await bot.send_message(user_id, get_text(user.language_code, 'none_auth_start'))

def register_auth(dp: Dispatcher):
    dp.register_message_handler(auth, commands=["auth"], state="*")
    dp.register_callback_query_handler(auth_callback, lambda c: c.data == 'auth-callback')