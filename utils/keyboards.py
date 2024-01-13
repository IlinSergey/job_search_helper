from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def covering_letter_keyboard(vacancy_id: int) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("Cопроводительное письмо", callback_data=vacancy_id),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


START_KEYBOARD = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Заполнить анкету", callback_data="анкета")
        ]
    ])
