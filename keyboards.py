from telegram import KeyboardButton, ReplyKeyboardMarkup
from text_translate import translator
# from bot import user_lang

choose_lang = [[KeyboardButton(text=translator['ru']['lang']), KeyboardButton(text=translator['uz']['lang'])]]


async def sphere_keyboards(user_lang):
    sphere_keyboard = [[KeyboardButton(text=translator[user_lang]['spheres'][0]), KeyboardButton(text=translator[user_lang]['spheres'][1])]]
    markup = ReplyKeyboardMarkup(keyboard=sphere_keyboard, resize_keyboard=True)
    return markup
