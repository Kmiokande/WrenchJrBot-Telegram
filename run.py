import logging
from bot import WrenchJr

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    updater = WrenchJr.instance()
    updater.run()
