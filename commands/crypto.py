import logging
from telegram.ext import CommandHandler
from core import TelegramCore
import requests
import json
from json.decoder import JSONDecodeError

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)


def crypto(update, context):
    cmd = update.message.text
    data = cmd.replace('/crypto ', '')

    crypto = requests.get(f'https://www.mercadobitcoin.net/api/{data.upper()}/ticker/')

    try:
        api = crypto.json()

        if data.upper() == 'BTC':
            _name = '[ BITCOIN ]'
        elif data.upper() == 'LTC':
            _name = '[ LITECOIN ]'
        elif data.upper() == 'BCH':
            _name = '[ BITCOIN CASH ]'
        elif data.upper() == 'XRP':
            _name = '[ RIPPLE ]'
        elif data.upper() == 'ETH':
            _name = '[ ETHEREUM ]'

        update.message.reply_text(
            f"{_name}\n"
            f"💵 ÚLTIMO PREÇO: R$ {float(api['ticker']['last']):.2f}\n"
            f"📈 MAIOR: R$ {float(api['ticker']['high']):.2f}\n"
            f"📉 MENOR: R$ {float(api['ticker']['low']):.2f}")

    except JSONDecodeError:
        update.message.reply_text(
            f"⚠️ O comando precisa de um valor de entrada!\n\n"
            f"Exemplo:\n"
            f"/crypto BTC : Bitcoin\n"
            f"/crypto LTC : Litecoin\n"
            f"/crypto BCH : BCash\n"
            f"/crypto XRP : Ripple\n"
            f"/crypto ETH : Ethereum")


def config_handlers(instance: TelegramCore):
    instance.add_handler(CommandHandler('crypto', crypto))
