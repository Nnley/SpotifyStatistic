from aiogram import Dispatcher
from aiogram import types

from db.crud import UserManager
from localization import get_text

from config import load_environment_variables
load_environment_variables()

async def github(message: types.Message):
    user_id = message.from_user.id
    user_language = message.from_user.language_code
    user = UserManager.get_or_create_user(user_id, user_language)
    
    await message.answer(get_text(user.language_code, 'github'))

def register_github(dp: Dispatcher):
    dp.register_message_handler(github, commands=["github"], state="*")