import logging
from abc import ABC
from decouple import config
from telegram import Update
from telegram.ext import Updater

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)


class TelegramCore(ABC):
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            TelegramCore._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        logging.info('Ligando...')
        self._token = config('BOT_TOKEN')
        self._updater = Updater(self._token, use_context=True)
        self._running = False

    @classmethod
    def instance(cls):
        return cls._instance or cls()

    def run(self):
        """Start the bot as a python script loop"""
        self._updater.start_polling()

        logging.info('Rodando como um script python!')
        self._updater.idle()

    def is_run(self):
        """Start the bot as a python script loop"""
        if not self._running:
            self._updater.start_polling()

            logging.info('Rodando como um script python!')
            self._running = True
        else:
            logging.info('Bot já está ligado!')
