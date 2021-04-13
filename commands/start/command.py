import logging

from telegram.ext import CommandHandler

logger = logging.getLogger(__name__)

def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm Wrench Jr."
    )

start_handler = CommandHandler("start", start)
