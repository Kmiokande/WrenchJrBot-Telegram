import logging

from decouple import config
from telegram.ext import CommandHandler, Updater

from commands.start import start

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

token = config('BOT_TOKEN')
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
