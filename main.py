import logging

from decouple import config
from telegram.ext import Updater

from commands.about.command import about_handler
from commands.crypto.command import crypto_handler
from commands.rules.command import rules_handler
from commands.start.command import start_handler
from commands.unknown.command import unknown_handler
from commands.welcome.callbacks import rules_callback
from commands.welcome.command import welcome_handler
from utils.utils import error_handler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

def main():
    token = config('BOT_TOKEN')
    mode = config('MODE', default='cmd')
    name = config('SERVER_NAME')
    port = config('PORT', default=8443, cast=int)
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    #  Associate commands with action.
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(about_handler)
    dispatcher.add_handler(crypto_handler)
    dispatcher.add_handler(rules_callback)
    dispatcher.add_handler(rules_handler)
    dispatcher.add_handler(welcome_handler)

    dispatcher.add_handler(unknown_handler)

    dispatcher.add_error_handler(error_handler)

    if mode == "cmd":
        updater.start_polling()
    elif mode == "web":
        updater.start_webhook(listen="0.0.0.0",
                          port=int(port),
                          url_path=token)
        updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(name, token))
    else:
        raise Exception("O modo passado não foi reconhecido")

    logger.info('Listening humans as %s..' % updater.bot.username)
    updater.idle()
    logger.info('Bot stopped gracefully')

if __name__ == '__main__':
    main()
