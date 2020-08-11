import logging
from decouple import config
from bot import WrenchJr

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    updater = WrenchJr.instance()
    try:
        mode = config("MODE", default="cmd")
        if mode == "cmd":
            updater.run_cmd()
        elif mode == "web":
            updater.run_web()
        else:
            raise Exception("O modo passado não foi reconhecido!")

    except Exception as e:
        logging.error(f'Modo: {config("MODE", default="cmd")}')
        logging.error(f"token: {updater.token}")
        logging.error(f"Port: {updater.port}")
        logging.error(f"heroku app name: {updater.server_url}")
        raise e
