import logging

from telegram.ext import CommandHandler

# from utils.utils import is_admin

logger = logging.getLogger(__name__)

def get_admin_ids(bot, chat_id):
    """Returns a list of admin IDs for a given chat. Results are cached for 1 hour."""
    return [admin.user.id for admin in bot.get_chat_administrators(chat_id)]

def ban(update, context):
    chat_type = update.message.chat.type

    # print(context.bot.get_chat_administrators(update.effective_chat.id))

    if chat_type == "group":
        if update.message.from_user.id in get_admin_ids(context.bot, update.message.chat_id):
            update.message.reply_text("Quer banir quem?")
        else:
            update.message.reply_text("Tu não é admin!")
    else:
        update.message.reply_text("Não pode usar esse comando no privado!")
    # print(update)

ban_handler = CommandHandler("ban", ban)
