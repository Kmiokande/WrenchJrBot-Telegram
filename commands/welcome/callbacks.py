import logging

from telegram.ext import CallbackQueryHandler

logger = logging.getLogger(__name__)

RULES = (
    "⚠️ REGRAS:\n\n"
    "1. Respeitar os membros do grupo.\n"
    "2. Não compartilhar conteúdo pirateado.\n"
    "3. Não enviar Spam.\n"
    "4. Proibido envio de material pornográfico.\n"
    "5. Se quebrar as porras das regras, será banido."
)

def rules_callback_handler(update, context):
    query = update.callback_query

    if query.data == "rules":
        context.bot.answer_callback_query(
            callback_query_id=query.id,
            text=RULES,
            show_alert=True
        )

rules_callback = CallbackQueryHandler(rules_callback_handler)
