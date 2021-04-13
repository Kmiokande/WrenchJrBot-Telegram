import logging

logger = logging.getLogger(__name__)

ERROR_INITIATE = (
    "Inicie uma conversa comigo para que eu possa te enviar uma mensagem!"
)

ERROR_BLOCKED = (
    "Acho bom você me desbloquear!"
)

def error_handler(update, context):
    error_name = context.error.__class__.__name__
    error_message = str(context.error)

    if error_message == "Forbidden: bot can't initiate conversation with a user":
        update.message.reply_text(ERROR_INITIATE)
    elif error_message == "Forbidden: bot was blocked by the user":
        update.message.reply_text(ERROR_BLOCKED)
    else:
        logger.warning('Update "%s" caused error "%s"', update, err)
