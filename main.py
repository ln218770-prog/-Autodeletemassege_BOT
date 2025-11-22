import os
from telegram.ext import Updater, MessageHandler, Filters

TOKEN = os.getenv("BOT_TOKEN")  # Render/GitHub ke ENV se token aayega

def delete_message(update, context):
    try:
        context.bot.delete_message(
            chat_id=update.message.chat_id,
            message_id=update.message.message_id
        )
    except:
        pass

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(MessageHandler(Filters.text | Filters.photo | Filters.video | Filters.document, delete_message))

updater.start_polling()
updater.idle()
