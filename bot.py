import logging
from decouple import config
from core import TelegramCore
from commands import handlers

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


class WrenchJr(TelegramCore):
    def __init__(self):
        super(WrenchJr, self).__init__()
        self._handlers_configured = False
        self.config_handlers()

    def config_handlers(self):
        for config_handler in handlers:
            config_handler(self)
        self._handlers_configured = True


if __name__ == "__main__":
    WrenchJr.instance().run()
