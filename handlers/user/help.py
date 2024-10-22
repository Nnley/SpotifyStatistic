from aiogram import types
from aiogram import Dispatcher

from db.crud import UserManager
from localization import get_text

async def help(message: types.Message):
    user_id = message.from_user.id
    user_language = message.from_user.language_code
    user = UserManager.get_or_create_user(user_id, user_language)
    
    await message.reply(get_text(user.language_code, 'help'))
    
def register_help(dp: Dispatcher):
    dp.register_message_handler(help, commands=["help"], state="*")