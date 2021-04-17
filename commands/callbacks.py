import json
import logging

import requests
from telegram.ext import CallbackQueryHandler

from .cpf.utils import new_cpf

logger = logging.getLogger(__name__)

cryptos = {
    "btc": "BITCOIN",
    "ltc": "LITECOIN",
    "bch": "BITCOIN CASH",
    "xrp": "RIPPLE",
    "eth": "ETHEREUM",
}

RULES = (
    "⚠️ REGRAS:\n\n"
    "1. Respeitar os membros do grupo.\n"
    "2. Não compartilhar conteúdo pirateado.\n"
    "3. Não enviar Spam.\n"
    "4. Proibido envio de material pornográfico.\n"
    "5. Se quebrar as porras das regras, será banido."
)

def callback_handlers(update, context):
    query = update.callback_query
    data = query.data

    if data in cryptos:
        crypto = requests.get(
            f"https://www.mercadobitcoin.net/api/{data.upper()}/ticker/"
        )

        api = crypto.json()

        _name = cryptos[data]

        query.edit_message_text(
            text=(
                f"[ {_name} ]\n"
                f"💵 ÚLTIMO PREÇO: R$ {float(api['ticker']['last']):.2f}\n"
                f"📈 MAIOR: R$ {float(api['ticker']['high']):.2f}\n"
                f"📉 MENOR: R$ {float(api['ticker']['low']):.2f}"
            )
        )
    elif data == "new_cpf":
        MESSAGE = (
            "✨ Your new CPF\n"
            "{cpf}"
        )
        cpf = new_cpf()
        query.edit_message_text(text=MESSAGE.format(cpf=cpf))
    elif data == "val_cpf":
        query.edit_message_text("Esse comando ainda não está disponível")
    elif data == "cancel":
        query.edit_message_text("Esse comando ainda não está disponível")
    elif data == "rules":
        context.bot.answer_callback_query(
            callback_query_id=query.id,
            text=RULES,
            show_alert=True
        )
    else:
        response = 'Unknown button %s' % data
        print(response)
        logger.info("We shouldn't be here. answer=%s", data)

callback_handlers = CallbackQueryHandler(callback_handlers)
