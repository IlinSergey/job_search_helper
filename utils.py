from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def covering_letter(vacancy_id: int):
    keyboard = [
        [
            InlineKeyboardButton("Cопроводительное письмо", callback_data=vacancy_id),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
