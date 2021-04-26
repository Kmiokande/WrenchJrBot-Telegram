import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

logger = logging.getLogger(__name__)


def crypto_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("Bitcoin", callback_data="btc"),
            InlineKeyboardButton("Ethereum", callback_data="eth"),
        ],
        [
            InlineKeyboardButton("Cardano", callback_data="ada"),
            InlineKeyboardButton("Monero", callback_data="xmr"),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)
