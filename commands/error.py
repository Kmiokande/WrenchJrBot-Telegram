import logging

from core import TelegramCore

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

ERROR_INITIATE = (
    "Por favor, inicie uma conversa comigo para que eu possa te enviar uma mensagem!"
)

ERROR_BLOCKED = (
    "Você me bloqueou?! Tsc tsc. Que feio!!!🙄"
)

def error(update, context, err):
    if err.message == "Forbidden: bot can't initiate conversation with a user":
        update.message.reply_text(ERROR_INITIATE)
    elif err.message == "Forbidden: bot was blocked by the user":
        update.message.reply_text(ERROR_BLOCKED)
    else:
        logger.warning('Update "%s" caused error "%s"', update, err)

def config_handlers(instance: TelegramCore):
    instance.add_error_handler(error)
