import logging
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from text_translate import translator
from keyboards import *

from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters
    # Updater
)

Token = "6632245348:AAFMiDy9n3almjEJaXYoLu42ymAXzvV7AUs"
bot_username = "SafiaComplaints_Bot"
# global user_lang

# updater


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # obj = crud.get_user(db=session, user_id=update.message.from_user.id)
    # if obj:
    #     await update.message.reply_text(translation[context.user_data['language']]['request_order'],reply_markup=ReplyKeyboardMarkup(main_buttons,resize_keyboard=True))
    await update.message.reply_text(f"{translator['ru']['greeting']}\n\n{translator['uz']['greeting']}")
    await update.message.reply_text(f"{translator['ru']['choose_lang']}\n\n{translator['uz']['choose_lang']}",
                                    reply_markup=ReplyKeyboardMarkup(choose_lang, resize_keyboard=True))


async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    # if message_type == "group":
    #     print("This group chat")
    #     if bot_username in text:
    #         new_text: str = text.replace(bot_username, "").strip()
    #         response: str = handle_message(new_text)
    #     else:
    #         return
    # else:
    if text == "Русский" or text == "O'zbek":
        if text == "Русский":
            context.user_data['user_lang'] = "ru"
        elif text == "O'zbek":
            context.user_data['user_lang'] = "uz"
        # context.user_data['user_lang'] = lang
        await update.message.reply_text(f"{translator[context.user_data['user_lang']]['choose_sphere']}",
                                        reply_markup=await sphere_keyboards(user_lang=context.user_data['user_lang']))

    print("Bot: ", text)


if __name__ == "__main__":
    print("Starting bot ...")
    app = Application.builder().token(Token).build()

    # Commands
    app.add_handler(CommandHandler("start", start_command))
    # app.add_handler(CommandHandler("help", start_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_messages))

    # Polls the bot
    print("Polling ...")
    app.run_polling(poll_interval=3)
