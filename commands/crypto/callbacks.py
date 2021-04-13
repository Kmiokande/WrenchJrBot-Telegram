import json
import logging

import requests
from telegram.ext import CallbackQueryHandler

logger = logging.getLogger(__name__)

def crypto_callback_handler(update, context):
    query = update.callback_query
    data = query.data.upper()

    crypto = requests.get(
        f"https://www.mercadobitcoin.net/api/{data}/ticker/"
    )

    api = crypto.json()

    if data == "BTC":
        _name = "[ BITCOIN ]"
    elif data == "LTC":
        _name = "[ LITECOIN ]"
    elif data == "BCH":
        _name = "[ BITCOIN CASH ]"
    elif data == "XRP":
        _name = "[ RIPPLE ]"
    elif data == "ETH":
        _name = "[ ETHEREUM ]"

    query.edit_message_text(
        text=(
            f"{_name}\n"
            f"💵 ÚLTIMO PREÇO: R$ {float(api['ticker']['last']):.2f}\n"
            f"📈 MAIOR: R$ {float(api['ticker']['high']):.2f}\n"
            f"📉 MENOR: R$ {float(api['ticker']['low']):.2f}"
        )
    )

crypto_callback = CallbackQueryHandler(crypto_callback_handler)
