from telegram import InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes, ConversationHandler

from data_base.search_params import create_search_params
from utils import keyboards
from utils.custom_types import SearchParams


async def anketa_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    if query:
        await query.edit_message_text("Введите текст для поиска вакансии:")
    return "vacancy_name"


async def save_vacancy(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    text = update.message.text
    context.user_data["vacancy_name"] = text
    reply_markup = InlineKeyboardMarkup(keyboards.EXPERIENCE_KEYBOARD)
    await update.message.reply_text("Выбери опыт работы:", reply_markup=reply_markup)
    return "experience"


async def save_experience(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()
    context.user_data["experience"] = query.data
    reply_markup = InlineKeyboardMarkup(keyboards.EMPLOYMENT_KEYBOARD)
    await query.edit_message_text("Выбери тип занятости:", reply_markup=reply_markup)
    return "type_of_employment"


async def save_employment(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()
    context.user_data["type_of_employment"] = query.data
    reply_markup = InlineKeyboardMarkup(keyboards.SCHEDULE_KEYBOARD)
    await query.edit_message_text("Выбери график работы:", reply_markup=reply_markup)
    return "schedule"


async def save_schedule(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    schedule = query.data
    params = SearchParams(
        vacancy_name=context.user_data["vacancy_name"],
        experience=context.user_data["experience"],
        type_of_employment=context.user_data["type_of_employment"],
        schedule=schedule,
    )
    create_search_params(user_id=update.effective_user.id, search_params=params)
    if query:
        await query.edit_message_text("Данные для поиска сохранены!")
    return ConversationHandler.END
