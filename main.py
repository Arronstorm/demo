import os
from telegram.ext import *

def start(update, context):
    update.message.reply_text("Hi How are you?")

def say(update, context):
    if len(context.args) > 0:
        saysomething = context.args[0]
        update.message.reply_text("you have said "+ saysomething )
    else:
        update.message.reply_text("Error" )

if __name__ == '__main__':

    PORT = os.environ.get('PORT')
    API_KEY = os.getenv('API_KEY')
    HEROKU_LINK = os.getenv('HEROKU_LINK')

    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("say", say))


    updater.start_webhook(listen="0.0.0.0",port=int(PORT),url="API_KEY", webhook_url=HEROKU_LINK + API_KEY)
    # updater.start_polling(1)
    updater.idle()
