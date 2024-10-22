from aiogram import types
from aiogram import Dispatcher

from loader import bot 
from db.crud import UserManager, UserRepository
from localization import get_text
from keyboards.reply import change_language_reply_keyboard

async def change_language(message: types.Message):
    user_id = message.from_user.id
    user_language = message.from_user.language_code
    user = UserManager.get_or_create_user(user_id, user_language)
    
    await message.reply(get_text(user.language_code, 'change_language_buttons_description'), reply_markup=change_language_reply_keyboard())

async def process_language_change(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    
    user_id = callback_query.from_user.id
    user = UserManager.get_or_create_user(user_id)
    
    if callback_query.data == 'language-english':
        user.language_code = 'en'
        UserRepository.update_user(user)
        
        await bot.send_message(callback_query.from_user.id, "You selected English language")
    elif callback_query.data == 'language-russian':
        user.language_code = 'ru'
        UserRepository.update_user(user)
        
        await bot.send_message(callback_query.from_user.id, "Вы выбрали русский язык")
    elif callback_query.data == 'language-latvian':
        user.language_code = 'lv'
        UserRepository.update_user(user)
        
        await bot.send_message(callback_query.from_user.id, "Jūs esat izvēlējies latviešu valodu")
    
def register_change_language(dp: Dispatcher):
    dp.register_message_handler(change_language, commands=["change_language"], state="*")
    dp.register_callback_query_handler(process_language_change, lambda c: c.data.startswith('language-'))
