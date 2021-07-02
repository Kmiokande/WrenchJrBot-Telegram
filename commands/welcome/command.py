import logging

from telegram.ext import Filters, MessageHandler

logger = logging.getLogger(__name__)


def welcome(update, context):
    new_member = update.message.new_chat_members[0]
    bot = new_member.is_bot

    if not bot:
        _full_name = new_member.full_name
        _title = update.message.chat.title

        update.message.reply_text(
            f"Olá {_full_name}, seja bem-vindo(a) ao {_title}.\n\n"
            f"Digite o comando /rules para ler nossas regras e ter "
            f"um bom convívio com os demais integrantes."
        )


welcome_handler = MessageHandler(Filters.status_update.new_chat_members, welcome)
