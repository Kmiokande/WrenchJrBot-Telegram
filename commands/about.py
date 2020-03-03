import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import CommandHandler
from core import TelegramCore

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)


def about(update, context):
    keyboard = [
        [
            InlineKeyboardButton(
                "Meu repositório no GitHub",
                callback_data='site',
                url='https://github.com/Kmiokande/WrenchJrBot-Telegram')
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        f"Meu nome é Wrench Jr. Sou programado em Python "
        f"e baseado no robô do Wrench no jogo "
        f"Watch Dogs 2.",
        reply_markup=reply_markup,
        parse_mode=ParseMode.MARKDOWN)


def config_handlers(instance: TelegramCore):
    instance.add_handler(CommandHandler('about', about))
