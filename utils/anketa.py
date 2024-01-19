from telegram import InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes, ConversationHandler

from data_base.user import set_vacancy
from utils import keyboards


async def anketa_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    if query:
        await query.edit_message_text("Введите текст для поиска вакансии:")
    return "vacancy_name"


async def save_vacancy(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    text = update.message.text
    set_vacancy(update.effective_user, text)  # type: ignore [arg-type]
    reply_markup = InlineKeyboardMarkup(keyboards.EXPERIENCE_KEYBOARD)
    await update.message.reply_text("Выбери опыт работы:", reply_markup=reply_markup)
    return "experience"


async def save_experience(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()
    #  save query.data
    reply_markup = InlineKeyboardMarkup(keyboards.EMPLOYMENT_KEYBOARD)
    await query.edit_message_text("Выбери тип занятости:", reply_markup=reply_markup)
    return "type_of_employment"


async def save_employment(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()
    # save query.data
    reply_markup = InlineKeyboardMarkup(keyboards.SCHEDULE_KEYBOARD)
    await query.edit_message_text("Выбери график работы:", reply_markup=reply_markup)
    return "schedule"


async def save_schedule(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    if query:
        await query.edit_message_text("Данные для поиска сохранены!")
    return ConversationHandler.END
