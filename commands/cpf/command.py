import logging

from telegram.ext import CommandHandler

from .utils import new_cpf

logger = logging.getLogger(__name__)

MESSAGE = (
    "✨ Your new CPF\n"
    "{cpf}"
)

def cpf(update, context):
    chat_type = update.message.chat.type
    cpf = new_cpf()

    if chat_type == "private":
        update.message.reply_text(MESSAGE.format(cpf=cpf))

cpf_handler = CommandHandler("cpf", cpf)