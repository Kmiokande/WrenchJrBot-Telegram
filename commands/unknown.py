import logging

from telegram.ext import Filters, MessageHandler

from core import TelegramCore

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

def unknown(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Sorry, I didn't understand that command.",
    )

def config_handlers(instance: TelegramCore):
    instance.add_handler(MessageHandler(Filters.command, unknown))
