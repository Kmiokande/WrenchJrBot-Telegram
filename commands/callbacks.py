import json
import logging

import requests
from telegram.ext import CallbackQueryHandler

logger = logging.getLogger(__name__)

cryptos = {
    "btc": "bitcoin",
    "ada": "cardano",
    "xmr": "monero",
    "eth": "ethereum",
}


def callback_handlers(update, context):
    query = update.callback_query
    data = query.data

    if data in cryptos:
        name_crypto = cryptos[data]
        result = requests.get(
            f"https://api.coingecko.com/api/v3/simple/price?ids={name_crypto}&vs_currencies=brl"
        )

        response = result.json()
        _name = name_crypto.upper()

        query.edit_message_text(
            text=(
                f"[ {_name} ]\n"
                f"💵 PREÇO: R$ {float(response[name_crypto]['brl']):.2f}"
            )
        )
    else:
        response = "Unknown button %s" % data
        print(response)
        logger.info("We shouldn't be here. answer=%s", data)


callback_handlers = CallbackQueryHandler(callback_handlers)
