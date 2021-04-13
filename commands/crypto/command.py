import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import CommandHandler

logger = logging.getLogger(__name__)

def crypto(update, context):
    keyboard = [
        [
            InlineKeyboardButton(
                "Bitcoin",
                callback_data='btc'),
        ],
        [
            InlineKeyboardButton(
                "Litecoin",
                callback_data='ltc'),
            InlineKeyboardButton(
                "Bitcoin Cash",
                callback_data='bch'),
        ],
        [
            InlineKeyboardButton(
                "Ripple",
                callback_data='xrp'),
                        InlineKeyboardButton(
                "Ethereum",
                callback_data='eth'),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        f"Choose a cryptocurrency\n",
        reply_markup=reply_markup,
        parse_mode=ParseMode.MARKDOWN
    )

crypto_handler = CommandHandler("crypto", crypto)
