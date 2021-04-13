import logging

from telegram.ext import Filters, MessageHandler

logger = logging.getLogger(__name__)

def unknown(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Sorry, I didn't understand that command.",
    )

unknown_handler = MessageHandler(Filters.command, unknown)
