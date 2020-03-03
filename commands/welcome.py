import logging
from telegram.ext import MessageHandler, Filters
from core import TelegramCore

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)


def welcome(update, context):
    new_member = update.message.new_chat_members[0]
    _full_name = new_member.full_name
    _title = update.message.chat.title

    update.message.reply_text(
        f"Olá {_full_name}, seja bem-vindo(a) ao {_title}.\n\n"
        f"Digite o comando /rules para ler nossas regras e ter "
        f"um bom convívio com os demais integrantes.")


def config_handlers(instance: TelegramCore):
    instance.add_handler(MessageHandler(
        Filters.status_update.new_chat_members, welcome))
