import logging
from decouple import config
from core import TelegramCore

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)


class WrenchJr(TelegramCore):
    def __init__(self):
        super(WrenchJr, self).__init__()


if __name__ == '__main__':
    WrenchJr.instance().run()
