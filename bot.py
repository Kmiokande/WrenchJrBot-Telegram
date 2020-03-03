import logging
from decouple import config

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)


class WrenchJr():
    def __init__(self):
        super(WrenchJr, self).__init__()
