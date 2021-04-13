import logging

logger = logging.getLogger(__name__)

ERROR_INITIATE = (
    "Inicie uma conversa comigo para que eu possa te enviar uma mensagem!"
)

ERROR_BLOCKED = (
    "Acho bom você me desbloquear!"
)

def error_handler(update, context):
    error = str(context.error)

    if error == "Forbidden: bot can't initiate conversation with a user":
        update.message.reply_text(ERROR_INITIATE)
    elif error == "Forbidden: bot was blocked by the user":
        update.message.reply_text(ERROR_BLOCKED)
    else:
        logger.warning(f"Update {update} caused error {error}")
