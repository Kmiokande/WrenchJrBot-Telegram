import logging

from telegram.ext import CommandHandler

logger = logging.getLogger(__name__)

RULES = (
    "[ 1 ] - Não haver discriminação com religião, raça e sexo.\n"
    "[ 2 ] - Não discutir política, religião e futebol.\n"
    "[ 3 ] - Não enviar links maliciosos ou encurtados.\n"
    "[ 4 ] - Não compartilhar arquivos apk, zip e rar.\n"
    "[ 5 ] - Proibido compartilhar fotos ou vídeos de acidentes, "
    "pornografia e informações que não seja de interesse do grupo.\n"
    "[ 6 ] - Proibido mensagem de cunho comercial, "
    "venda de produtos ou serviço.\n"
    "[ 7 ] - Não compartilhar conteúdo sem autorização "
    "ou qualquer tipo que se encaixe como pirataria.\n"
    "[ 8 ] - Não ficar conversando com o bot no grupo.\n"
    "[ 9 ] - Proibido enviar spam.\n"
)

def rules(update, context):
    user_id = update.message.from_user.id
    context.bot.sendMessage(
        chat_id=user_id,
        text=RULES)

rules_handler = CommandHandler("rules", rules)
