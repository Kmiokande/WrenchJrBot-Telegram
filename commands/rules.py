import logging
from telegram.ext import CommandHandler
from core import TelegramCore
from messages import RULES


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)


def rules(update, context):
    update.message.reply_text(RULES)


def config_handlers(instance: TelegramCore):
    instance.add_handler(CommandHandler('rules', rules))
