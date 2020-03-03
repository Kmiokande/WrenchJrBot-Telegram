import logging
from telegram.ext import CommandHandler
from core import TelegramCore

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    """Send a message when the command /start is issued."""
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm Wrench Jr.")


def config_handlers(instance: TelegramCore):
    instance.add_handler(CommandHandler('start', start))
