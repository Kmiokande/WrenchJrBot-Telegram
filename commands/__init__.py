from commands.about import config_handlers as about_handler
from commands.crypto import config_handlers as crypto_handler
from commands.qrcode import config_handlers as qr_code
from commands.rules import config_handlers as rules_handler
from commands.start import config_handlers as start_handler
from commands.unknown import config_handlers as unknown_handler
from commands.welcome import config_handlers as welcome_handler

handlers = [
    start_handler,
    welcome_handler,
    about_handler,
    rules_handler,
    crypto_handler,
    qr_code,
    unknown_handler
]
