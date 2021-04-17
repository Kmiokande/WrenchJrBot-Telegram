import logging

from telegram import ParseMode
from telegram.ext import Filters, MessageHandler

from .keyboard import welcome_keyboard

logger = logging.getLogger(__name__)

def welcome(update, context):
    new_member = update.message.new_chat_members[0]
    bot = new_member.is_bot

    if not bot:
        _full_name = new_member.full_name
        _title = update.message.chat.title

        reply_markup = welcome_keyboard()
        update.message.reply_text(
            f"Olá {_full_name}, seja bem-vindo(a) ao {_title}.\n\n"
            f"Digite o comando /rules para ler nossas regras e ter "
            f"um bom convívio com os demais integrantes.\n"
            f"Ou se preferir, clique no botão abaixo para ler as "
            f"regras resumidas.",
            reply_markup=reply_markup,
            parse_mode=ParseMode.MARKDOWN
        )

welcome_handler = MessageHandler(
    Filters.status_update.new_chat_members, welcome
)
