import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

logger = logging.getLogger(__name__)

def welcome_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "Resumo das regas",
                callback_data='rules')
        ],
    ]

    return InlineKeyboardMarkup(keyboard)
