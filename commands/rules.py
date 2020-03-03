import logging
from telegram.ext import CommandHandler
from core import TelegramCore

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)


def rules(update, context):
    update.message.reply_text(
        f"[ 1 ] - Não haver discriminação com religião, raça e sexo.\n"
        f"[ 2 ] - Não discutir política, religião e futebol.\n"
        f"[ 3 ] - Não enviar links maliciosos ou encurtados.\n"
        f"[ 4 ] - Não compartilhar arquivos apk, zip e rar.\n"
        f"[ 5 ] - Proibido compartilhar fotos ou vídeos de acidentes, "
        f"pornografia e informações que não seja de interesse do grupo.\n"
        f"[ 6 ] - Proibido mensagem de cunho comercial, "
        f"venda de produtos ou serviço.\n"
        f"[ 7 ] - Não compartilhar conteúdo sem autorização "
        f"ou qualquer tipo que se encaixe como pirataria.\n"
        f"[ 8 ] - Não ficar conversando com o bot no grupo.\n"
        f"[ 9 ] - Proibido enviar spam.\n")


def config_handlers(instance: TelegramCore):
    instance.add_handler(CommandHandler('rules', rules))
