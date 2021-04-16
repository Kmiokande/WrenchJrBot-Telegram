import logging

from telegram.ext import CommandHandler

from utils.utils import get_admin_ids

logger = logging.getLogger(__name__)

def ban(update, context):
    chat_type = update.message.chat.type
    chat_id = update.message.chat_id

    if chat_type == "group":
        admins = get_admin_ids(context, chat_id)
        if update.message.from_user.id in admins:
            update.message.reply_text("Quer banir quem?")
        else:
            update.message.reply_text("Tu não é admin!")
    elif chat_type == "private":
        update.message.reply_text("Não pode usar esse comando no privado!")

ban_handler = CommandHandler("ban", ban)
