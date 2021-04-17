from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def cpf_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "New CPF",
                callback_data="new_cpf"
            ),
            InlineKeyboardButton(
                "Validate CPF",
                callback_data="val_cpf"
            ),
        ],
        [
            InlineKeyboardButton(
                "Cancel",
                callback_data="cancel"
            ),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)