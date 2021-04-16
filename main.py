import logging

from decouple import config
from telegram.ext import Updater

from commands.about.command import about_handler
from commands.ban.command import ban_handler
from commands.crypto.callbacks import crypto_callback
from commands.crypto.command import crypto_handler
from commands.getid.command import getid_handler
from commands.rules.command import rules_handler
from commands.start.command import start_handler
from commands.unknown.command import unknown_handler
from commands.welcome.callbacks import rules_callback
from commands.welcome.command import welcome_handler
from utils.utils import error_handler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)

def main():
    TOKEN = config("BOT_TOKEN")
    MODE = config("MODE", default="cmd")
    NAME = config("SERVER_NAME")
    PORT = config("PORT", default=8443, cast=int)

    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    #  Associate commands with action.
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(about_handler)
    dispatcher.add_handler(crypto_handler)
    dispatcher.add_handler(getid_handler)
    dispatcher.add_handler(rules_handler)
    dispatcher.add_handler(welcome_handler)
    dispatcher.add_handler(ban_handler)

    # Add callback handlers
    dispatcher.add_handler(crypto_callback)
    dispatcher.add_handler(rules_callback)

    # Add error handler
    dispatcher.add_handler(unknown_handler)
    dispatcher.add_error_handler(error_handler)

    if MODE == "cmd":
        updater.start_polling()
        logging.info("Bot is running as a python script.")
    elif MODE == "web":
        updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=TOKEN)
        updater.bot.setWebhook(f"https://{NAME}.herokuapp.com/{TOKEN}")
        logging.info("Bot is running like a webhook.")
    else:
        raise Exception("The past mode was not recognized!")

    logger.info(f"Listening humans as {updater.bot.username}...")
    updater.idle()
    logger.info("Bot stopped gracefully")

if __name__ == "__main__":
    main()
