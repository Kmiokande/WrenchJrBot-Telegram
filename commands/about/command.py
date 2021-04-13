import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import CommandHandler

logger = logging.getLogger(__name__)

def about(update, context):
    keyboard = [
        [
            InlineKeyboardButton(
                "Meu repositório no GitHub",
                callback_data="site",
                url="https://github.com/Kmiokande/WrenchJrBot-Telegram",
            )
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        f"Meu nome é Wrench Jr. Sou programado em Python "
        f"e baseado no robô do Wrench no jogo "
        f"Watch Dogs 2.",
        reply_markup=reply_markup,
        parse_mode=ParseMode.MARKDOWN
    )

about_handler = CommandHandler("about", about)
