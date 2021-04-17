import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import CommandHandler

from .utils import new_cpf

logger = logging.getLogger(__name__)

MESSAGE = "✨ Your new CPF\n" "{cpf}"


def cpf(update, context):
    cpf = new_cpf()

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=MESSAGE.format(cpf=cpf),
    )


cpf_handler = CommandHandler("cpf", cpf)
