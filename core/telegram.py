import logging
from abc import ABC, abstractmethod

from decouple import config
from telegram import Update
from telegram.ext import Handler, Updater

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)


class TelegramCore:
    def __init__(self):
        logging.info("Iniciando...")
        self.token = config("BOT_TOKEN")
        self.port = config("PORT", default=8443, cast=int)
        self.server_url = config("SERVER_URL")
        self._updater = Updater(self.token)
        self._runing = False

    def add_handler(self, handler: Handler):
        if not isinstance(handler, Handler):
            raise ValueError("O handler deve ser do tipo Handler!")
        self._updater.dispatcher.add_handler(handler)

    def run_web(self):
        """Start the bot as a webhook server"""
        self._updater.start_webhook(
            listen="0.0.0.0", port=self.port, url_path=self.token
        )
        self._updater.bot.set_webhook(f"https://{self.server_url}/{self.token}")
        logging.info("O bot está rodando como um webserver!")
        self._updater.idle()

    def run_cmd(self):
        """Start the bot as a python script loop"""
        self._updater.start_polling()
        logging.info("O Bot está rodando como um script python!")
        self._updater.idle()

    def is_run(self):
        """Start the bot as a python script loop"""
        if not self._runing:
            self._updater.start_polling()
            logging.info("O Bot está rodando como um script python!")
            self._runing = True
        else:
            logging.info("O Bot já está rodando...")


#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             TelegramCore._instance = super().__new__(cls)
#         return cls._instance

#     @classmethod
#     def instance(cls):
#         return cls._instance or cls()

#     @abstractmethod
#     def config_handlers(self):
#         raise NotImplementedError(
#             'Cannot call config_handler from BotTelegramCore'
#         )
