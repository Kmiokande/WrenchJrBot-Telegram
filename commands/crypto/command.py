import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import CommandHandler

from .keyboard import crypto_keyboard

logger = logging.getLogger(__name__)


def crypto(update, context):
    reply_markup = crypto_keyboard()

    update.message.reply_text(
        f"Choose a cryptocurrency\n",
        reply_markup=reply_markup,
        parse_mode=ParseMode.MARKDOWN,
    )


crypto_handler = CommandHandler("crypto", crypto)
