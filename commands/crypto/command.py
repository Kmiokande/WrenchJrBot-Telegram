import json
import logging
from json.decoder import JSONDecodeError

import requests
from telegram.ext import CommandHandler

logger = logging.getLogger(__name__)

def crypto(update, context):
    cmd = update.message.text
    data = cmd.replace("/crypto ", "")

    crypto = requests.get(f"https://www.mercadobitcoin.net/api/{data.upper()}/ticker/")

    try:
        api = crypto.json()

        if data.upper() == "BTC":
            _name = "[ BITCOIN ]"
        elif data.upper() == "LTC":
            _name = "[ LITECOIN ]"
        elif data.upper() == "BCH":
            _name = "[ BITCOIN CASH ]"
        elif data.upper() == "XRP":
            _name = "[ RIPPLE ]"
        elif data.upper() == "ETH":
            _name = "[ ETHEREUM ]"

        update.message.reply_text(
            f"{_name}\n"
            f"💵 ÚLTIMO PREÇO: R$ {float(api['ticker']['last']):.2f}\n"
            f"📈 MAIOR: R$ {float(api['ticker']['high']):.2f}\n"
            f"📉 MENOR: R$ {float(api['ticker']['low']):.2f}"
        )

    except JSONDecodeError:
        update.message.reply_text(
            "⚠️ O comando precisa de um valor de entrada!\n\n"
            "Exemplo:\n"
            "/crypto BTC : Bitcoin\n"
            "/crypto LTC : Litecoin\n"
            "/crypto BCH : BCash\n"
            "/crypto XRP : Ripple\n"
            "/crypto ETH : Ethereum"
        )

crypto_handler = CommandHandler("crypto", crypto)
