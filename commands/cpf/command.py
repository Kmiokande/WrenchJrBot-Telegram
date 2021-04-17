import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import CommandHandler

from ..messages import NOT_GROUP, NEW_CPF
from .utils import new_cpf

logger = logging.getLogger(__name__)


def cpf(update, context):
    chat_type = update.message.chat.type

    if chat_type == "private":
        cpf = new_cpf()

        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=NEW_CPF.format(cpf=cpf),
        )
    elif chat_type == "group":
        update.message.reply_text(NOT_GROUP)


cpf_handler = CommandHandler("cpf", cpf)
