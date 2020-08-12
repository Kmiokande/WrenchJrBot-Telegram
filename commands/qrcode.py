import logging

import qrcode
from telegram.ext import CommandHandler

from core import TelegramCore

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


def qr_code(update, context):
    qr = qrcode.QRCode(version=5, box_size=15, border=5)
    data = update.message.text.replace("/qrcode", "")

    if not data:
        update.message.reply_text(
            f"⚠️ O comando precisa de um valor de entrada!\n\n"
            f"Exemplo:\n"
            f"/qrcode www.site.com"
        )
    else:
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")
        img.save("imgs/qrcode/myQR.png")
        qr_img = open("imgs/qrcode/myQR.png", "rb")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=qr_img)


def config_handlers(instance: TelegramCore):
    instance.add_handler(CommandHandler("qrcode", qr_code))
