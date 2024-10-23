from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from localization import get_text

def change_language_reply_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1)
    
    set_english_button = InlineKeyboardButton(text=get_text('en', 'change_language_button_text'), callback_data="language-english") # type: ignore
    set_russian_button = InlineKeyboardButton(text=get_text('ru', 'change_language_button_text'), callback_data="language-russian") # type: ignore
    set_latvian_button = InlineKeyboardButton(text=get_text('lv', 'change_language_button_text'), callback_data="language-latvian") # type: ignore
    
    keyboard.add(set_english_button, set_russian_button, set_latvian_button)
    
    return keyboard

def auth_reply_keyboard(auth_link: str, language_code: str):
    keyboard = InlineKeyboardMarkup()
    
    auth_button = InlineKeyboardButton(text=get_text(language_code, 'auth_button_text'), url=auth_link) # type: ignore
    
    keyboard.add(auth_button)
    
    return keyboard