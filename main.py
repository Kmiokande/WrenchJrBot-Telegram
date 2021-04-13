import logging

from decouple import config
from telegram.ext import Updater

from commands.about.command import about_handler
from commands.rules.command import rules_handler
from commands.start.command import start_handler
from commands.unknown.command import unknown_handler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

def main():
    token = config('BOT_TOKEN')
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    #  Associate commands with action.
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(about_handler)
    dispatcher.add_handler(rules_handler)

    dispatcher.add_handler(unknown_handler)

    updater.start_polling()
    logger.info('Listening humans as %s..' % updater.bot.username)
    updater.idle()
    logger.info('Bot stopped gracefully')

if __name__ == '__main__':
    main()
