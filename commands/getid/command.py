import logging

from telegram import ParseMode
from telegram.ext import CommandHandler

logger = logging.getLogger(__name__)

def getid(update, context):
    user_id = update.message.from_user.id

    TEXT = (
        f"🆔 Your ID\n"
        f"{user_id}"
    )

    context.bot.sendMessage(
        chat_id=user_id,
        text=TEXT
    )

getid_handler = CommandHandler("getid", getid)