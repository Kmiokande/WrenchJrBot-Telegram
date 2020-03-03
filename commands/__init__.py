from commands.start import config_handlers as start_handler
from commands.about import config_handlers as about_handler
from commands.rules import config_handlers as rules_handler
from commands.crypto import config_handlers as crypto_handler

handlers = [
    start_handler,
    about_handler,
    rules_handler,
    crypto_handler
]