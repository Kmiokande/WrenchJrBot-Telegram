import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import CommandHandler

from .keyboard import cpf_keyboard

logger = logging.getLogger(__name__)

def cpf(update, context):
    reply_markup = cpf_keyboard()

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Choose a option",
        reply_markup=reply_markup,
    )

cpf_handler = CommandHandler("cpf", cpf)
