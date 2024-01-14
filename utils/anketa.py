from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes, ConversationHandler

from data_base.user import set_vacancy


async def anketa_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    if query:
        await query.edit_message_text("Введите текст для поиска вакансии:")
    return "vacancy_name"


async def save_vacancy(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    text = update.message.text
    set_vacancy(update.effective_user, text)  # type: ignore [arg-type]
    keyboard = [
        [
            InlineKeyboardButton("Нет опыта", callback_data="noExperience"),
        ],
        [
            InlineKeyboardButton("От 1 года до 3 лет", callback_data="between1And3"),
        ],
        [
            InlineKeyboardButton("От 3 до 6 лет", callback_data="between3And6"),
        ],
        [
            InlineKeyboardButton("Более 6 лет", callback_data="moreThan6"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выбери опыт работы:", reply_markup=reply_markup)
    return "experience"


async def save_experience(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    if query:
        await query.edit_message_text("Данные для поиска сохранены!")
    return ConversationHandler.END
